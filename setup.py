from setuptools import setup, find_packages

setup(
    name='pyqt-database-example',
    version='0.0.1',
    author='Jung Gyu Yoon',
    author_email='yjg30737@gmail.com',
    license='MIT',
    packages=find_packages(),
    description='PyQt Database (mainly SQLite currently) basic use example',
    url='https://github.com/yjg30737/pyqt-database-example.git',
    install_requires=[
        'PyQt5>=5.8',
    ]
)