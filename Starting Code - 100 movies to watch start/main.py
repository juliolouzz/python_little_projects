import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
webpage = response.text

soup = BeautifulSoup(webpage, "html.parser")
all_movies = soup.find_all(name="h3", class_="title")

movie_titles = [movie.getText() for movie in all_movies] # make a list with just the text of all_movies
movies = movie_titles[::-1] # reverse the list to start form 1 not from 100

with open("movies.txt", mode="w") as file:
    for movie in movies:
        file.write(f"{movie}\n")


# title = []
# for title in all_movies:
#     string_line = title.get_text()
#     titles.append(string_line)
#
# with open("movies.txt", "w") as file:
#     for x in range(len(movie_titles)-1, -1, -1): #range(start, stop, step), to go until index 0, stop need to be -1
#         file.write(str(titles[x] + "\n"))
