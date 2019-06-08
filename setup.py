import subprocess
from distutils.core import setup


REQUIRED = ['statsd']


git_proc = subprocess.Popen('bin/version', stdout=subprocess.PIPE, shell=True)
(VERSION, err) = git_proc.communicate()
git_proc.wait()

VERSION = VERSION.strip()

EXTRAS = {
    # 'statsd': ['statsd']
}

setup(
    name='telemetry',
    version=VERSION,
    packages=['telemetry',],
    #package_dir={ 'telemetry': 'src/telemetry' },
    description='',
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
    ]
)

# https://github.com/kennethreitz/setup.py/blob/master/setup.py
