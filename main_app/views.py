from django.shortcuts import render, redirect
from .stamp_class import stamps
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Stamp, Attraction, Photo
from .forms import WeatherForm

import uuid
import boto3

# Create your views here.
from django.http import HttpResponse

S3_BASE_URL = 'https://s3-us-west-1.amazonaws.com/'
BUCKET = 'passportstampcollector'


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def stamps_index(request):
    stamps = Stamp.objects.filter(user=request.user)
    return render(request, 'stamps/index.html', {'stamps': stamps})

@login_required
def stamp_details(request, stamp_id):
    stamp = Stamp.objects.get(id=stamp_id)
    attractions_i_have_not_seen = Attraction.objects.exclude(id__in = stamp.attractions.all().values_list('id'))
    weather_form = WeatherForm()
    context = {
        'stamp': stamp,
        'weather_form': weather_form,
        'attractions': attractions_i_have_not_seen
    }
    return render(request, 'stamps/detail.html', context)

@login_required
def add_weather(request, stamp_id):
    form = WeatherForm(request.POST)

    if form.is_valid():
        new_weather = form.save(commit=False)
        new_weather.stamp_id = stamp_id
        new_weather.save()
    return redirect ('detail', stamp_id=stamp_id)

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login (request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)


class StampCreate(LoginRequiredMixin, CreateView):
    model = Stamp
    fields = ['country', 'date', 'color', 'shape']
    success_url = '/stamps/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class StampUpdate(LoginRequiredMixin, UpdateView):
    model = Stamp
    fields = ['date', 'color', 'shape']

class StampDelete(LoginRequiredMixin, DeleteView):
    model = Stamp
    success_url = '/stamps/'

@login_required
def assoc_attraction(request, stamp_id, attraction_id):
    Stamp.objects.get(id=stamp_id).attractions.add(attraction_id)
    return redirect('detail', stamp_id=stamp_id)

@login_required
def add_photo(request, stamp_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            photo = Photo(url=url, stamp_id=stamp_id)
            photo.save()
        except:
            print('An error occurred uploading file to S3')
    return redirect('detail', stamp_id=stamp_id)