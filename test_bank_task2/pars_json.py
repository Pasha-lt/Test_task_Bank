import json
import requests
from pprint import pprint
from requests_html import HTMLSession


session = HTMLSession()

url = session.get('https://data.gov.ua/dataset/41d166e9-d1b8-4a54-8e0a-363b02e2f11d/')

spisok_link = url.html.xpath('//*[@id="dataset-resources"]/ul//a//@href')

main_url = []

for i in spisok_link:
    if i.startswith('https') and not i.endswith('shema.json'):
        main_url.append(i)


url = main_url[0]
response = requests.get(url)

total_save = response.json()


exit()  # Первый вариант его отбросил так как несмог довести.

from pprint import pprint

import requests
import json

req = requests.get('https://data.gov.ua/dataset/ab09ed00-4f51-4f6c-a2f7-1b2fb118be0f/datapackage')


with open("1.json", "wb") as code:
    code.write(req.content)


file_open = open('1.json', mode='r', encoding='Latin-1')
json_data = json.load(file_open)



list_url = []  # Список где мы будем хранить ссылки на json с документами.
for user in json_data['resources']:
    if 'shema' not in str(user['path']):
        # pprint(user['path'])
        list_url.append(user['path'])


for i in list_url:
    urll = str(i)
    req2 = requests.get(urll)
    total_save = req2

    print(type(total_save))



    # file_name = str(i)[-8:]
    # with open(file_name, "wb") as code:
    #     code.write(req2.content)