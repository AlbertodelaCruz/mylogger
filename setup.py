from setuptools import setup, find_packages

setup(
    name='mylogger',
    version='0.0.1',
    author='Alberto de la Cruz',
    description='Mylogger',
    platforms='Linux',
    packages=find_packages(exclude=['tests', 'specs', 'integration_specs']),
    install_requires=[
        'infcommon'
        ],
    dependency_links=[
        'git+https://github.com/aleasoluciones/infcommon.git#egg=infcommon'
        ]
)
