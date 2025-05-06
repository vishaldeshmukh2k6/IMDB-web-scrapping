from tasks.task_1 import scrape_top_list

print(scrape_top_list())



from tasks.task_1 import scrape_top_list
from tasks.task_2 import get_all_top_movies_grouped_by_year

movies = scrape_top_list() 
grouped = get_all_top_movies_grouped_by_year(movies) 

print(grouped)