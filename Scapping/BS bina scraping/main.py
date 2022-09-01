"""
Scrapes newest house anouncements from 
bina.az web site and prints them.
"""


import requests as reqs
from bs4 import BeautifulSoup


URL = "https://bina.az/"

content = reqs.get(URL)
soup = BeautifulSoup(content.text, 'html.parser')
items_container = soup.find('div', class_='items_container')
list_items = items_container.findChildren('div', class_='items_list')[0]
list_items = list_items.find_all('div', class_='items-i')
def extracter(items):
	if not items:
		raise ValueError("'items' is empty")

	res = []

	for item in items:
		u = item.findChild('a', class_='item_link', href=True)['href']
		card_params = item.find_all('div', class_='card_params')
		for i in card_params:
			price = int((i.find('span', class_='price-val').text).replace(' ', ''))
			location = i.find('div', class_='location').text
			when = i.find('div', class_='city_when').text

			# print(price, location, when, u, end='\n\n')
			res.append({'price':price, 'location':location, 'when':when, 'url': URL[:-1]+u})
	return res


data = extracter(list(list_items))
for d in data:
	print(d, '\n')