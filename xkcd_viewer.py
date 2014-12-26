import requests
import random

from PIL import Image
from bs4 import BeautifulSoup
from StringIO import StringIO


# Randomly get a title from the xkcd archive
def get_title():

    link = 'http://www.xkcd.org/archive/'
    r = requests.get(link)
    soup = BeautifulSoup(r.content)
    titles = []

    for name in soup.find('div', id='middleContainer').find_all('a'):
        titles.append('http://www.xkcd.org{}'.format(name.get('href')))

    title = random.choice(titles)

    return title


# Download and view the image
def show_image():

    comic_page = requests.get(get_title())
    comic_soup = BeautifulSoup(comic_page.content)

    link = comic_soup.find('div', id='comic').find('img').get('src')
    print comic_soup.find('title').string.lstrip('xkcd: ')

    res_img = requests.get(link)
    image = Image.open(StringIO(res_img.content))
    image.show()

    # the next line to save the retrieved the image
    # image.save(comic_soup.find('title').string.lstrip('xkcd: '), 'PNG')

if __name__ == "__main__":
    show_image()
