import requests
from bs4 import BeautifulSoup
import json

url = 'https://www.audiosparx.com/sa/display/displayby.cfm/target.subject'
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

# Find all the theme divs
theme_div = soup.find('div', {'id': 'subBodyContentDiv'}).find_all('a', {'class': 'lmfont11 alinkInvert hoverBlockA1'})

# Create dictionary with themes and links to theme
theme_dict = dict()
l = list()
for div in theme_div:
    l.append(div.text)
print(l)

for div in theme_div:
    print(div.text)
    theme_link = div.get('href').split('subject.')[0]
    theme_response = requests.get('https://www.audiosparx.com' + theme_link + 'startrow.1')
    theme_soup = BeautifulSoup(theme_response.content, 'html.parser')
    theme_td = theme_soup.find('div', {'id': 'masterEncapsDivId'}).find_all('table')[1].find_all('td')[1].text
    num_tracks = int(theme_td.split(' ')[0].replace('(', ''))
    theme_track_page_links = list()
    for i in range(1, num_tracks, 50):
        temp_link_var = f'https://www.audiosparx.com{theme_link}startrow.{i}'
        theme_track_page_links.append(temp_link_var)
    theme_dict[div.text] = theme_track_page_links

pretty_dict = json.dumps(theme_dict, indent=4)

with open("data/theme_links.json", "a") as outfile:
    outfile.write(pretty_dict)

print(pretty_dict)
