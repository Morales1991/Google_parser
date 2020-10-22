import requests
import json

from bs4 import BeautifulSoup as BS


USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0'
headers = {'user-agent' : USER_AGENT}
URL =  'https://www.google.com/search'
params = {'q':'scrapy'}

responce = requests.get(URL, headers=headers, params=params)

if responce.status_code == 200:
    soup = BS(responce.content, 'html.parser')
    results = []
    for g in soup.find_all('div', class_='g'):
        anchors = g.find_all('a')
        if anchors:
            link = anchors[0]['href']
            title = g.find('h3').text
            Description = g.select_one('div > div:not([class]) > span').text
        
            item = {
                'Name': title,
                'Url': link,
                'Description': Description
            }
            
            results.append(item)  

else:
    results.append({'error': f'received invalid status code ({response.status_code})'})

with open('personal.json', 'w') as json_file:
    json.dump(results, json_file)

