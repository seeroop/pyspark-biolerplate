from pyspark.sql import SparkSession

def getYarn(name):    
    return SparkSession.builder\
        .master("yarn")\
        .appName(name)\
        .getOrCreate()

def getLocal(name):    
    return SparkSession.builder\
        .master("local[2]")\
        .appName(name)\
        .getOrCreate()
