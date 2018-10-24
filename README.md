# pyspark boilerplate
Based on [python-packaging](https://python-packaging.readthedocs.io/en/latest/index.html)


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
