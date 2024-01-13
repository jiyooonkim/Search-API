"""
Title : Inverted Index(역색인)
Date : 2024-01-13 ~
Desc:
- 문서를 토큰 단위로 분리하여 inverted index 생성
- Analyzer
    - Token filter : 대문자를 소문자화
    - Tokenizer
    - Character filter
- Indexing vs Hashing
    - Indexing :
    - Hashing :
"""
from pyspark.pandas.DataFrame import set_index
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

def tokenizer(df):
    return 0



if __name__ == '__main__':
    df = CreateData().read_data(file_path=input_path, file_type="csv", header=True)
    prod_df = df.select(F.col('상품명'), F.explode(F.split(F.col('상품명'), " ")).alias('tokens'))
    prod_df.withColumn("idx", set_index(F.col('상품명'))).show()
    # todo  : 상품명 기준 인덱스 생성

    exit(0)