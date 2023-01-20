import setuptools

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name='heartbit',
    author='Ravi Tiwari',
    author_email='rtiwariops@gmail.com',
    description='open source observability platform',
    keywords='pypi, package',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='',
    project_urls={
        'Documentation': '',
        'Bug Reports':
        'https://github.com/heartbit-dev/heartbit/issues',
        'Source Code': 'https://github.com/heartbit-dev/heartbit',
        # 'Funding': '',
        # 'Say Thanks!': '',
    },
    classifiers=[
        # see https://pypi.org/classifiers/
        'Development Status :: 5 - Production/Stable',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3 :: Only',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    extras_require={
        'dev': ['check-manifest'],
    },
)

