from bs4 import BeautifulSoup
import requests
import random

def user_agent():
    url = 'https://www.imdb.com/chart/top/?ref_=nv_mv_250'
    user_agents = ['Mozilla/5.0 (iPhone; CPU iPhone OS 5_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9B179 Safari/7534.48.3'
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36']
    HEADER = {'User-Agent': random.choice(user_agents)}
    page = requests.get(url, headers=HEADER)
    return page

def parse():
    connect = user_agent()
    filtered = {}
    if connect.status_code == 200:
        soup = BeautifulSoup(connect.text, "html.parser")
        allfilms= soup.findAll('div', class_='ipc-metadata-list-summary-item__tc')
        for data in allfilms:
            movie_link = data.find('h3', {'class': 'ipc-title__text'}).text
            movie_desc = data.find('span', {'class': 'ipc-rating-star--imdb'}).text.strip().split()[0]
            filtered[movie_link] = movie_desc
        for key, value in filtered.items():
            print(key, "-", value)
    else:
        print("sorry, we have small error :(\n Try again")