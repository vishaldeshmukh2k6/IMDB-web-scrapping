import requests, json
from bs4 import BeautifulSoup
import re

def scrape_top_list():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
    }
    url = "https://www.imdb.com/chart/top/"

    html_content = requests.get(url, headers=headers).content
    soup = BeautifulSoup(html_content, "html.parser")
    movies = []

    movie_list = soup.find("ul", class_=re.compile("compact-list-view")).find_all("li")

    for movie in movie_list:
        film = {}

        title_tag = movie.find('h3', class_="ipc-title__text")
        film['name'] = title_tag.text if title_tag else "N/A"

        info_div = movie.find("div", class_=re.compile("cli-title-metadata"))
        if info_div:
            spans = info_div.find_all("span")
            film['year'] = spans[0].text if len(spans) > 0 else "N/A"
            film['run_time'] = spans[1].text if len(spans) > 1 else "N/A"
        else:
            film['year'] = "N/A"
            film['run_time'] = "N/A"

        rating_tag = movie.find("span", class_="ipc-rating-star--rating")
        film['rating'] = rating_tag.text if rating_tag else "N/A"

        link_tag = movie.find("a", class_="ipc-title-link-wrapper")
        film['url'] = "https://www.imdb.com" + link_tag["href"] if link_tag else "N/A"

        movies.append(film)

    with open("data/task_1.json", 'w+', encoding='utf-8') as f:
        json.dump(movies, f, indent=4, ensure_ascii=False)
    return movies
