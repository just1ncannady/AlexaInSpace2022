Documentation for the gcb2rst.py script

Setup
-----
It may be necessary to install bs4 in the terminal. Before running this

$ pip3 install bs4

Also, the import certifi  may only be necessary for MacOS
# See: https://stackoverflow.com/questions/40684543/how-to-make-python-use-ca-certificates-from-mac-os-truststore


To run
------

The python script can be run from the command line as follows, where
'$' is the command-line prompt:

$ python3 gcb2rst.py

Input: mcsp-urls.txt
--------------------

The gcb2rst.py reads ULRs from the mcsp-urls.txt file. URLs
are stored one per line with no indentation, for example:

https://mobilecsp-2017.appspot.com/mobilecsp/unit?unit=1
https://mobilecsp-2017.appspot.com/mobilecsp/unit?unit=1&lesson=45

The URLs must use 'mobilecsp-2017.appspot.com' as the host name,
not 'course.mobilecsp.org'. 

In mcscp-urls.txt Lines that begin with a '#' are considered comments 
and ignored. 

Output
------
The script will generate one .rst file for each URL that is provided, e.g.:

I-Have-A-Dream-Tutorial.rst
Algorithm-Basics.rst

The output files will be stored in the same directory from which the Python
script is run.

MacOS Users
-----------

Python3 on MacOS no longer uses the Mac's built-in SSL certificates. This will prevent
the script from being able to access the GCB course pages. To fix this issue, see the
following:

https://stackoverflow.com/questions/40684543/how-to-make-python-use-ca-certificates-from-mac-os-truststore
