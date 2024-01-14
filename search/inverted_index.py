"""
Title : Inverted Index(역색인)
Date : 2024-01-13 ~
Desc:
- 역색인 생성과정
    1. 문서를 토큰 단위(term)로 분리(데이터 전처리 포함)
    2. inverted index 생성
- Analyzer
    - Token filter : 대문자를 소문자화
    - Tokenizer
    - Character filter
- Indexing vs Hashing
    - Indexing :
    - Hashing :
"""

from pyspark.sql.window import Window
import pyspark.sql.functions as F
import os

os.chdir('../../')
from search import CreateData

input_path = ""

# import yaml
#
# with open('conf.yaml', 'r') as f:
#     config = yaml.load(f)
# print(config['1st_key']) # value_1
input_path = "SearchAPI/data/prod/nvr_prod.csv"


def search_or(df, query):
    # for query in query_tokenizer(query):


    return 0


def search_and(df, query):
    return 0


def query_tokenizer(txt):
    return list(txt.split(" "))


if __name__ == '__main__':
    df = CreateData().read_data(file_path=input_path, file_type="csv", header=True)
    # todo  불용어 제거, 형태소분석, 동의어 처리
    prod_df = (df.select(
        F.col('상품명'),
        F.explode(
            F.split(
                F.trim(
                    F.regexp_replace(
                        F.regexp_replace(F.lower(F.col('상품명')), "[^A-Za-z0-9가-힣]", ' '), r"\s+", ' '
                    )
                ), ' '
            )
        ).alias('tokens')
    ).withColumn(
        "idx",
        F.rank().over(Window().partitionBy().orderBy(F.col('상품명'))))
    )
    # prod_df.show(100, False)

    prod_df.groupby(F.col('tokens')).agg(F.collect_list(F.col('idx'))).show()

    txt = " 다즐샵 식단 도시락 15종 10팩+ "
    query_tokenizer(txt)

    from pyspark.sql import SparkSession

    sc = SparkSession.getOrCreate()


    data = [1,2,3,4,5]
    print(sc.parallelize(data))
    exit(0)
