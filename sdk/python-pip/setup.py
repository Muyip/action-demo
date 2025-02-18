# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

packages=find_packages()
requirements = [
    "click>=5.0",
    "colorama>=0.3.9",
    "cookiecutter>=1.6.0"
]


setup(
    name='mt-my-simple-greet',
    version='0.3.18',
    packages=find_packages(),
    install_requires=requirements,
    author='Your Name',
    author_email='your.email@example.com',
    description='A simple example package',
    url='https://github.com/yourusername/my_package',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)

