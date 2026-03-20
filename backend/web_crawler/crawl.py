import requests
import time
from bs4 import BeautifulSoup
from link import get_top_link
import re

def crawl(data):
    links = get_top_link(data) #Getting the top links
    print(links)
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept": "text/html,application/xhtml+xml",
        "Connection": "keep-alive"
    }

    # Iterating over the link to parse the web page
    for url in links:
        # Fetching the documents using requests method
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            html_content = response.text # Getting the content
            soup = BeautifulSoup(html_content,'lxml')
            count = 1
            result = re.findall("<p>")
            print(result)
            # with open(f'text{count}.html', 'w', encoding='utf-8') as f:
            #     f.write(html_content)
            # count = count+1
            time.sleep(3)
        else:
            print(f"Failed to retrieve page: {response.status_code}")


crawl("machinelearning")