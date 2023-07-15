## [WEB-06P1] Project - Finding a job at Netflix ##

# Downloading the source code #
import requests
req = requests.get('https://jobs.lever.co/netflix')
req.request.headers
html_str = req.text
len(html_str)

# Parsing the source code #
from bs4 import BeautifulSoup
soup = BeautifulSoup(html_str, 'html.parser')

# Link #
link = soup.find_all('a', 'posting-title')
len(link)
link[0]
link = [l['href'] for l in link]
link[:5]
link[-5:]

# Job #
job = soup.find_all('h5', {'data-qa': 'posting-name'})
len(job)
job = soup.find_all('h5')
len(job)
job[0]
job = [j.text for j in job]
job[:5]
job[-5:]

# Location #
location = soup.find_all('span', 'sort-by-location posting-category small-category-label')
len(location)
location = soup.find_all('span', 'sort-by-location')
len(location)
import re
location = soup.find_all('span', re.compile('location'))
len(location)
location = [l.text for l in location]
location[:5]

# Team #
team = soup.find_all('span', re.compile('team'))
len(team)
team = [t.text for t in team]
team[:5]
team = [t.split(' – ') for t in team]
team[:5]
division = [t[0] for t in team]
division[:5]
dept = [t[1] for t in team]
dept[:5]

# Packing #
N = len(link)
rows = [[link[i], job[i], location[i], division[i], dept[i]] for i in range(N)]
rows[:5]
header = ['link', 'job', 'location', 'division', 'dept']
data = [header] + rows
data[:5]

# Writing to a CSV file (edit path) #
import csv
with open('netflix.csv', mode='w', newline='', encoding='utf-8') as conn:
    writer = csv.writer(conn, delimiter=',')
    writer.writerows(data)
