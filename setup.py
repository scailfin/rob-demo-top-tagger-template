# This file is part of the Reproducible Open Benchmarks for Data Analysis
# Platform (ROB) - Top Tagger Benchmark Demo Template.
#
# ROB is free software; you can redistribute it and/or modify it under the
# terms of the MIT License; see LICENSE file for more details.

from setuptools import setup, find_packages


"""Required packages for install and tests."""

install_requires = [
    'argparse',
    'numpy'
]


tests_require = [
    'coverage>=4.0',
    'pytest',
    'pytest-cov'
]


extras_require = {
    'tests': tests_require,
}


setup(
    name='top-tagger-template',
    version='0.1.0',
    description='Template for ML4Jets Top Taggers',
    url='https://github.com/scailfin/rob-demo-top-tagger-template',
    author='Heiko Mueller',
    author_email='heiko.muller@gmail.com',
    license='MIT',
    packages=find_packages(exclude=('tests',)),
    include_package_data=True,
    extras_require=extras_require,
    tests_require=tests_require,
    install_requires=install_requires,
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python'
    ]
)
