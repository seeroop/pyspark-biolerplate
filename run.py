import sparkutils.session as spus

spark = spus.getYarn("sparkutlis")
spark.sql("show tables").show()

