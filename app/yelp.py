import requests, json, os
from dotenv import load_dotenv
load_dotenv()

class YelpAPI:

    def __init__(self):
        api_key = str(os.getenv('api_key'))
        self.headers = {'Authorization': 'Bearer %s' % api_key}
    
    def search(self, query, location, limit=5, sort_by='best_match', price="1,2,3,4", open_now=False):
        """ search for businesses by query and location """
    
        url = 'https://api.yelp.com/v3/businesses/search'
        if open_now == "true":
            open_now = True
        else:
            open_now = False
            
        params = {
            'term': query,
            'location': location, 
            'limit': limit, 
            'sort_by': sort_by,
            'price': price,
            'open_now': open_now
            }
        
        res = requests.get(url, params = params, headers = self.headers)
        
        return json.loads(res.text)
        
    def reviews(self, business_id):
        """ search for business reviews by business id """
        
        url = "https://api.yelp.com/v3/businesses/{}/reviews".format(business_id)
        res = requests.get(url, headers = self.headers)
        return json.loads(res.text)

    def category(self, query):
        """ search for business reviews by business id """
        
        url = "https://api.yelp.com/v3/categories/{}".format(query)
        res = requests.get(url, headers = self.headers)
        return json.loads(res.text)



    