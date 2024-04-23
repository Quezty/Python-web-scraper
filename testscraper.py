from bs4 import BeautifulSoup
import requests

page = requests.get('https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/')
soup = BeautifulSoup(page.content, 'html.parser')
title = soup.title.text
body = soup.body
head = soup.head
first_h1 = soup.select('h1')[0].text
seventh_p = soup.select('p')[6].text
print(first_h1)
