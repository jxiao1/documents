Python Data Modules
===================

Introduction
------------
Objects are Python’s abstraction for data. All data in a Python program
is represented by objects or by relations between objects.

Data Modules:
    number, string, sequence, mapping(dictionary), set

Build-in Sequences:
    list, tuple, string, unicode, buffer, xrange

The start index for all Sequences is 0, and -1 is means the last one.

Immutable sequences: string, unicode, tuple
Mutable sequences: list, byte array, 

(1, ) # If there is only one item in the tuple

The key of dictionary must can not be changed, for example: ``int, float, string, tuple``.
But the value of dictionary can be any data type.

.. seealso:: pickle module

.. note:: The differences between reference and copy


Other operation supported by sequences
--------------------------------------

Slicing::

    >>> i=3
    >>> numbers=[0,1,2,3,4,5,6,7,8,9]
    >>> numbers[i]      # numbers[3] = 3
    3
    >>> numbers[-3]     # numbers[10-3] = numbers[7]
    7
    >>> numbers[3:6]    # from 3 to 6, but not include 6
    [3, 4, 5]
    >>> numbers[-3:-1]  # from -3 to -1, the same as numbers[7:9]
    [7, 8]
    >>> numbers[3:]     # from 3 to the end
    [3, 4, 5, 6, 7, 8, 9]
    >>> numbers[:3]     # from the beginning to 3, doesn't include 3
    [0, 1, 2]
    >>> numbers[-3:]    # the last 3 items
    [7, 8, 9]
    >>> numbers[:-3]    # from the beginning to the last third one
    [0, 1, 2, 3, 4, 5, 6]
    >>> numbers[::2]    # step is 2
    [0, 2, 4, 6, 8]
    >>> numbers[::-1]   # step is -1, which means reverse the sequence
    [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    >>> numbers[-1:-10:-1]
    [9, 8, 7, 6, 5, 4, 3, 2, 1]
    >>> numbers[9:0:-1]
    [9, 8, 7, 6, 5, 4, 3, 2, 1]

    >>> numbers=[0,1,2,3,4,5,6,7,8,9]
    >>> numbers[-2:] = [-2, -1]   # change value
    >>> numbers
    [0, 1, 2, 3, 4, 5, 6, 7, -2, -1]

    >>> numbers[2:2] = [20, 21]   # insert
    >>> numbers
    [0, 1, 20, 21, 2, 3, 4, 5, 6, 7, -2, -1]

    >>> numbers[-2:] = [-3, -2, -1]   # change value and append
    >>> numbers
    [0, 1, 20, 21, 2, 3, 4, 5, 6, 7, -3, -2, -1]

    >>> numbers=[0,1,2,3,4,5,6,7,8,9]
    >>> numbers[0:9:2] = [10, 12, 14, 16, 18]   # change value in specified step
    >>> numbers
    [10, 1, 12, 3, 14, 5, 16, 7, 18, 9]

Append::

    >>> numbers=[0,1,2,3,4,5,6,7,8,9]
    >>> numbers + numbers
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

Times::

    >>> numbers=[0,1,2,3,4,5,6,7,8,9]
    >>> numbers * 2
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

Change value::

    >>> numbers[0] = 10
    >>> numbers
    [10, 1, 2, 3, 4, 5, 6, 7, 8, 9]

Check item existence::

    >>> 2 in numbers
    True
    >>> 'P' in "Python"
    True

Build in functions::

    >>> max("Python")
    'y'
    >>> max(numbers)
    9
    >>> min(numbers)
    0
    >>> len(numbers)
    10

Delete::

    >>> del numbers[0]
    >>> numbers
    [1, 2, 3, 4, 5, 6, 7, 8, 9]


Sequences type cast
-------------------

Sting to list::

    >>> list("Python")
    ['P', 'y', 't', 'h', 'o', 'n']

String to tuple::

    >>> tuple("Python")
    ('P', 'y', 't', 'h', 'o', 'n')

List to string::

    # Items for join function must be strings or characers
    >>> ''.join(['P', 'y', 't', 'h', 'o', 'n'])
    'Python'


List build-in functions
-----------------------

append::

    >>> numbers.append(10)
    >>> numbers
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

count::

    >>> numbers[10]=9
    >>> numbers
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 9]
    >>> numbers.count(9)   # count the number of value '9'
    2

extend::

    >>> numbers=[0,1,2,3,4,5,6,7,8,9]
    >>> numbers.extend([10, 11, 12, 13])   # similar to a = a + b
    >>> numbers
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

.. note::
    a + b will not change a，but a.extend(b) will change a

index::

    >>> numbers=[0,1,2,3,4,5,6,7,8,9]
    >>> numbers.index(4)   # find the first one and return the index
    4

insert::

    >>> numbers.insert(4, 41)
    >>> numbers
    [0, 1, 2, 3, 41, 4, 5, 6, 7, 8, 9]

remove::

    >>> numbers.remove(41)   # remove the first one which is found
    >>> numbers
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

pop::

    #pop(n) remove and return the Nth item, default is '-1'
    >>> numbers.pop()
    9
    >>> numbers
    [0, 1, 2, 3, 4, 5, 6, 7, 8]

reverse::

    >>> numbers.reverse()
    >>> numbers
    [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

sort::

    >>> numbers.sort()    # no return value, just change the list.
    >>> numbers
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    >>> name=["John", "Stephanie", "Hasan"]
    >>> name.sort(cmp)    # use build-in function 'cmp' as compare function 
    >>> name
    ['Hasan', 'John', 'Stephanie']

    >>> name.sort(key=len)   # compare the len
    >>> name
    ['John', 'Hasan', 'Stephanie']

    >>> name.sort(key=len, reverse=True)  # sort and also reverse the result
    >>> name
    ['Stephanie', 'Hasan', 'John']


Operations supported by dictionary
----------------------------------

Create::

    d = {'name': 'Alex', 'age': 42}
    d = dict(name='Alex', age=42)
    items = [('name', 'Alex'), ('age', 42)]
    d = dict(items)

Add/Set::

    d['name'] = 'Alisa'
    d['interest'] = 'reading'

Delete::

    del d['interest'] 

Length::

    len(d)

Member check::

    ‘name’  in d    #true

Dictionary to Sting::

    >>> str(d)
    "{'age': 42, 'name': 'Alex'}"

Format by key-value paring in dictionary::

    >>> print "Name is %(name)s, age is %(age)s" % d
    Name is Alex, age is 42


Dictionary build-in functions
-----------------------------

>>> dir(d)
['__class__', '__cmp__', '__contains__', '__delattr__', '__delitem__',
'__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
'__getitem__', '__gt__', '__hash__', '__init__', '__iter__', '__le__',
'__len__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__',
'__repr__', '__setattr__', '__setitem__', '__sizeof__', '__str__',
'__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'has_key', 'items',
'iteritems', 'iterkeys', 'itervalues', 'keys', 'pop', 'popitem', 'setdefault',
'update', 'values', 'viewitems', 'viewkeys', 'viewvalues']

clear::

    d.clear()  # clear all key-value, no return value

copy::

    >>> d['interest'] = ["reading", "chese", "movie"]
    >>> d
    {'age': 42, 'name': 'Alex', 'interest': ['reading', 'chese', 'movie']}
    >>> d1 = d.copy()    # just add the reference
    >>> d1['name'] = 'John'
    >>> d1['interest'].remove('movie')
    >>> d
    {'age': 42, 'name': 'Alex', 'interest': ['reading', 'chese']}
    >>> d1
    {'age': 42, 'name': 'John', 'interest': ['reading', 'chese']}

deepcopy::

    >>> from copy import deepcopy  
    >>> d2 = deepcopy(d) # deepcopy from the copy module
    >>> d2['interest'].append('movie')
    >>> d
    {'age': 42, 'name': 'Alex', 'interest': ['reading', 'chese']}
    >>> d2
    {'age': 42, 'name': 'Alex', 'interest': ['reading', 'chese', 'movie']}

fromkeys::

    >>> d1 = d.fromkeys(['name', 'age'], 'Unknown')  
    >>> d1
    {'age': 'Unknown', 'name': 'Unknown'}

    #fromkeys is a dict class static method
    >>> d1 = dict.fromkeys(['name', 'age'], 'Unknown')
    >>> d1
    {'age': 'Unknown', 'name': 'Unknown'}

get::

    >>> print d.get('name')
    Alex
    >>> print d.get('country')   # return None instead of exception if doesn't exist.
    None
    >>> print d['country']
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    KeyError: 'country'

    >>> print d.get('country', 'Unkown')  # provide a default value
    Unkown

setdefault::

    # It's to get value, but if key doesn't exist, return the default value.
    # Will also add the key and the default value as new key-value paring. 
    >>> d.setdefault('interest', ['reading', 'chese'])
    ['reading', 'chese']

has_key::

    >>> d.has_key('name')
    True

items::

    >>> d.items()   # return the list of all the key-value tuple
    [('age', 42), ('name', 'Alex'), ('interest', ['reading', 'chese'])]

    >>> for key, value in d.items():
    ...    print "[%s]:%s" %(key, value)
    ...
    [age]:42
    [name]:Alex
    [interest]:['reading', 'chese']

iteritems::

    >>> it = d.iteritems()   # return the iterable items
    >>> it
    <dictionary-itemiterator object at 0x7f2382fae2b8>
    >>> list(it)
    [('age', 42), ('name', 'Alex'), ('interest', ['reading', 'chese'])]

keys::

    >>> d.keys()   # return the list of all the keys only
    ['age', 'name', 'interest']

iterkeys::

    >>> d.iterkeys()  # return a iterable keys 
    <dictionary-keyiterator object at 0x7f2382fae310>

values::

    >>> d.values()  # return the list of all the values only
    [42, 'Alex', ['reading', 'chese']]

itervalues::

    >>> d.itervalues() # return the iterable values
    <dictionary-valueiterator object at 0x7f2382fae310>

pop::

    # Remove the key-value specified by this key in the dictionary.
    # And return the value of this key
    >>> d.pop('interest')
    ['reading', 'chese']
    >>> d
    {'age': 42, 'name': 'Alex'}
    
    # provide default return value if key doesn't exist 
    >>> d.pop('interest', 'No this key')  
    'No this key'

popitem::

    # The same as pop, but using a random key instead of specified one
    # Also return the value of this randome key-value paring.
    >>>d.popitem()

update::

    # Update if the same key exist, add new key-value paring if not.
    >>> d1 = {'name': 'John', 'country': 'USA'}
    >>> d.update(d1) 
    >>> d
    {'country': 'USA', 'age': 42, 'name': 'John', 'interest': ['reading', 'chese']}


Operations supported by set
---------------------------
::

    >>> x = set('python')
    >>> y = {'p', 'o', 'i', 'n', 't'}

    >>> x & y
    set(['p', 't', 'o', 'n'])

    >>> x | y
    set(['i', 'h', 'o', 'n', 'p', 't', 'y'])

    >>> x - y
    set(['y', 'h'])

    >>> x ^ y   #differences in x and y
    set(['i', 'h', 'y'])

    >>> s = set()
    >>> s.add('test')
