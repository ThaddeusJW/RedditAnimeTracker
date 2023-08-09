import requests
import json
from bs4 import BeautifulSoup

url = 'https://www.reddit.com/r/anime/search/?q=discussion&restrict_sr=1&t=week'
headers = {"User-Agent": 
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"}
request = requests.get(url, headers=headers)

soup = BeautifulSoup(request.text, 'html.parser')

def getTitles():

    titles = soup.find_all("a", {"data-testid": "post-title"})
    title_list = []

    for title in titles:
        if 'Episode' in title.text:
            title_list.append(title.text.strip())
        
        else:
            pass
    
    # print(title_list)
    return title_list

def getURLs():

    urls = soup.find_all("a", {"data-testid": "post-title"})
    url_list = []
    for url in urls:
        if 'Episode' in url.text:
            url_list.append(url.get('href'))

        else:
            pass

    # print(url_list)
    return url_list

def getRatings(url_list):

    counter = 0
    labels = ['Episode', 'Rating']

    for link in url_list:

        page = requests.get('https://reddit.com'+link, headers=headers)
        soup = BeautifulSoup(page.text, 'html.parser')
        temp_url = 'https://reddit.com'+link
        print(temp_url)

        table = soup.find_all('table')
        print(f"Info for {title_list[counter][:45]}...:")
        for tr in table:
            d = 0
            for td in tr.find_all('td'):
                if "Link" in td.text:
                        pass
                
                else:
                    print(labels[d%2], td.text.strip())
                    d += 1

        print("\n")
        counter += 1


def getComments():
    
    counter = 0

    for link in url_list:

        page = requests.get('https://reddit.com'+link, headers=headers)
        soup = BeautifulSoup(page.text, 'html.parser')
        temp_url = 'https://reddit.com'+link
        print(temp_url)

        comments = soup.find_all('span')
        print(soup)

        counter += 1

        break
    


title_list = getTitles()
url_list = getURLs()

disc_dict = dict(zip(title_list, url_list))

print(f"Top {len(title_list)} Episode Discussions for the week")

for k, v in disc_dict.items():
    print(f"Title: {k}\nURL: {v}\n")
    
ratings = getRatings(url_list)
