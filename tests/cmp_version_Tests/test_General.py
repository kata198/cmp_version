#!/usr/bin/env GoodTests.py
'''
    Test various comparison methods
'''

import copy
import sys
import subprocess

import cmp_version

class TestGeneral(object):
    '''
        Tests some attribute behaviour
    '''


    def test_compareMajorMinor(self):
        
        cmpFunc = cmp_version.cmp_version

        assert cmpFunc('1.0', '1.0') == 0 , 'Expected 1.0 to be equal to 1.0'

        assert cmpFunc('1.0', '2.0') < 0 , 'Expected 2.0 to be greater than 1.0'
        assert cmpFunc('2.0', '1.0') > 0 , 'Expected 1.0 to be less than 2.0'


if __name__ == '__main__':
    sys.exit(subprocess.Popen('GoodTests.py -n1 "%s" %s' %(sys.argv[0], ' '.join(['"%s"' %(arg.replace('"', '\\"'), ) for arg in sys.argv[1:]]) ), shell=True).wait())
