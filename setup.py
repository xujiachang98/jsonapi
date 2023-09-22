from setuptools import setup, find_packages

setup(
    name='jsonapi',
    version='0.0.1',
    install_requires=[],
    description='Extended JSON encoding and decoding library',
    author='Xujia Chang',
    author_email='chang.xu@northeastern.edu',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
)
