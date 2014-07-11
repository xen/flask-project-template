# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name="flask-project-template",
    version='0.1',
    url='',
    description='',
    author='Mikhail Kashkin',
    author_email='mkashkin@gmail.com',
    packages=["project"],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'Flask',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ]
)
