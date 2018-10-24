from pyspark.sql import SparkSession

def getInstance(name):    
    return SparkSession.builder\
        .master("yarn")\
        .appName(name)\
        .getOrCreate()
