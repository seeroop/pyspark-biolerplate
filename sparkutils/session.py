from pyspark.sql import SparkSession

def get_spark():
    return (SparkSession.builder
                .master("yarn")
                .appName("changeme")
                .getOrCreate())
