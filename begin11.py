#Operating System Interface

# import os
# os.getcwd()      # Return the current working directory

# os.chdir('/server/accesslogs')   # Change current working directory
# os.system('mkdir today')   # Run the command mkdir in the system shell


import os
dir(os)

help(os)


#For daily file and directory management tasks, the shutil module provides a higher level interface that is easier to use


import shutil
a=shutil.copyfile('data.db', 'archive.db')

b = shutil.move('/build/executables', 'installdir')



#File Wildcards

import glob
a=glob.glob('*.py')
print(a)


#Command Line Arguments

#Common utility scripts often need to process command line arguments. These arguments are stored in the sys module’s argv attribute as a list. For instance, let’s take the following demo.py file

# File demo.py
import sys
print(sys.argv)



#The argparse module provides a more sophisticated mechanism to process command line arguments. The following script extracts one or more filenames and an optional number of lines to be displayed
import argparse

parser = argparse.ArgumentParser(
    prog='top',
    description='Show top lines from each file')
parser.add_argument('filenames', nargs='+')
parser.add_argument('-l', '--lines', type=int, default=10)
args = parser.parse_args()
print(args)




# Error Output Redirection and Program Termination


sys.stderr.write('Warning, log file not found starting a new one\n')




#String Pattern Matching
#The re module provides regular expression tools for advanced string processing. For complex matching and manipulation, regular expressions offer succinct, optimized solutions

import re
a=re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')
print(a)

b=re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat')
print(b)

#Mathematics
#The math module gives access to the underlying C library functions for floating-point math

import math
a = math.cos(math.pi / 4)
print(a)
b = math.log(1024, 2)
print(b)

#The random module provides tools for making random selections




import random
random.choice(['apple', 'pear', 'banana'])
print(random.choice)
random.sample(range(100), 10)   # sampling without replacement
print(random.sample)

random.sample()    # random float from the interval [0.0, 1.0)
print(random.sample())
random.randrange(6)    # random integer chosen from range(6)
print(random.randrange)


#The statistics module calculates basic statistical properties (the mean, median, variance, etc.) of numeric data



import statistics
data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
statistics.mean(data)
print(statistics.mean)
statistics.median(data)
print(statistics.median)
statistics.variance(data)
print(statistics.variance)

#There are a number of modules for accessing the internet and processing internet protocols. Two of the simplest are urllib.request for retrieving data from URLs and smtplib for sending mail


from urllib.request import urlopen
with urlopen('http://worldtimeapi.org/api/timezone/etc/UTC.txt') as response:
    for line in response:
        line = line.decode()             # Convert bytes to a str
        if line.startswith('datetime'):
            print(line.rstrip())         # Remove trailing newline



import smtplib
server = smtplib.SMTP('localhost')
server.sendmail('soothsayer@example.org', 'jcaesar@example.org',
"""To: jcaesar@example.org
From: soothsayer@example.org

Beware the Ides of March.
""")
print(server.sendmail)
server.quit()


#Dates and Times

# dates are easily constructed and formatted
from datetime import date
now = date.today()
now

now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.")
print(now.strftime)

# dates support calendar arithmetic
birthday = date(1964, 7, 31)
age = now - birthday
print(age.days)


#datetime module supplies classes for manipulating dates and times in both simple and complex ways. While date and time arithmetic is supported, the focus of the implementation is on efficient member extraction for output formatting and manipulation


#Data Compression
#Common data archiving and compression formats are directly supported by modules including: zlib, gzip, bz2, lzma, zipfile and tarfile.


import zlib
s = b'witch which has which witches wrist watch'
len(s)

t = zlib.compress(s)
len(t)
print(len(t))
a =zlib.decompress(t)
print(a)
b = zlib.crc32(s)
print(b)




# Performance Measurement


from timeit import Timer
a=Timer('t=a; a=b; b=t', 'a=1; b=2').timeit()
print(a)
b = Timer('a,b = b,a', 'a=1; b=2').timeit()
print(b)

#Quality Control





def average(values):
    """Computes the arithmetic mean of a list of numbers.

    >>> print(average([20, 30, 70]))
    40.0
    """
    return sum(values) / len(values)

import doctest
doctest.testmod()   # automatically validate the embedded tests




#The unittest module is not as effortless as the doctest module, but it allows a more comprehensive set of tests to be maintained in a separate file


import unittest

class TestStatisticalFunctions(unittest.TestCase):

    def test_average(self):
        self.assertEqual(average([20, 30, 70]), 40.0)
        self.assertEqual(round(average([1, 5, 7]), 1), 4.3)
        with self.assertRaises(ZeroDivisionError):
            average([])
            print(average([]))
        with self.assertRaises(TypeError):
            average(20, 30, 70)
            print(average(20, 30, 70))

unittest.main()  # Calling from the command line invokes all tests




#Batteries Included
#Python has a “batteries included” philosophy. This is best seen through the sophisticated and robust capabilities of its larger packages.




