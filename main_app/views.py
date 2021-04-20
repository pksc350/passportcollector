from django.shortcuts import render
from .stamp_class import stamps
from .models import Stamp

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
    context = {
        'stamp': stamp
    }
    return render(request, 'stamps/detail.html', context)