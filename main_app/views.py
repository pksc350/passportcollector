from django.shortcuts import render, redirect
from .stamp_class import stamps
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Stamp, Attraction
from .forms import WeatherForm

# Create your views here.
from django.http import HttpResponse


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def stamps_index(request):
    stamps = Stamp.objects.all()
    return render(request, 'stamps/index.html', {'stamps': stamps})


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

def add_weather(request, stamp_id):
    form = WeatherForm(request.POST)

    if form.is_valid():
        new_weather = form.save(commit=False)
        new_weather.stamp_id = stamp_id
        new_weather.save()
    return redirect ('detail', stamp_id=stamp_id)


class StampCreate(CreateView):
    model = Stamp
    fields = '__all__'

class StampUpdate(UpdateView):
    model = Stamp
    fields = ['date', 'color', 'shape']

class StampDelete(DeleteView):
    model = Stamp
    success_url = '/stamps/'


def assoc_attraction(request, stamp_id, attraction_id):
    Stamp.objects.get(id=stamp_id).attractions.add(attraction_id)
    return redirect('detail', stamp_id=stamp_id)