"""
Title : 역색인
Date : 2024-01-13 ~
"""
from flask import Flask, request
import json
import re
import os
os.chdir('../')
from search import CreateData

input_path = ""

# import yaml
#
# with open('conf.yaml', 'r') as f:
#     config = yaml.load(f)
# print(config['1st_key']) # value_1
input_path = "/Users/jy_kim/Documents/private/SearchAPI/data/prod/nvr_prod.csv"
# todo 경로 왜 안먹히냐... 아...

if __name__ == '__main__':
    print(os.getcwd())
    # print(CreateData.save_data())
    # print(CreateData.init_spark_session())
    print(CreateData().read_data(file_path=input_path, file_type="csv", header=None))

    exit(0)