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


    def test_compareWithRelease(self):

        cmpFunc = cmp_version.cmp_version

        # Some equal stancing, different release
        assert cmpFunc('1.0-1', '1.0-1') == 0 , 'Expected 1.0-1 to be equal to 1.0-1'

        assert cmpFunc('1.8-2', '1.8-4') < 0 , 'Expected "1.8-2" to be less than "1.8-4"'
        assert cmpFunc('1.8-4', '1.8-2') > 0 , 'Expected "1.8-4" to be greater than "1.8-2"'

        # Different stance, different release
        assert cmpFunc('2.49.93-1', '2.49-3') > 0 , 'Expected "2.49.93-1" to be greater than "2.49-3"'
        assert cmpFunc('2.49-6', '2.49.1-6') < 0 , 'Expected "2.49-6" to be less than "2.49.1-6"'

        assert cmpFunc('5-9', '5.1') < 0 , 'Expected "5-9" to be less than "5.1"'

        # Check release in one, not in other
        assert cmpFunc('1.5.0-1', '1.5.0') > 0 , 'Expected "1.5.0-1" to be greater than "1.5.0"'
        assert cmpFunc('1.5.0', '1.5.0-1') < 0 , 'Expected "1.5.0" to be less than "1.5.0-1"'

        # Check that a -0 release is treated same as no release
        assert cmpFunc('1.1-0', '1.1') == 0 , 'Expected "1.1-0" to be equal to "1.1"'

if __name__ == '__main__':
    sys.exit(subprocess.Popen('GoodTests.py -n1 "%s" %s' %(sys.argv[0], ' '.join(['"%s"' %(arg.replace('"', '\\"'), ) for arg in sys.argv[1:]]) ), shell=True).wait())
