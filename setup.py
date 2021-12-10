import os
import setuptools
from distutils.core import setup


REQUIRED = ['statsd']

BIN_DIR = os.path.dirname(os.path.realpath(__file__))

EXTRAS = { # 'statsd': ['statsd']
    'datadog': ["datadog-api-client"],
    'statsd': ['statsd']
}

setup(
    name='telemetry',
    version='1.2.3',  # open("VERSION", "r").read(),
    packages=setuptools.find_packages(),
    # ['telemetry',],
    package_data={'': ['README.md', 'VERSION']},
    #package_dir={ 'telemetry': 'src/telemetry' },
    description="Remote measurements for your app",
    long_description="""
Remote measuring abstraction for software applications.

`telemetry` serves as a simple facade or abstraction for various telemetry frameworks (e.g. pagerduty, slack, graphite) 
allowing the end user to plug in the desired telemetry framework at deployment time. Think [slf4j](http://www.slf4j.org/)
but for events and numbers.  This library borrows from their example (and copy.)

As your projects grow, their telemetry requirements will change.  The purpose of this library is to simplify
implementation, provide easy configuration, encourage testing, and avoid vendor lock.

## Supported Services:

* pagerduty
* slack
* statsd, graphite, datadog

Telemeters preference to being configurable, but don't require more than
credentials to get working. For instance, slack can be implemented with
the following:

```SLACK_ROOM_ID=Txxx/Byyy/Zzzz python
import logging
from telemetry import SlackTelemeter

logging.basicConfig(level=logging.INFO)
logging.getLogger().addHandler(SlackTelemeter())
logging.info("hello room!")
```

or 

```SLACK_ROOM_ID=Txxx/Byyy/Zzzz python

from telemetry import SlackTelemeter
meter = SlackTelemeter()
meter.message("your message!")
```

Clients are written using core python libraries, so `telemetry` is light weight.
 
    """, # open("README.md", "r").read(),
    # long_description=open('README2.0.md').read(),
    long_description_content_type="text/markdown",
    author='trevor grayson',
    author_email='trevor@dave.com',
    url='http://github.com/trevorgrayson/telemetry',

    py_modules=['telemetry'],
    scripts=['bin/telemetry'],
    # entry_points={ },

    # python_requires='2.7', #todo
    # install_requires=REQUIRED,
    extras_require=EXTRAS,
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
