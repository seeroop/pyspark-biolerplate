# pyspark boilerplate
Based on [python-packaging](https://python-packaging.readthedocs.io/en/latest/index.html)

## running unit tests

```
SPARK_HOME=/opt/cloudera/parcels/SPARK2/lib/spark2 \
PYTHONPATH=$PYTHONPATH:$SPARK_HOME/python/lib/pyspark.zip \
PYTHONPATH=$PYTHONPATH:$SPARK_HOME/python/lib/py4j-0.10.7-src.zip \
python setup.py test

PYTHONPATH=$PYTHONPATH:/opt/cloudera/parcels/SPARK2/lib/spark2/python/lib/pyspark.zip:/opt/cloudera/parcels/SPARK2/lib/spark2/python/lib/py4j-0.10.7-src.zip python setup.py test
```

## build examples
```
python setup.py sdist
python setup.py sdist --format=zip
python setup.py bdist_egg
```

## run examples
```
spark2-submit --py-files=dist/sparkutils-0.1.tar.gz run.py
spark2-submit --py-files=dist/sparkutils-0.1.zip run.py
spark2-submit --py-files=dist/sparkutils-0.1-py2.7.egg run.py
```
