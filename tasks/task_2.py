import  json
from tasks.task_1 import scrape_top_list

def get_all_top_movies_grouped_by_year(movies):
    grouped_data = {}
    for movie in movies:
        year = movie['year']
        if year not in grouped_data:
            grouped_data[year] = []
        grouped_data[year].append(movie)
    return grouped_data

all_movies = scrape_top_list()
grouped = get_all_top_movies_grouped_by_year(all_movies)

with open("data/movies_data.json", 'w') as f:
    json.dump(grouped, f, indent=4)


