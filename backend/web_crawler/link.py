import os
from dotenv import load_dotenv
from serpapi import GoogleSearch

load_dotenv()
serpapi_key = os.getenv("serpapi_key")

def link(data):
    params = {
        'engine' : 'google',
        'q' : data,
        'api_key' : serpapi_key,        
    }

    search = GoogleSearch(params)
    result = search.get_dict()
    
    links = []
    for result in result.get('organic_results',[]):
        links.append(result["link"])

    return links