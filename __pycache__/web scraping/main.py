# If you want to scraping a website:
# 1. Use the API 
# 2. HTML Web scrapingusing some tool like bs4

# Step 0:Install all the requirements
# pip install requests
# pip install html5lib
# pip install bs4


import requests
from bs4 import BeautifulSoup
url="https://codewithharry.com"


# Step 1:Get the HTML
r = requests.get(url)
htmlcontent = r.content
print(htmlcontent)
# Step 2:Parse the HTML
soup=BeautifulSoup(htmlcontent, 'html.parser')
print(soup)
# Step 3:HTML Tree traversal 