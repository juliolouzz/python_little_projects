from bs4 import BeautifulSoup
# Documentation - https://www.crummy.com/software/BeautifulSoup/bs4/doc/index.html#module-bs4
# import lxml <--- can use lxml instead html.parser
import requests

response = requests.get("https://news.ycombinator.com/")
yc_web_page = response.text

# soup = BeautifulSoup(yc_web_page, "html.parser")
# article_tag = soup.find(name="span", class_="titleline")
# article_text = article_tag.get_text()
# article_link = article_tag.find(name="a").get("href")
# article_upvote = soup.find(name="span", class_="score").get_text()
# print(article_tag)
# print(article_text)
# print(article_link)
# print(article_upvote)

# to get all from the page with a for loop

soup = BeautifulSoup(response.text,'html.parser')
articles = soup.select(selector=".titleline")

article_texts = []
article_links = []

for article in articles:
    single_line = article.select_one(selector='a')
    link = single_line.get('href')
    text = single_line.text
    article_texts.append(text)
    article_links.append(link)

article_upvotes = [int(score.text.split()[0]) for score in soup.select(selector=".score")]

max_pos = article_upvotes.index(max(article_upvotes))

print(article_texts[max_pos])
print(article_links[max_pos])
print(article_upvotes[max_pos])







# with open("website.html") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
# print(soup.title)
