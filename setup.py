#!/usr/bin/env python
#


#vim: set ts=4 sw=4 expandtab

import os
from setuptools import setup


if __name__ == '__main__':
 

    dirName = os.path.dirname(__file__)
    if dirName and os.getcwd() != dirName:
        os.chdir(dirName)

    summary = 'A script and python module to compare version numbers. Use this to compare the version strings of packages, modules, really anything.'

    try:
        with open('README.rst', 'rt') as f:
            long_description = f.read()
    except Exception as e:
        sys.stderr.write('Exception when reading long description: %s\n' %(str(e),))
        long_description = summary

    setup(name='cmp_version',
            version='2.1.1',
            packages=['cmp_version'],
            scripts=['cmp-version'],
            author='Tim Savannah',
            author_email='kata198@gmail.com',
            maintainer='Tim Savannah',
            url='https://github.com/kata198/cmp_version',
            maintainer_email='kata198@gmail.com',
            description=summary,
            long_description=long_description,
            license='Public Domain',
            keywords=['cmp', 'version', 'cmp_version', 'compare', 'version', 'number', 'package', 'rpm', 'commandline', 'tool', 'module', 'release'],
            classifiers=['Development Status :: 5 - Production/Stable',
                         'Programming Language :: Python',
                         'License :: Public Domain',
                         'Programming Language :: Python :: 2',
                          'Programming Language :: Python :: 2',
                          'Programming Language :: Python :: 2.6',
                          'Programming Language :: Python :: 2.7',
                          'Programming Language :: Python :: 3',
                          'Programming Language :: Python :: 3.3',
                          'Programming Language :: Python :: 3.4',
                          'Programming Language :: Python :: 3.5',
                          'Topic :: Software Development :: Version Control',
                          'Topic :: Software Development :: Libraries :: Python Modules',
            ]
    )



