from distutils.core import setup


REQUIRED = ['statsd']

EXTRAS = {
    # 'statsd': ['statsd']
}

setup(
    name='telemetry',
    version='0.2.0',
    packages=['telemetry',],
    package_dir={
      'telemetry': 'src/telemetry'
    },
    description='',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='trevor grayson',
    author_email='trevor@retentionscience.com',
    python_requires='2.7', #todo
    url='http://github.com/trevorgrayson/telemetry',

    py_modules=['telemetry'],

    entry_points={
        'console_scripts': ['telemetry=telemetry:main'],
    },

    install_requires=REQUIRED,
    extras_require=EXTRAS,
    include_package_data=True,
    license='MIT',
    classifiers=[
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 4',
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


)
