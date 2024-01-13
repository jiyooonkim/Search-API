"""
Title : 역색인


"""
from flask import Flask, request
import json
import re
from SearchAPI import init_spark_session

if __name__ == '__main__':
    print("main")
    init_spark_session()