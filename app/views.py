from django.shortcuts import render
from .yelp import YelpAPI
from django.http import HttpResponse

def index(request):
    yelp = YelpAPI()
    yelp_results = yelp.search("hotel", "San Francisco")
    context = {
        "data": yelp_results['businesses']
    }
    return render(request, 'app/home-v2.html', context)

def detail(request):
    yelp = YelpAPI()
    print(yelp.search("barber", "nyc"))
    return render(request, 'app/detail.html')

def search(request):
    
    query = request.GET.get('query', "Hotel")
    location = request.GET.get('location', "San Francisco")
    yelp = YelpAPI()
    yelp_results = yelp.search(query, location)
    context = {
        "data": yelp_results['businesses']
    }
    print(yelp_results)
    
    return render(request, 'app/home-v2.html', context)