from setuptools import setup, find_packages
from codecs import open

from xq import VERSION, NAME, DESCRIPTION

with open('README.rst', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name=NAME,
    description=DESCRIPTION,
    long_description=long_description,
    keywords='xml xpath text',
    version=VERSION,
    license='MPL 2.0',

    author='Ben Jeffrey',
    author_email='mail@benjeffrey.net',
    url='https://github.com/jeffbr13/xq',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3',
        'Intended Audience :: Developers',
        'Environment :: Console',
        'Topic :: Terminals',
        'Topic :: Text Processing :: Markup :: XML',
        'Topic :: Utilities',
        'License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)',
    ],

    packages=find_packages(),

    install_requires=[
        'lxml',
        'pygments'
    ],

    entry_points={
        'console_scripts': [
            'xq=xq.__main__:main',
        ],
    },
)
