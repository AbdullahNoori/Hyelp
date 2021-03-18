from django.shortcuts import render
from .yelp import YelpAPI
from django.http import HttpResponse

def index(request):
    yelp = YelpAPI()
    print(yelp.search("barber", "nyc"))
    return render(request, 'app/home-v2.html')
    # return HttpResponse("Hello, world. You're at the polls index.")