import requests # obtem o html da página
from bs4 import BeautifulSoup 

page = requests.get('https://quotes.toscrape.com/')

page_data = BeautifulSoup(page.text, 'html.parser') # html to python obj

print(page_data.prettify())

# filtra os elementos com essas caracteristicas -> div com a classe quote
all_quotes = page_data.find_all('div', class_="quote") # class -> class_ palavra reservada python

for div in all_quotes:
  text = div.find('span', class_="text").text
  print(text)