# cmp\_version

A script and python module to compare version numbers. Use this to compare the version strings of packages, modules, really anything.

Since version 3.0, cmp\_version supports all kinds of complex version numbers, including those with releases ( like $version-5 ) or Epochs (like 5:$version)


Commandline Tool
----------------

You can use the provided *cmp-version* tool to compare two version strings. 

It will print to stdout "-1" if version1 is less/older than version2, "0" if they are equal, and "1" if version1 is greater/newer than version2.


Examples:

	$ ./cmp-version 1.0.1b 1.0.1a
	1

	$ ./cmp-version 1.0.1b 1.0.2
	-1

	$ ./cmp-version 1.0 1.0.0
	0


Comparing Filenames
-------------------

Without actually scanning the contents of a package, you can from a script compare the versions based on the filenames.

Example:

	$ cmp-version glibc-6.2.1-3.x86_64.rpm glibc-6.2.3-1.x86_64.rpm
	-1



Method Signature
----------------

The cmp\_version module provides a single method, *cmp\_version* which compares two versions "cmp" style (think strcmp or the "cmp" operator in python<3).

	
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


Special Type
------------

cmp\_version provides a special type, "VersionString", which inherits string. All the comparison magic functions are implemented, such that you can directly compare VersionString objects.

Example:

	>>> x = VersionString('0.1b2')
	>>> y = VersionString('.2b2')
	>>>
	>>> '0.1b2' < '.2b2' # Show that as strings this version compare gives wrong answer
	False
	>>> x < y # Show that using VersionString objects, the comparison does work
	True



Sorting Lists
-------------

You can sort a list of versions, or filenames containing versions etc like this:

    >>> from cmp_version import cmp_version, VersionString
    >>>
    >>> x = ['.9a', '0.9', '0.9.0', '1.2c', '1.1b', '1.b4.0']
    >>> sorted(x, key=VersionString)
    ['0.9', '0.9.0', '.9a', '1.1b', '1.2c', '1.b4.0']

	


Return value
------------

* 0 is returned when the two versions are equal, even if the strings are not equal (for example "1.0" is the same version as "1.0.0")

* -1 is returned when version1 is older/less than version2

* 1 is returned when version1 is newer/greater than version2.


License
-------

This module is released under Public Domain.
