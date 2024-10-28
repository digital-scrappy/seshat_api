from setuptools import setup

setup(
    name='seshat_api',
    version='0.1.2',
    description='A Python package for interacting with the Seshat API.',
    url='https://github.com/Seshat-Global-History-Databank/seshat_api',
    author='Kalle Westerling, Ed Chalstrey',
    author_email='kwesterling@turing.ac.uk, echalstrey@turing.ac.uk',
    license='',
    packages=['seshat_api',
              'seshat_api.core',
              'seshat_api.crisisdb',
              'seshat_api.general',
              'seshat_api.rt',
              'seshat_api.sc',
              'seshat_api.wf',
              'seshat_api.models'],
    install_requires=['requests'],
)
