import requests # obtem o html da página
from bs4 import BeautifulSoup 

page = requests.get('https://quotes.toscrape.com/')
page_data = BeautifulSoup(page.text, 'html.parser') # html to python obj

print(page_data.prettify())

all_quotes = page_data.find_all('div', class_="quote")

def filter(classe_css):
  return classe_css is not None and len(classe_css) == 4 

# buscando de acordo com método
all_quotes = page_data.find_all('div', class_=filter)

for div in all_quotes:
  print(div['class'])