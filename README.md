## Search API Project
#### Flask 이용한 상품검색 API 

##### skill : pyspark, python
  + version : python3.8, pyspark3.3.2 

##### 구성 및 작업 내용
+ Data processing
  + Tokenizing (대/소문자, 공백, 연속된 한글, 자모, 영문/숫자/하이픈)
  + TF-IDF
    + 토큰 기반 TF-IDF Score 기준 내림차순
  + 역색인
  
+ API
  + Flask
    + Get 방식
    + /search?query=아이폰14ProMax
