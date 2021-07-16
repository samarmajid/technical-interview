#inmporting necessary items 
import requests
from bs4 import BeautifulSoup
import json

#getting data 
r = requests.get('http://books.toscrape.com/')
soup = BeautifulSoup(r.content)

#setting output to an empty list
output = []

#scraping title data 
#finding all the img data since the title is contained in the alt text of the 
#img of the books 
images = soup.find_all('img')
#looping through all images
for image in images:
    #getting the alt text and appending the output 
    output.append((image['alt']))

#finding all the data from the class price_color 
price_colors = soup.find_all("p", class_='price_color')
#looping through the price colors
for price_color in price_colors:
    #appending the output with the string in the class 
    output.append((price_color.string))

#finding all the data from the star-rating class
price_ratings = soup.find_all("p", class_='star-rating')
#looping through each rating
for price_rating in price_ratings:
    #appending the output with the second instance of the class's list 
    output.append((price_rating["class"][1]))

#putting the output in the json file and having the result variable contain this file 
result = json.dumps(output) 
print(result)

#opening json file or creating it if it does not exist 
with open("result.json", "w") as f:
    f.write(result)
