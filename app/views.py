from django.shortcuts import render
from .yelp import YelpAPI
# Create your views here.
from django.http import HttpResponse


def index(request):
    yelp = YelpAPI()
    print(yelp.search("barber", "nyc"))
    
    return HttpResponse("Hello, world. You're at the polls index.")