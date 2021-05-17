#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click>=7.0', ]

setup_requirements = ['pytest-runner', ]

test_requirements = ['pytest>=3', ]

setup(
    author="Rob Scott",
    author_email='rob@rjdscott.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="A Pandas DataFrame SQL Query Utility",
    entry_points={
        'console_scripts': [
            'df_query=df_query.cli:main',
        ],
    },
    install_requires=["pandas"],
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='df_query',
    name='df_query',
    packages=find_packages(include=['df_query', 'df_query.*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/rjdscott/df_query',
    version='0.1.0',
    zip_safe=False,
)
