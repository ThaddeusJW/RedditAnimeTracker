import requests
import json
from bs4 import BeautifulSoup

url = 'https://www.reddit.com/r/anime/search/?q=discussion&restrict_sr=1&t=week'

request = requests.get(url)

soup = BeautifulSoup(request.text, 'html.parser')

def getTitles():

    titles = soup.find_all("a", {"data-testid": "post-title"})
    title_list = []

    for title in titles:
        title_list.append(title.text.strip())
    
    # print(title_list)
    return title_list

def getURLs():

    urls = soup.find_all("a", {"data-testid": "post-title"})
    url_list = []
    for url in urls:
        url_list.append(url.get('href'))

    # print(url_list)
    return url_list

# title_list = getTitles()
# url_list = getURLs()

# disc_dict = dict(zip(title_list, url_list))

# print(len(disc_dict.keys()))

# for k, v in disc_dict.items():
#     print(f"Title: {k}\nURL: {v}\n")
#     break

disc_1 = requests.get('https://www.reddit.com/r/anime/comments/15jsfn1/mushoku_tensei_isekai_ittara_honki_dasu_season_2/')
soup = BeautifulSoup(disc_1.text, 'html.parser')

table = soup.find_all('table')

for tr in table:
    for td in tr.find_all('td'):
        print(td.text.strip())

