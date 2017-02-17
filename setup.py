import sys

from setuptools import setup
from setuptools import find_packages

version = '0.0.1'

# Please update tox.ini when modifying dependency version requirements
install_requires = [
    'ply'
]

setup(
    name='jbossply',
    version=version,
    description='JBoss CLI output parser',
    url='https://github.com/EnigmaBridge/jbossply',
    author="Dusan Klinec (ph4r05)",
    author_email='ph4r05@gmail.com',
    license=open('LICENSE').read(),
    long_description=open('README.rst').read(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5'
    ],

    packages=find_packages(),
    include_package_data=True,
    install_requires=install_requires,
    extras_require={
        'dev': [],
        'docs': [],
    },

    entry_points={
        'console_scripts': [
            'jboss2json = jbossply.main:main',
        ],
    }
)
