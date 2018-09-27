from sparkutils import session

spark = session.get_spark()
spark.sql("show tables").show()
