#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

requirements = [
    'web.py',
    'pyClamd',
]

setup(
    name='multiav',
    version='0.1.0',
    description="MultiAV scanner with Python and JSON API",
    author="Joxean Koret",
    author_email='admin@joxeankoret.com',
    url='https://github.com/haruka-YNU/multiav',
    packages=[
        'multiav',
    ],
    package_dir={'multiav':
                 'multiav'},
    include_package_data=True,
    install_requires=requirements,
    license="ISCL",
    zip_safe=False,
    keywords='multiav',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
)
