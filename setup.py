import os
import subprocess
import setuptools
from distutils.core import setup


REQUIRED = ['statsd']

BIN_DIR = os.path.dirname(os.path.realpath(__file__))

EXTRAS = {
    'statsd': ['statsd==3.3.0'],
    'slack': ['slackclient==2.9.3'],
}

setup(
    name='telemetry',
    version="v0.3.6",
    packages=setuptools.find_packages(),
    # ['telemetry',],
    package_data={'': ['README.md', 'VERSION']},
    #package_dir={ 'telemetry': 'src/telemetry' },
    description="""Remote measuring abstraction for software applications.""",
    # long_description=open('README.md').read(),
    # long_description_content_type="text/markdown",
    author='trevor grayson',
    author_email='trevor@retentionscience.com',
    url='http://github.com/trevorgrayson/telemetry',

    py_modules=['telemetry'],

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
