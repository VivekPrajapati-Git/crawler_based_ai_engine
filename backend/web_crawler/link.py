import os
from dotenv import load_dotenv
from serpapi import GoogleSearch

load_dotenv()
serpapi_key = os.getenv("serpapi_key")

def get_top_link(data):
    #Defining the params for serpapi for fetching the result
    params = {
        'engine' : 'google',
        'q' : data,
        'api_key' : serpapi_key,        
    }

    search = GoogleSearch(params)
    result = search.get_dict() #Getting the result
    
    links = []
    # Appending all the links that is visited
    for result in result.get('organic_results',[]):
        links.append(result["link"])

    return links