import requests, json, os
from bs4 import BeautifulSoup

def get_all_top_movies_grouped_by_year():    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
    }
    url = "https://www.imdb.com/chart/top/"

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    movies = {}

    movie_list = soup.find("ul", class_="ipc-metadata-list ipc-metadata-list--dividers-between sc-e22973a9-0 khSCXM compact-list-view ipc-metadata-list--base")


    position = 1
    
    for movie in movie_list:
        position += 1

        name = movie.select_one("h3.ipc-title__text").text.strip()
        info_div = movie.select_one("div.cli-title-metadata")
        spans = info_div.find_all("span")
        year = int(spans[0].text)
        run_time = spans[1].text if len(spans) > 1 else None
        rating_tag = movie.select_one("span.ipc-rating-star--rating")
        rating = float(rating_tag.text)
        link_tag = movie.select_one("a.ipc-title-link-wrapper")

        add_url = link_tag['href']
        full_url = "https://www.imdb.com" + add_url

        movie_data = {
            'name': name,
            'year': year,
            'run_time': run_time,
            'position': position,
            'rating': rating,
            'url': full_url
        }

        if year not in movies:
            movies[year] = []
        movies[year].append(movie_data)

    
    with open("data/movies_data.json", 'w') as f:
        json.dump(movies, f, indent=4)

    return movies


