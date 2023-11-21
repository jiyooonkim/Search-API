## Flask 이용한 상품검색 API 

#### skill : pyspark, python
  + version : python3.9, pyspark3.3.2 

#### 구성 및 작업 내용
+ Data processing
  + Tokenizing 기준
    + 소문자 처리
    + 공백기준
    + 연속된 한글, 자모, 영문숫자하이픈
    + 이 외 통합
  + TF-IDF
    + 토큰 기반 TF-IDF Score 기준 내림차순
   
+ API
  + Flask
    + Get 방식
    + /search?query=아이폰14ProMax
