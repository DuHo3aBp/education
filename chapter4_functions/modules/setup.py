#создание файла установки, включающего функцию vsearch6.py
from setuptools import setup

setup(
    name='vsearch6',
    version='1.0',
    description='Search tool',
    author='HF Python 2e',
    author_email='demo@demo.com',
    url='demo.com',
    py_modules=['vsearch6'],
)

#нужно создать еще README.txt
#далее в командноц строке заходим в папку и выполняем
#следующий код: py -3 setup.py sdist

#после создания дистрибутива нужно установить пакет с помощью pip
#в созданной папке dist запустить
#следующий код: py -3 -m pip install vsearch6-1.0.tar.gz

