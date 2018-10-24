reload(session)

from sparkutils import session

spark = session.getOrCreate("sparkutils")
spark.sql("show tables").show()
