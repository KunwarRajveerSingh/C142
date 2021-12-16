import csv

with open('movies.csv',encoding='utf-8') as f:
    reader = csv.reader(f)
    data = list(reader)
    all_movies = data[1:]
    headers = data[0]
headers.append('poster_link')

with open('final.csv','a+') as f:
    writer = csv.writer(f)
    writer.writerow(headers)

with open('movie_links.csv',encoding='utf-8')as f:
    reader = csv.reader(f)
    data = list(reader)
    all_movie_link = data[1:]

for movieitem in all_movies:
    poster_found = any(movieitem[8] in movie_link_items for movie_link_items in all_movie_link)
    if poster_found:
        for movie_link_items in all_movie_link:
            if movieitem[8] == movie_link_items[0]:
                movieitem.append(movie_link_items[1])
                if (len(movieitem) == 28):
                    with open("final.csv",'a+') as f:
                        writer = csv.writer(f)
                        writer.writerow(movieitem)
                    

