# pyspark boilerplate
Based on [python-packaging](https://python-packaging.readthedocs.io/en/latest/index.html)


## build source distribution
python setup.py sdist

## build source distribution as tgz
spark2-submit --py-files=dist/sparkutils-0.1.tar.gz run.py

## build source distribution as zip
python setup.py sdist --format=zip

## build source distribution
spark2-submit --py-files=dist/sparkutils-0.1.zip run.py

## build binary egg distribution
python setup.py bdist_egg

## run package
spark2-submit --py-files=dist/sparkutils-0.1-py2.7.egg run.py
