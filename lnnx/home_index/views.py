# Create your views here.
from django.shortcuts import render_to_response
from django.conf import settings

def index(request):
    return render_to_response('home/index.html')