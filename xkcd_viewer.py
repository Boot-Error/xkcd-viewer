import requests
import Image
from StringIO import StringIO
import random
from bs4 import BeautifulSoup

# randomly get the title from the archieves
def get_titles():

	link = 'http://www.xkcd.org/archive/'
	r = requests.get(link)
	soup = BeautifulSoup(r.content)
	titles = []

	for name in soup.find('div', id='middleContainer').find_all('a'):
		titles.append('http://www.xkcd.org'+name.get('href'))

	return titles

#downloads and views the image
def show_random():

	title = random.choice(get_titles())
	comic_page = requests.get(title)
	comic_soup = BeautifulSoup(comic_page.content)

	link = comic_soup.find('div', id='comic').find('img').get('src')
	print comic_soup.find('title').string.lstrip('xkcd: ')

	res_img = requests.get(link)
	image = Image.open(StringIO(res_img.content))
	image.show()
	
	# the next line to save the retrieved the image
	# image.save(comic_soup.find('title').string.lstrip('xkcd: '), 'PNG')

if __name__ == "__main__":
	show_random()
