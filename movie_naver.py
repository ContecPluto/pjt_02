import csv
import requests
import json
from pprint import pprint
from decouple import config


CLIENT_ID = config('NAVER_CLIENT_ID')
CLIENT_SECRET = config('NAVER_CLIENT_SECRET')
HEADERS = {'X-Naver-Client-Id':CLIENT_ID, 'X-Naver-Client-Secret': CLIENT_SECRET}
url = 'https://openapi.naver.com/v1/search/movie.json'
result = {}

with open('movie.csv', 'r', newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for read in reader:        
        adress = f'{url}?query={read.get("영화명(국문)")}'
        response = requests.get(adress, headers=HEADERS).json()
        result[read.get('영화명(국문)')] = dict(
            movieCd = read.get('영화 대표코드'),
            link = response.get('items')[0].get('link') if response.get('items')[0].get('link') else '',
            userRating = response.get('items')[0].get('userRating'),
            image = response.get('items')[0].get('image') if response.get('items')[0].get('image') else ''
        )

with open('movie_naver.csv','w', newline='', encoding='utf-8') as f:
    feldnames = ('movieCd','link', 'image', 'userRating' )
    writer = csv.DictWriter(f, fieldnames=feldnames)
    writer.writeheader()    
    for write_movie in result.values():
        writer.writerow(write_movie)








