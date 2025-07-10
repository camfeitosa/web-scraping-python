import requests
from bs4 import BeautifulSoup
import shutil
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

url_base = "http://books.toscrape.com/"
page = requests.get(url_base)

data = BeautifulSoup(page.text, "html.parser")

all_images = data.find_all("img", class_="thumbnail")

i = 0
# dowload images
for img in all_images:
  i += 1
  url_ext = img.attrs['src']
  full_url = url_base + url_ext
  
  r = requests.get(full_url, stream=True) #Get request on full_url

  if r.status_code == 200:
    with open(f"book/images/book-{i}.jpg", 'wb') as f: 
        r.raw.decode_content = True
        shutil.copyfileobj(r.raw, f)
        
  # show images   
  img = mpimg.imread(f'book/images/book-{i}.jpg')
  imgplot = plt.imshow(img)
  plt.show()
  