## [WEB-07P1] Project - Wise job postings ##

# An attempt with Requests #
import requests
html_str = requests.get('https://www.transferwise.jobs/search').text
'Senior Product Designer' in html_str

# Starting the browser #
from selenium import webdriver
browser = webdriver.Chrome()
browser.get('https://www.transferwise.jobs/search')

# Extracting HTML elements with selenium #
from selenium.webdriver.common.by import By
browser.find_element(By.ID, 'twcc__accept-button')
browser.find_elements(By.ID, 'twcc__accept-button')
browser.find_elements(By.CSS_SELECTOR, 'button.twcc__button')
browser.find_elements(By.XPATH, '//button[@id="twcc__accept-button"]')

# Accepting cookies #
button = browser.find_elements(By.ID, 'twcc__accept-button')
if len(button) == 1: button[0].click()

# Expanding the page #
browser.find_elements(By.CSS_SELECTOR, 'button.o-btn.o-btn--ghost')
browser.find_elements(By.XPATH, '//button[@class="o-btn o-btn--ghost"]')
'Show more roles' in browser.page_source
import time
time.sleep(5)
while 'Show more roles' in browser.page_source:
    button = browser.find_element(By.XPATH, '//button[@class="o-btn o-btn--ghost"]')
    button.click()
    print('Page expanded')
    time.sleep(5)
'Show more roles' in browser.page_source

# Scraping with Beautiful Soup #
from bs4 import BeautifulSoup
soup = BeautifulSoup(browser.page_source, 'html.parser')
block = soup.find_all('a', 'c-card')
len(block)
link = [b['href'] for b in block]
len(link)
link[:5]
title = [t.find('span', 'o-btn__label').text for t in block]
len(title)
title[:5]
team = [t.find_all('span', 'o-tag__label')[0].text for t in block]
len(team)
team[:5]
import re
team = [re.sub('(^\s+)|(\s+$)', '', t) for t in team]
team[:5]
location = [t.find_all('span', 'o-tag__label')[1].text for t in block]
len(location)
location[:5]
location = [re.sub('(^\s+)|(\s+$)', '', l) for l in location]
location[:5]

# The same with with Selenium #
block = browser.find_elements(By.CSS_SELECTOR, 'a.c-card')
link = [b.get_attribute('href') for b in block]
title = [b.find_element(By.CSS_SELECTOR, 'span.o-btn__label').text for b in block]
team = [b.find_elements(By.CSS_SELECTOR, 'span.o-tag__label')[0].text for b in block]
team = [re.sub('\n|\t', '', t) for t in team]
location = [b.find_elements(By.CSS_SELECTOR, 'span.o-tag__label')[1].text for b in block]
location = [re.sub('\n|\t', '', l) for l in location]

# Closing connection #
browser.close()

# Packing #
header = ['link', 'title', 'team', 'location']
rows = [[link[i], title[i], team[i], location[i]] for i in range(len(link))]
data = [header] + rows

# Writing to a CSV file (edit path) #
import csv
with open('wise.csv', mode='w', newline='', encoding='utf-8') as conn:
    writer = csv.writer(conn, delimiter=',')
    writer.writerows(data)
