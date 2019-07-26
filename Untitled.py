import requests
from decouple import config
import csv
from pprint import pprint

# .env에 key값, secret값을 저장하고 요청에 활용합니다.
CLIENT_ID = config('NAVER_CLIENT_ID')
CLIENT_SECRET = config('NAVER_CLIENT_SECRET')
HEADERS = {'X-Naver-Client-Id': CLIENT_ID, 'X-Naver-Client-Secret': CLIENT_SECRET}
url = 'https://openapi.naver.com/v1/search/movie.json'
read_dict = {}

# movie.csv파일을 읽어, 그 안의 영화명과 영화 대표코드를 저장합니다.
with open('movie.csv', newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for read in reader:
        if read.get('영화명(국문)'):
            movieNm = read.get('영화명(국문)')
            movieCd = read.get('영화 대표코드')
            # 저장된 영화명으로 네이버 영화에 검색을 요청합니다.
            address = f'{url}?query={movieNm}'
            response = requests.get(address, headers=HEADERS).json()
            movie = response['items'][0]
            # 받은 정보 중 필요한 요소를 뽑아 딕셔너리로 저장합니다.
            read_dict[movieNm] = {
                '영진위 영화 대표코드': movieCd,
                '하이퍼텍스트 link': movie.get('link'),
                '유저 평점': movie.get('userRating'),
            }
            # image url이 없는 경우에는 ''로 저장합니다.
            read_dict[movieNm]['영화 썸네일 이미지의 URL'] = movie.get('image') if movie.get('image') else ''

# movie_naver.csv를 만들어, 구성된 딕셔너리를 파일에 기록합니다. 
with open('movie_naver.csv', 'w', newline='', encoding='utf-8') as f:
        fieldnames = ['영진위 영화 대표코드', '하이퍼텍스트 link', '영화 썸네일 이미지의 URL', '유저 평점']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for value in read_dict.values():
            writer.writerow(value)
