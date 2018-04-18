#!/usr/bin/env GoodTests.py
'''
    Test various comparison methods
'''

import copy
import sys
import subprocess

import cmp_version

class TestEpoch(object):
    '''
        Tests some attribute behaviour
    '''


    def test_compareWithEpochs(self):
        
        cmpFunc = cmp_version.cmp_version

        assert cmpFunc('1.5', '2:0.9') < 0 , 'Expected "1.5" to be less than "2:0.9"'
        assert cmpFunc('1.0', '0:1.0') == 0 , 'Expected "1.0" to be equal to "0:1.0"'
        assert cmpFunc('3:1.0', '3:1.0') == 0 , 'Expected "3:1.0" to be equal to "3:1.0"'
        assert cmpFunc('4:1.0', '3:1.0') > 0 , 'Expected "4:1.0" to be greater than "3:1.0"'
        assert cmpFunc('4:1.5-2', '3:1.5-4') > 0 , 'Expected "4:1.5-2" to be greater than "3:1.5-4"'


if __name__ == '__main__':
    sys.exit(subprocess.Popen('GoodTests.py -n1 "%s" %s' %(sys.argv[0], ' '.join(['"%s"' %(arg.replace('"', '\\"'), ) for arg in sys.argv[1:]]) ), shell=True).wait())
