import requests
import json

url = 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json'
response = requests.get(url)
if response.status_code == 200:
    print("ok")

heroes_list = ['Hulk', 'Captain America', 'Thanos']
intelligence_dict = {'Hulk': 0, 'Captain America': 0, 'Thanos': 0}

heroes = response.json()
for hero in heroes:
    if hero['name'] in heroes_list:
        intelligence_dict[hero['name']] = hero['powerstats']['intelligence']
print(intelligence_dict)
print(f'{max(intelligence_dict, key=intelligence_dict.get)} самый умный супергерой!')


