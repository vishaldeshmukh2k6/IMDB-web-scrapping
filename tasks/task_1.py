import requests, json
from bs4 import BeautifulSoup

def scrape_top_list():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
    }
    url = "https://www.imdb.com/chart/top/"

    html_content = requests.get(url, headers=headers).content
    soup = BeautifulSoup(html_content,"html.parser")
    movies = []

    movie_list = soup.find("ul", class_="ipc-metadata-list ipc-metadata-list--dividers-between sc-e22973a9-0 khSCXM compact-list-view ipc-metadata-list--base").find_all("li")
    for movie in movie_list:
        film = {}
        film['name']= movie.find('h3', class_="ipc-title__text").text
        movies.append(film)
        
        
    with open("data/movies.json", 'w+') as f:
        json.dump(movies, f, indent=4)
    return movies