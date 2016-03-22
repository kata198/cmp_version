'''
    The following work authored by Tim Savannah has been dedicated to the Public Domain.
    You are free to use or modify.
'''


import re
import sys

try:
    cmp
except NameError:
    def cmp(a, b):
        if a < b:
            return -1
        if a > b:
            return 1
        return 0

__all__ = ('cmp_version',)

__version__ = '1.0.2'

__version_tuple__ = (1, 0, 2)

ALPHA_OR_NUM_RE = re.compile('([a-zA-Z]+)|([0-9]+)')

def cmp_version(version1, version2):
    '''
        cmp_version - Compare two version strings, checking which one represents a "newer" (greater) release.

        Note that even if two version strings are not equal string-wise, they may still be equal version-wise (e.x. 1.0.0 is the same version as 1.0)

        @param version1 <str> - A version string
        @param version2 <str> - A version string

        @return <int>
            -1  if version1 is older/less than version2
            0   if version1 is equal to version2
            1   if version1 is newer/greater than version2

        So for example,

            cmp_version('1.0.5b', '1.0.5a') would return 1 because 1.0.5b comes after 1.0.5a
    '''
    if version1 == version2:
        return 0
    
    version1Split = version1.split('.')
    version2Split = version2.split('.')

    version1Len = len(version1Split)
    version2Len = len(version2Split)

    while version1Len < version2Len:
        version1Split += ['0']
        version1Len += 1
    else:
        while version2Len < version1Len:
            version2Split += ['0']
            version2Len += 1
            

    for i in range(version1Len):
        try:
            cmpRes = cmp(int(version1Split[i]), int(version2Split[i]))
            if cmpRes != 0:
                return cmpRes
        except ValueError:
            # Some sort of letter in here
            try1 = ALPHA_OR_NUM_RE.findall(version1Split[i])
            try1Len = len(try1)
            try2 = ALPHA_OR_NUM_RE.findall(version2Split[i])
            try2Len = len(try2)
            for j in range(len(try1)):
                if j >= try2Len:
                    return 1
                testSet1 = try1[j]
                testSet2 = try2[j]
                
                res1 = cmp(testSet1[0], testSet2[0])
                if res1 != 0:
                    return res1
                
                res2 = 0 
                if testSet1[1].isdigit():
                    if testSet2[1].isdigit():
                        res2 = cmp(int(testSet1[1]), int(testSet2[1]))
                    else:
                        return 1
                else:
                    if testSet2[1].isdigit():
                        return 1
                if res2 != 0:
                    return res2

            if try2Len > try1Len:
                return -1
                
            

    return 0

