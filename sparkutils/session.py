from pyspark.sql import SparkSession

def getOrCreate(name):
    return SparkSession.builder\
        .master("yarn")\
        .appName(name)\
        .getOrCreate()
