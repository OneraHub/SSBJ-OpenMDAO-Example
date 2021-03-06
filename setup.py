'''
Author: Remi Lafage <remi.lafage@onera.fr>

This package is distributed under Apache 2 license.
'''

from setuptools import setup

from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

CLASSIFIERS = """
Development Status :: 4 - Beta
Intended Audience :: Science/Research
Intended Audience :: Developers
License :: OSI Approved :: Apache Software License
Programming Language :: Python
Programming Language :: Python :: 2.7
Programming Language :: Python :: 3.6
Topic :: Software Development
Topic :: Scientific/Engineering
Operating System :: Microsoft :: Windows
Operating System :: Unix
Operating System :: MacOS
"""

metadata = dict(
    name='ssbj_disciplines',
    version='0.1.0',
    description='Disciplines of the SSBJ MDO test case used in SSBJ-OpenMDAO',
    author='Rémi Lafage',
    author_email='remi.lafage@onera.fr',
    license='Apache License, Version 2.0',
    classifiers=[_f for _f in CLASSIFIERS.split('\n') if _f],
    packages=[
        'ssbj_disciplines'
    ],
    python_requires='>=2.7,!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*,!=3.4.*,!=3.5.*',
    zip_safe=True,
    url = 'https://github.com/OneraHub/ssbj_openmdao',
    download_url = 'https://github.com/OneraHub/ssbj_openmdao/releases',
)

setup(**metadata)
