# sparkutils


## build package
python setup.py sdist

## build source distribution
spark2-submit --py-files=dist/sparkutils-0.1.tar.gz run.py


## build binary distribution
python setup.py bdist_egg

## run package
spark2-submit --py-files=dist/sparkutils-0.1-py2.7.egg run.py
