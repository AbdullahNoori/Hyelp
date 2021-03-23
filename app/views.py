from django.shortcuts import render
from .yelp import YelpAPI
from django.http import HttpResponse

def index(request):
    yelp = YelpAPI()
    yelp_results = yelp.search("hotel", "San Francisco", 10)
    context = {
        "featured_businesses": yelp_results['businesses']
    }
    return render(request, 'app/home-v2.html', context)

def detail(request):
    yelp = YelpAPI()
    print(yelp.search("barber", "nyc"))
    return render(request, 'app/detail.html')

def search(request):
    
    query = request.GET.get('query', "Hotel")
    location = request.GET.get('location', "San Francisco")
    price = request.GET.get('price', "1,2,3,4")
    sort_by = request.GET.get('sort_by', "best_match")
    open_now = request.GET.get('open_now', False)
    
    yelp = YelpAPI()
    yelp_results = yelp.search(query, location, 10, sort_by, price, open_now)
    yelp_featured = yelp.search(query, location, 5, "rating")
    
    context = {
        "data": yelp_results['businesses'],
        "yelp_featured": yelp_featured['businesses'],
        "location": location,
        "query": query, 
        "price": price,
        "sort_by": sort_by,
        "open_now": open_now
    }
    
    return render(request, 'app/home-v2.html', context)