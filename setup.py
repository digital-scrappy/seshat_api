from setuptools import setup

setup(
    name='seshat_api',
    version='0.1.0',
    description='A Python package for interacting with the Seshat API.',
    url='https://github.com/Seshat-Global-History-Databank/seshat_api',
    author='Kalle Westerling',
    author_email='kwesterling@turing.ac.uk',
    license='',
    packages=['seshat_api', 'seshat_api.core', 'seshat_api.models'],
    install_requires=['requests'],
)
