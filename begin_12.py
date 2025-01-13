#Output Formatting



import reprlib
a = reprlib.repr(set('supercalifragilisticexpialidocious'))
print(a)

#The pprint module offers more sophisticated control over printing both built-in and user defined objects in a way that is readable by the interpreter.

import pprint
t = [[[['black', 'cyan'], 'white', ['green', 'red']], [['magenta',
    'yellow'], 'blue']]]

pprint.pprint(t, width=30)

#The textwrap module formats paragraphs of text to fit a given screen width

import textwrap
doc = """The wrap() method is just like fill() except that it returns
a list of strings instead of one big string with newlines to separate
the wrapped lines."""

print(textwrap.fill(doc, width=40))

#The locale module accesses a database of culture specific data formats. The grouping attribute of locale’s format function provides a direct way of formatting numbers with group separators.

import locale
locale.setlocale(locale.LC_ALL, 'English_United States.1252')


conv = locale.localeconv()          # get a mapping of conventions
x = 1234567.8
locale.format_string("%d", x, grouping=True)

a = locale.format_string("%s%.*f", (conv['currency_symbol'],
                     conv['frac_digits'], x), grouping=True)

print(a)

#Templating

#The string module includes a versatile Template class with a simplified syntax suitable for editing by end-users. This allows users to customize their applications without having to alter the application.

from string import Template
t = Template('${village}folk send $$10 to $cause.')
a = t.substitute(village='Nottingham', cause='the ditch fund')

print(a)

#The string module includes a versatile Template class with a simplified syntax suitable for editing by end-users. This allows users to customize their applications without having to alter the application.

# t = Template('Return the $item to $owner.')
# d = dict(item='unladen swallow')
# t.substitute(d)



# b = t.safe_substitute(d)

# print(b)


import time, os.path
photofiles = ['img_1074.jpg', 'img_1076.jpg', 'img_1077.jpg']
class BatchRename(Template):
    delimiter = '%'

fmt = input('Enter rename style (%d-date %n-seqnum %f-format):  ')


t = BatchRename(fmt)
date = time.strftime('%d%b%y')
for i, filename in enumerate(photofiles):
    base, ext = os.path.splitext(filename)
    newname = t.substitute(d=date, n=i, f=ext)
    print('{0} --> {1}'.format(filename, newname))



# Working with Binary Data Record Layouts


# import struct

# with open('myfile.zip', 'rb') as f:
#     data = f.read()

# start = 0
# for i in range(3):                      # show the first 3 file headers
#     start += 14
#     fields = struct.unpack('<IIIHH', data[start:start+16])
#     crc32, comp_size, uncomp_size, filenamesize, extra_size = fields

#     start += 16
#     filename = data[start:start+filenamesize]
#     start += filenamesize
#     extra = data[start:start+extra_size]
#     print(filename, hex(crc32), comp_size, uncomp_size)

#     start += extra_size + comp_size     # skip to the next header

    #Multi-threading


#     import threading, zipfile

# class AsyncZip(threading.Thread):
#     def __init__(self, infile, outfile):
#         threading.Thread.__init__(self)
#         self.infile = infile
#         self.outfile = outfile

#     def run(self):
#         f = zipfile.ZipFile(self.outfile, 'w', zipfile.ZIP_DEFLATED)
#         f.write(self.infile)
#         f.close()
#         print('Finished background zip of:', self.infile)

# background = AsyncZip('mydata.txt', 'myarchive.zip')
# background.start()
# print('The main program continues to run in foreground.')

# background.join()    # Wait for the background task to finish
# print('Main program waited until background was done.')



#Logging

# logging module offers a full featured and flexible logging system. At its simplest, log messages are sent to a file or to sys.stderr

import logging
a = logging.debug('Debugging information')
print(a)
b = logging.info('Informational message')
print(b)
c = logging.warning('Warning:config file %s not found', 'server.conf')
print(c)
d = logging.error('Error occurred')
print(d)
e = logging.critical('Critical error -- shutting down')
print(e)




# Weak Reference

import weakref, gc
class A:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return str(self.value)

a = A(10)                   # create a reference
d = weakref.WeakValueDictionary()
d['primary'] = a            # does not create a reference
d['primary']  

            # fetch the object if it is still alive


del a                       # remove the one reference
gc.collect()                # run garbage collection right away

               # entry was automatically removed



#Tools for Working with List

from array import array
a = array('H', [4000, 10, 700, 22222])
sum(a)

print(a[1:3])





from collections import deque
d = deque(["task1", "task2", "task3"])
d.append("task4")
print("Handling", d.popleft())



#the bisect module with functions for manipulating sorted lists:

import bisect
scores = [(100, 'perl'), (200, 'tcl'), (400, 'lua'), (500, 'python')]
bisect.insort(scores, (300, 'ruby'))
print(scores)



# heapq module provides functions for implementing heaps based on regular lists.

from heapq import heapify, heappop, heappush
data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
heapify(data)                      # rearrange the list into heap order
heappush(data, -5)                 # add a new entry
b = [heappop(data) for i in range(3)]  # fetch the three smallest entries

print(b)

# Decimal Floating-Point Arithmetic


from decimal import *
round(Decimal('0.70') * Decimal('1.05'), 2)

b = round(.70 * 1.05, 2)

print(b)


Decimal('1.00') % Decimal('.10')

a = 1.00 % 0.10 
print(a)


sum([Decimal('0.1')]*10) == Decimal('1.0')

b = 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 == 1.0
print(b)


getcontext().prec = 36
b = Decimal(1) / Decimal(7)

print(b)
