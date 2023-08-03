## [WEB-06P3] Project - Best restaurants in Barcelona according to TripAdvisor [2] ##

# Packages #
import requests, re
from bs4 import BeautifulSoup

# Headers #
headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) \
	AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'}

# Scraping BelleBuon's page #
req = requests.get('https://www.tripadvisor.com/Restaurant_Review-g187497-d4049034', headers=headers)
soup = BeautifulSoup(req.text, 'html.parser')
claimed = soup.find('span', re.compile('ui_icon verified-checkmark')) != None
claimed
# travelers = soup.find('span', re.compile('ui_icon travelers-choice-badge')) != None
travelers = soup.find('span', text=re.compile("Travelers' Choice")) != None
travelers
photos = soup.find('span', 'details').text
photos = int(re.sub('[() ,a-zA-Z]', '', photos))
photos
thefork = soup.find('div', text='Reserve a table')
thefork = thefork != None
thefork
justeat = soup.find('div', text='Get food delivered')
justeat = justeat != None
justeat
cuisines = soup.find('div', text='CUISINES')
cuisines
if cuisines: cuisines = cuisines.find_next().text
cuisines
diets = soup.find('div', text='Special Diets')
if diets: diets = diets.find_next().text
diets
meals = soup.find('div', text='Meals')
if meals: meals = meals.find_next().text
meals
features = soup.find('div', text='FEATURES')
if features: features = features.find_next().text
features
neigh = soup.find('span', re.compile('ui_icon neighborhoods'))
if neigh: neigh = neigh.find_next('div').text
neigh
excellent = soup.find('div', {'data-value': '5'})
excellent = excellent.find('span', re.compile('row_num'))
excellent
excellent = int(excellent.text.replace(',', ''))
excellent
verygood = int(soup.find('div', {'data-value': '4'}).find('span', 'row_num').text.replace(',', ''))
average = int(soup.find('div', {'data-value': '3'}).find('span', 'row_num').text.replace(',', ''))
poor = int(soup.find('div', {'data-value': '2'}).find('span', 'row_num').text.replace(',', ''))
terrible = int(soup.find('div', {'data-value': '1'}).find('span', 'row_num').text.replace(',', ''))
revEnglish = soup.find('div', {'data-value': 'en'}).find('span', 'count')
revEnglish
if revEnglish: revEnglish = int(re.sub('[(),]', '', revEnglish.text))
else: revEnglish = 0
revSpanish = soup.find('div', {'data-value': 'es'}).find('span', 'count')
if revSpanish: revSpanish = int(re.sub('[(),]', '', revSpanish.text))
else: revSpanish = 0

# Reading previous data (edit path) #
import csv
with open('trip1.csv', 'r') as conn:
	reader = csv.reader(conn)
	data1 = list(reader)

# Scraping function #
def trip2(i):
	url = 'https://www.tripadvisor.com/Restaurant_Review' + '-g187497-' + data1[i][2]
	html_str = requests.get(url, headers=headers).text
	soup = BeautifulSoup(html_str)
	claimed = soup.find('span', re.compile('ui_icon verified-checkmark')) != None
	travelers = soup.find('span', text=re.compile("Travelers' Choice")) != None
	photos = soup.find('span', 'details').text
	photos = int(re.sub('[() ,a-zA-Z]', '', photos))
	thefork = soup.find('div', text='Reserve a table') != None
	justeat = soup.find('div', text='Get food delivered') != None
	cuisines =  soup.find('div', text='CUISINES')
	if cuisines: cuisines = cuisines.find_next().text
	diets = soup.find('div', text='Special Diets')
	if diets: diets = diets.find_next().text
	meals = soup.find('div', text='Meals')
	if meals: meals = meals.find_next().text
	features = soup.find('div', text='FEATURES')
	if features: features = features.find_next().text
	neigh = soup.find('span', re.compile('ui_icon neighborhoods'))
	if neigh: neigh = neigh.find_next('div').text
	excellent = int(soup.find('div', {'data-value': '5'}).find('span', 'row_num').text.replace(',', ''))
	verygood = int(soup.find('div', {'data-value': '4'}).find('span', 'row_num').text.replace(',', ''))
	average = int(soup.find('div', {'data-value': '3'}).find('span', 'row_num').text.replace(',', ''))
	poor = int(soup.find('div', {'data-value': '2'}).find('span', 'row_num').text.replace(',', ''))
	terrible = int(soup.find('div', {'data-value': '1'}).find('span', 'row_num').text.replace(',', ''))
	revEnglish = soup.find('div', {'data-value': 'en'}).find('span', 'count')
	if revEnglish: revEnglish = int(re.sub('[(),]', '', revEnglish.text))
	else: revEnglish = 0
	revSpanish = soup.find('div', {'data-value': 'es'}).find('span', 'count')
	if revSpanish: revSpanish = int(re.sub('[(),]', '', revSpanish.text))
	else: revSpanish = 0
	return [claimed, travelers, photos, thefork, justeat, cuisines, diets, meals, features, neigh,
		excellent, verygood, average, poor, terrible, revEnglish, revSpanish]

# Scraping the new data #
data2 = [['claimed', 'travelers', 'photos', 'thefork', 'justeat', 'cuisines', 'diets', 'meals', 'features',
	'neigh', 'excellent', 'verygood', 'average', 'poor', 'terrible', 'revEnglish', 'revSpanish']]
for i in range(1, 451):
	data2 = data2 + [trip2(i)]
	if i%25 == 0: print('Page ' + str(i) + ' processed')

# Joining the two data sets #
data = [data1[i] + data2[i] for i in range(451)]

# Writing to CSV file (edit path) #
with open('trip.csv', 'w', newline='', encoding='utf-8') as conn:
	writer = csv.writer(conn, delimiter=',')
	writer.writerows(data)
