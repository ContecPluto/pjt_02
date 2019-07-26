import csv
import requests
from decouple import config
from pprint import pprint
​
CLIENT_ID = config('NAVER_CLIENT_ID')
CLIENT_SECRET = config('NAVER_CLIENT_SECRET')
HEADERS = {'X-NAVER-Client-Id' : CLIENT_ID, 'X-NAVER-Client-Secret' : CLIENT_SECRET}
​
# 1 csv.DictReader() _ boxoffice에서 영화코드 읽어오기
with open('movie.csv', newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f) # 읽어올 파일만 입력=>reader에 파일이 들어있음
    movie_cd_nm = {}
    for row in reader:
        # code = row['영화 대표코드']
        # name = row['영화명(국문)']
        movie_cd_nm.update({row['영화 대표코드'] : row['영화명(국문)']})
​
result = {}
# 요청하기
for movie_cd, movie_nm in movie_cd_nm.items():
    url = 'https://openapi.naver.com/v1/search/movie.json'
    address = f'{url}?query={movie_nm}'
    response = requests.get(address, headers=HEADERS).json()
    api_data = response.get('items')[0]
​
# 필요한 정보 : 영진위 영화 대표코드(movieCd), 하이퍼텍스트 link(link), 영화썸네일 이미지의 url(없으면 저장x)(image), 유저 평점(userRating)
    result[movie_nm] = {
            '영진위 영화 대표코드': movie_cd,
            '하이퍼텍스트 link': api_data.get('link'),
            '영화 썸네일 이미지의 URL': api_data.get('image'),
            '유저 평점': api_data.get('userRating')
        }
​
#pprint(result)
with open('movie_naver.csv', 'w', encoding='utf-8', newline='') as f:
    fieldnames = ('영진위 영화 대표코드', '하이퍼텍스트 link', '영화 썸네일 이미지의 URL', '유저 평점')
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for value in result.values():
        print(value)
        writer.writerow(value)