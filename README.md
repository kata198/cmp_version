# cmp\_version

A script and python module to compare version numbers. Use this to compare the version strings of packages, modules, really anything.


Commandline Tool
----------------

You can use the provided *cmp-version* tool to compare two version strings. 

It will print to stdout "-1" if version1 is less/older than version2, "0" if they are equal, and "1" if vrsion1 is greater/newer than version2.


Examples:

	$ ./cmp-version 1.0.1b 1.0.1a
	1

	$ ./cmp-version 1.0.1b 1.0.2
	-1

	$ ./cmp-version 1.0 1.0.0
	0



Method Signature
----------------

The cmp\_version module provides a single method, *cmp\_version* which compares two versions "cmp" style (think strcmp or the "cmp" operator in python<3).

**Return value:**

* 0 is returned when the two versions are equal, even if the strings are not equal (for example "1.0" is the same version as "1.0.0")

* -1 is returned when version1 is older/less than version2

* 1 is returned when version1 is newer/greater than version2.

	.
	
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


License
-------

This module is released under Public Domain.
