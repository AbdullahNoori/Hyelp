import requests, json, os
from dotenv import load_dotenv
load_dotenv()

class YelpAPI:

    def __init__(self):
        api_key = str(os.getenv('api_key'))
        self.headers = {'Authorization': 'Bearer %s' % api_key}
    
    def search(self, query, location):
        """ search for businesses by query and location """
    
        url = 'https://api.yelp.com/v3/businesses/search'
        params = {'term': query,'location': location}
        res = requests.get(url, params = params, headers = self.headers)
        
        return json.loads(res.text)
        
    def reviews(self, business_id):
        """ search for business reviews by business id """
        
        url = "https://api.yelp.com/v3/businesses/{}/reviews".format(business_id)
        res = requests.get(url, headers = self.headers)
        return json.loads(res.text)



    