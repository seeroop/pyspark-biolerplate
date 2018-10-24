from sparkutils import session

spark = session.getInstance("sparkutlis")
spark.sql("show tables").show()

