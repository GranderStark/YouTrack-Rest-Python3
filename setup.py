from os import path
from setuptools import setup

here = path.abspath(path.dirname(__file__))


setup(
    name='youtrack',
    version='0.0.1',
    python_requires='>=3',
    packages=['youtrack', 'youtrack.sync'],
    license='Apache 2.0',
    maintainer='Lev Subbotin',
    maintainer_email='grander.stark@yandex.ru',
    description='Python3 library for interacting with YouTrack via REST API',
    install_requires=[
        "httplib2 >= 0.7.4",
        # Cannot use original module because at the time it was modified in youtrack repo.
        # "urllib2_file",
        "six"
    ]
)
