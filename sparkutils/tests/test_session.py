import traceback
from unittest import TestCase
from sparkutils import session as spus

class TestSession(TestCase):
 
  def test_me(self):
    try:
      spark = spus.getLocal("sparkutils")
      count = spark.sparkContext.parallelize([1, 2, 3, 4]).count()
      self.assertEquals(count,4)
    except Exception as e:
      print "Failed to create Spark Session"
      traceback.print_exc()
      self.assertTrue(False)
