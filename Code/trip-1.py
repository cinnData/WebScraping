## Example - Best restaurants in Barcelona according to TripAdvisor [1] ##

# Spoofing #
import requests
# req = requests.get('https://www.tripadvisor.com/Restaurants-g187497')
headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) \
	AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'}
req = requests.get('https://www.tripadvisor.com/Restaurants-g187497', headers=headers)
html_str = req.text

# Scraping the first page #
from bs4 import BeautifulSoup
soup = BeautifulSoup(html_str, 'html.parser')
import re
block = soup.find_all('div', {'data-test': re.compile('[0-9]+_list_item')})
len(block)
blockname = [b.find_all('a')[1] for b in block]
len(blockname)
blockname[0]
blockname[0].text
rank = [int(re.sub('\..+', '', b.text)) for b in blockname]
rank[:5]
name = [re.sub('[0-9]+\. ', '', b.text) for b in blockname]
name[:5]
link = [b['href'] for b in blockname]
link[:5]
id = [re.sub('/Restaurant_Review-g187497-|-Reviews-.+', '', l) for l in link]
id[:5]
bubble = [b.find('svg', {'aria-label': True})['aria-label'] for b in block]
bubble[:5]
bubble = [float(b.replace('of 5 bubbles', '')) for b in bubble]
reviewCount = [b.find('span', 'IiChw').text for b in block]
reviewCount[:5]
reviewCount = [int(re.sub(' reviews|,', '', r)) for r in reviewCount]
reviewCount[:5]
priceRange = [b.find(text=re.compile('\$')) for b in block]
priceRange[:5]
data = [[rank[i], name[i], id[i], bubble[i], reviewCount[i], priceRange[i]] for i in range(30)]
data[:5]

# Scraping function #
def trip1(i):
	url = 'https://www.tripadvisor.com/Restaurants-g187497-oa' + str(30*i)
	html_str = requests.get(url, headers=headers).text
	soup = BeautifulSoup(html_str, 'html.parser')
	block = soup.find_all('div', {'data-test': re.compile('[0-9]+_list_item')})
	blockname = [b.find_all('a')[1] for b in block]
	rank = [int(re.sub('\..+', '', b.text)) for b in blockname]
	name = [re.sub('[0-9]+\. ', '', b.text) for b in blockname]
	link = [b['href'] for b in blockname]
	id = [re.sub('/Restaurant_Review-g187497-|-Reviews-.+', '', l) for l in link]
	bubble = [b.find('svg', {'aria-label': True})['aria-label'] for b in block]
	bubble = [float(b.replace('of 5 bubbles', '')) for b in bubble]
	reviewCount = [b.find('span', 'IiChw').text for b in block]
	reviewCount = [int(re.sub(' reviews|,', '', r)) for r in reviewCount]
	priceRange = [b.find(text=re.compile('\$')) for b in block]
	data = [[rank[i], name[i], id[i], bubble[i], reviewCount[i], priceRange[i]] for i in range(30)]
	return data

# Scraping the new data #
data1 = [['rank', 'name', 'id', 'bubble', 'reviewCount', 'priceRange']]
for i in range(15):
	data1 = data1 + trip1(i)
	print('Page ' + str(i + 1) + ' processed')

# Writing to a CSV file (edit path) #
import csv
with open('trip1.csv', 'w', newline='') as conn:
	writer = csv.writer(conn, delimiter=',')
	writer.writerows(data1)
