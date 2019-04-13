from setuptools import setup, find_packages

setup(
    name='mylogger',
    version='0.0.1',
    author='Alberto de la Cruz',
    description='Mylogger',
    platforms='Linux',
    packages=find_packages(exclude=['tests', 'specs', 'integration_specs']),
    install_requires=[
        'infcommon==0.0.1'
    ],
    dependency_links=[
        'git+ssh://git@github.com/aleasoluciones/infcommon.git#egg=infcommon-0.0.1'
    ]
)
