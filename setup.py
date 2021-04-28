from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA example package',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/<MPOTTO123>/<package-mypackage>',
    author='<MPOTTO>',
    author_email='<motto@cellc.co.za>'
)