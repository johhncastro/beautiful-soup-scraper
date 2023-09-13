from bs4 import BeautifulSoup
import requests

website = "https://subslikescript.com/movie/Harry_Potter_and_the_Prisoner_of_Azkaban-304141"
result = requests.get(website)
content = result.text

soup = BeautifulSoup(content, 'lxml')
# print(soup.prettify())

# this is grabs the parent div of all the content to scrape
parentDiv = soup.find('article', class_='main-article')

# this will get title of the transcript
title = parentDiv.find('h1').get_text()
# print(title)

transcript = parentDiv.find('div', class_='full-script').get_text(strip=True, separator=' ')

# print(transcript)

with open(f'{title}.txt', 'w') as file:
    file.write("Write Successful:  " + transcript)
