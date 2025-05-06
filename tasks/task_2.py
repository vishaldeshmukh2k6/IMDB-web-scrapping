import requests, json
from bs4 import BeautifulSoup

def group_by_year():    

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
        film['name'] = movie.find('h3', class_="ipc-title__text").text

        
        info_div = movie.find("div", class_="sc-5179a348-6 bnnHxo cli-title-metadata") 
        if info_div:
            spans = info_div.find_all("span")
            film['year'] = spans[0].text if len(spans) > 0 else None
            film['run_time'] = spans[1].text if len(spans) > 1 else None
        else:
            film['year'] = None
            film['run_time'] = None

        film['rating'] = movie.find("span", class_="ipc-rating-star--rating").text
        add_main_url = movie.find("a", class_="ipc-title-link-wrapper")["href"]
        film['url'] = "https://www.imdb.com" + add_main_url

        movies.append(film)

    with open("data/movies_data.json", 'w+') as f:
        json.dump(movies, f, indent=4)
    return movies

