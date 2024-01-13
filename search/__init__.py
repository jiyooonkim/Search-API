
import pyspark.sql.types as T
import pyspark.sql.functions as F
import re
DEFAULT_PATH = '../'


class CreateData:

    def __init__(self):
        self.application_name = application_name

        def save_data(self, dirctory, file_type, mode=None):
            return None

def init_spark_session(app_name="spark_job", arrow=True, dm="16g", dc=8, em="16g", deployMode="client"):
    from pyspark.sql import SparkSession
    spark = SparkSession.builder \
        .appName(app_name) \
        .master('local[*]') \
        .config('spark.sql.execution.arrow.pyspark.enabled', arrow) \
        .config('spark.sql.session.timeZone', 'UTC') \
        .config('spark.driver.memory', dm) \
        .config('spark.driver.cores', dc) \
        .config('spark.executor.memory', em) \
        .config('spark.submit.deployMode', deployMode) \
        .config("spark.driver.bindAddress", "127.0.0.1") \
        .config("spark.network.timeout", 10000) \
        .config('spark.ui.showConsoleProgress', True) \
        .config('spark.sql.repl.eagerEval.enabled', True) \
        .getOrCreate()
    return spark

def read_data(self, file_path, file_type="parquet", header=None):
    spark = init_spark_session()
    if file_type is 'parquet':
        df = spark.read.parquet(file_path)
    elif file_type is 'csv':
        df =spark.read.csv(file_path)
    return df




