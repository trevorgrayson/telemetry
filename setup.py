import os
import subprocess
import setuptools
from distutils.core import setup


REQUIRED = ['statsd']

BIN_DIR = os.path.dirname(os.path.realpath(__file__))

EXTRAS = { # 'statsd': ['statsd'] 
}

setup(
    name='telemetry',
    version="v0.3.0",
    packages=setuptools.find_packages(),
    # ['telemetry',],
    package_data={'': ['README.md', 'VERSION']},
    #package_dir={ 'telemetry': 'src/telemetry' },
    description="""
Remote measuring abstraction for software applications.

`telemetry` serves as a simple facade or abstraction for various telemetry frameworks (e.g. statsd, graphite) 
allowing the end user to plug in the desired telemetry framework at deployment time. Think [slf4j](https://www.slf4j.org/)
but for events and numbers, not logs.  This library borrows from their example (and copy.)

As your projects grow, their telemetry requirements will change.  The purpose of this library is to simplify
implementation, provide easy configuration, encourage testing, and avoid vendor lock.


## Supported Services:

* statsd/graphite
    """,
    # long_description=open('README.md').read(),
    # long_description_content_type="text/markdown",
    author='trevor grayson',
    author_email='trevor@retentionscience.com',
    url='http://github.com/trevorgrayson/telemetry',

    py_modules=['telemetry'],

    # entry_points={ },

    # python_requires='2.7', #todo
    # install_requires=REQUIRED,
    # extras_require=EXTRAS,
    # include_package_data=True,
    license='MIT',
    classifiers=[
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        # 'Development Status :: 4',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries',
        'Topic :: System :: Monitoring',
        'Topic :: System :: Logging',
        # 'Programming Language :: Python :: 3',
        # 'Programming Language :: Python :: 3',
        # 'Programming Language :: Python :: 3.6',
        # 'Programming Language :: Python :: Implementation :: CPython',
        # 'Programming Language :: Python :: Implementation :: PyPy'
    ],
    include_package_data=True
)

# https://github.com/kennethreitz/setup.py/blob/master/setup.py
