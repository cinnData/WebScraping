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
block = soup.find_all('div', 'DT5BTM v9kdwN w8MdNG VHXqc_ _8O8c-d')
len(block)
block = [b for b in block if not b.find('span', text='Patrocinado')]
len(block)
img_link = [b.find('img', '_0Qm8W1')['src'] for b in block]
outfit_link = [b.find('a', href=re.compile('/outfits.+'))['href'] for b in block]
outfit_link = ['https://www.zalando.es' + o for o in outfit_link]
creator_area = [b.find_all('a', href=re.compile('/creator.+'))[-1] for b in block] 
creator_link = ['https://www.zalando.es' + c['href'] for c in creator_area]
creator = [c.text for c in creator_area]
no_looks = [b.find('span', text=re.compile('Looks')).text for b in block]
no_looks = [int(re.sub(' .+', '', n)) for n in no_looks]

# Closing connection #
browser.close()

# Packing #
N = len(block)
header = ['img_link', 'outfit_link', 'creator_link', 'creator', 'no_looks']
rows = [[img_link[i], outfit_link[i], creator_link[i], creator[i], no_looks[i]] for i in range(N)]
data = [header] + rows

# Writing to a CSV file (edit path) #
import csv
with open('zalando.csv', mode='w', newline='', encoding='utf-8') as conn:
    writer = csv.writer(conn, delimiter=',')
    writer.writerows(data)

# Closing connection #
browser.close()
