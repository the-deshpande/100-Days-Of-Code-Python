from bs4 import BeautifulSoup
import requests

# with open('website.html') as file:
#     content = file.read()
#
# soup = BeautifulSoup(content, 'html.parser')
#
# for tags in soup.find_all("a"):
#     print(tags.get('href'))

response = requests.get("https://news.ycombinator.com/")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

links = soup.select('.titleline>a')
scores = soup.select('.score')
articles = [(link.text, link.get('href'), int(score.text.split()[0])) for link, score in zip(links, scores)]

articles.sort(key=lambda x: x[-1], reverse=True)
print(*articles[0])
