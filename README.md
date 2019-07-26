# Project_02_-_파이썬 데이터 수집 2

## 1.프로젝트 설명

영화의 정보가 담긴 movie.csv를 이용하는 프로젝트입니다. csv에 기록된 `영화명(국문)`을 이용하여 검색하여 추가적인 정보를 movie_naver.csv에 저장하여 이를 이용하여 images폴더에 이미지를 저장하는 프로젝트입니다.

## 2.movie_naver.py

### 2.1 movie_naver.py

movie.csv의 정보중 `영화명(국문)` `영화 대표코드` 를 저장하고 `영화명(국문)` 을 통해 네이버를 통해 추가적인 정보인  `하이퍼텍스트 link`, `영화 썸네일 이미지의 URL`,` 유저 평점 ` 의 세가지의 추가적인 정보를 movie_naver.csv에 저장하였습니다.

![movie_naver](/uploads/5c38cdd5d0769a326b31f0b3d4841818/movie_naver.PNG)

### 2.2 시행착오

```python
adress = f'{url}?query={read.get('영화명(국문)')}'
```

adress를 작성하는 코드를 작성하였으나 지속적인 오류가 발생하는것을 확인하였습니다.



```python
adress = f'{url}?query={read.get("영화명(국문)")}'
```

''(작은 따음표) 안에 ''(작은 따음표)를 사용하며 생긴 오류로 ""(큰 따음표)를 사용하며 오류를 처리하였습니다.



```python
adress = f'{url}?query={read.get("영화명(국문)")}'

response = requests.get(adress, headers=HEADERS).json()
```

headers의 사용에 몇가지 시행착오를 겼엇습니다. 

json뒤의 괄호()를 붙이지않아 response의 값이 HTTP 상태 코드인 200만을 응답으로 주는것을 확인했습니다.



## 2.3 핵심

```python
CLIENT_ID = config('NAVER_CLIENT_ID')
CLIENT_SECRET = config('NAVER_CLIENT_SECRET')
HEADERS = {'X-Naver-Client-Id':CLIENT_ID, 'X-Naver-Client-Secret': CLIENT_SECRET}

url = 'https://openapi.naver.com/v1/search/movie.json'

adress = f'{url}?query={read.get("영화명(국문)")}'
response = requests.get(adress, headers=HEADERS).json()

print(response)
```

 movie_naver.py는 naver에 요청을 보내 응답을 보내는 프로젝트 입니다. 따라서 naver에 올바르게 요청을 보내 응답을 받는것이 가장 핵심적인 기술입니다.



```python
with open('movie.csv', 'r', newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
```

 movie.csv에서 정보를 가져오는것 또한 이 프로젝트의 핵심기술중 하나입니다. movie.csv의 파일을 열어 그 정보를 딕셔너리의 형태로 가져옵니다.



```python
dictionary.get('Key')
```

 마지막으로 딕셔너리의 형태로서 저장된 정보를 활용하기 위해 딕셔너리의 키값에 접근하여 벨류를 얻어 내어 정보를 얻어 활용해 프로젝트를 진행하였습니다.



## 3. movie_image.py

### 3.1 movie_image.py

​	앞서 네이버 영화 검색 API를 통해 얻은 이미지 URL에 요청을 보내 영화코드의 이름으로 이미지 파일로 저장합니다.

![movie_image](/uploads/bb6b8ee186c1bc96cc85b971d7cdc7b6/movie_image.PNG)



### 3.2 시행착오

 이 프로젝트는 이미 작성된 `movie_naver.csv`의 `image`의  URL에 접근하여 이미지파일을 다운받는것입니다. 이를 정확히 인지하지못하여 `CLIENT_ID` 와 `CLIENT_SECRET ` 를 이용해 요청을 보내 응답을 받으려 했습니다.  이는 코드를 작성해 나가며 깨닫게되어 이후 삭제하였습니다.



### 3.3 핵심

  ```python
with open(f'images/README.jpg','wb') as f:
	response = requests.get(image_url).content
	f.write(response)
  ```

위의 코드를 이용해 URL에 요청을 보내 `images`의 폴더에 `README.jpg` 의 파일을 저장하는것이 이 프로젝트의 핵심이었습니다. 



