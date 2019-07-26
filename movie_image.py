import csv
import requests
from pprint import pprint

result = {}

with open('movie_naver.csv', 'r', newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for read in reader:
        with open(f'images/{read.get("movieCd")}.jpg','wb') as f:
            response = requests.get(read.get('image')).content
            f.write(response)

