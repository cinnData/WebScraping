## [WEB-07P2] Project - Get a look from Zalando ##

# Starting the browser #
from selenium import webdriver
browser = webdriver.Chrome()
browser.get('https://www.zalando.es/consigue-el-look-mujer')
browser.maximize_window()

# Accepting cookies #
import time
time.sleep(15)
from selenium.webdriver.common.by import By
button = browser.find_elements(By.ID, 'uc-btn-accept-banner')
if len(button) == 1: button[0].click()
time.sleep(15)

# Scrolling down to bottom #
for j in range(15):
	browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
	pic_count = browser.page_source.count('imwidth=600')
	time.sleep(15)
	print('Scrolled ' + str(j+1) + ', ' + str(pic_count) + ' pics')
	
# Parsing HTML code with Beautiful Soup #
from bs4 import BeautifulSoup
soup = BeautifulSoup(browser.page_source, 'html.parser')

# Scraping data #
import re
block = soup.find_all('div', '_5qdMrS v9kdwN w8MdNG VHXqc_ mzdoCd')
len(block)
block = [b for b in block if not b.find('span', text='Curated by Zalando')]
len(block)
block = [b for b in block if b.find('span', text='Seguir')]
len(block)
img_link = [b.find('img', 'KxHAYs lystZ1 FxZV-M _2Pvyxl JT3_zV EKabf7 mo6ZnF _1RurXL mo6ZnF _7ZONEy')['src'] for b in block]
img_link[:5]
outfit_link = [b.find('a', href=re.compile('/outfits.+'))['href'] for b in block]
outfit_link = ['https://www.zalando.es' + o for o in outfit_link]
outfit_link[:5]
creator_area = [b.find_all('a', href=re.compile('/creator.+'))[-1] for b in block]   ## Fix this ##
creator_link = ['https://www.zalando.es' + c['href'] for c in creator_area]
creator_link[:5]
creator = [c.text for c in creator_area]
creator[:5]

# Closing connection #
browser.close()

# Packing #
N = len(block)
header = ['img_link', 'outfit_link', 'creator_link', 'creator']
rows = [[img_link[i], outfit_link[i], creator_link[i], creator[i]] for i in range(N)]
data = [header] + rows

# Writing to a CSV file (edit path) #
import csv
with open('zalando.csv', mode='w', newline='', encoding='utf-8') as conn:
    writer = csv.writer(conn, delimiter=',')
    writer.writerows(data)
