import json
from tasks.task_1 import scrape_top_list

def group_by_decade(movies):
    result = {}
    for m in movies:
        year = m.get("year")
        if year and year.isdigit():
            year = int(year)
            decade = (year // 10) * 10
            decade_str = str(decade)
            if decade_str not in result:
                result[decade_str] = [] 
            result[decade_str].append(m)
    return result

all_movies = scrape_top_list()
decade = group_by_decade(all_movies)

with open("data/task_3.json", "w+") as f:
    json.dump(decade, f , indent=4)