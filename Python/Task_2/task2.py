import requests
from bs4 import BeautifulSoup
import json


r = requests.get('http://books.toscrape.com/')

soup = BeautifulSoup(r.content)


output = []
images = soup.find_all('img')
for image in images:
    output.append((image['alt']))


price_colors = soup.find_all("p", class_='price_color')
for price_color in price_colors:
    output.append((price_color.string))


price_ratings = soup.find_all("p", class_='star-rating')
for price_rating in price_ratings:
    output.append((price_rating["class"][1]))

result = json.dumps(output) 
print(result)

with open("result.json", "w") as f:
    f.write(result)
