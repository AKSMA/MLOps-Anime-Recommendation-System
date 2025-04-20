from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='PROJ2',
    version='0.1',
    author='Akshat Manihar',
    packages=find_packages(),
    install_requires=requirements,
)