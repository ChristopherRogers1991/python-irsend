from setuptools import setup
from os import path

package_dir = path.abspath(path.dirname(__file__))

with open(path.join(package_dir, 'README.md')) as readme:
    long_description = readme.read()

setup(
    name='py_irsend',
    version='1.0.0',
    packages=['py_irsend'],
    url='https://github.com/ChristopherRogers1991/python-irsend',
    license='GPLv3',
    author='Christopher Rogers',
    author_email='ChristopherRogers1991@gmail.com',
    description="A simple wrapper for lirc's irsend. ",
    long_description=long_description,
    keywords='lirc irsend',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3'
    ],
)
