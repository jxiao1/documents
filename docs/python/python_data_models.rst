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

.. note::

    - The differences between reference and copy
    - See also pickle module


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


Operations supported by string
------------------------------

String is a special kind of sequence, so most of the above sequence operations are valid to string,
such as slicing, '+', '*',  and build-in functions 'len', 'cmp', for example::


    s[::-1]  # reverse the string

    str="This is a string"" and some others together"

    str1 = 'strcat'
    str2 = 'append'
    str1 += str2

    # basestring is the base calse of all string and unicode type:
    # The following way can check whether the it's a string.
    isinstance(myobj, basesring)


Format a string
---------------



**Usage: format_string % tuple/dictionary**
https://docs.python.org/2/library/stdtypes.html#string-formatting

Format string: ``%[[+/-]width][.precision]type``

Examples::

    %s,  %8d, %-16s, %10.2f, %010.2f,  %+5d

    print "My name is %s, age is %d\n" % (name, age) 

    d = {'name': 'Alex', 'age': 42}
    print "Name is %(name)s, age is %d" % d


**Usage: Template()**
https://docs.python.org/2/library/string.html#template-strings

Examples::

    >>> s = Template("My name is $name, age is $age")
    >>> s.substitute(name="John", age=18)  #使用变量赋值
    'My name is John, age is 18'
    >>> d = {'name':'John', 'age':18}
    >>> s.substitute(d)     #使用字典赋值
    'My name is John, age is 18'

**Usage: format()**
https://docs.python.org/2/library/string.html#custom-string-format_string

Examples::

    >>> '{0}, {1}, {2}'.format('arg0', 'arg1', 'arg2')
    'arg0, arg1, arg2'

    >>> '{0}, {arg1}, {arg2}'.format('arg0', arg1='arg1', arg2='arg2')
    'arg0, arg1, arg2'

    >>> '{arg0}, {0}, {arg2}'.format('arg1', arg0='arg0', arg2='arg2')  # named arguments must be at last.
    'arg0, arg1, arg2'

    >>> config['conf0':'arg0', 'conf1':'arg1']
    >>> '{0[conf0]}, {0[conf1]}, {1}'.format(config, 'arg2')
    'arg0, arg1, arg2'

    >>> '|{0[conf0]:>10}|{0[conf1]:<10}|{1:^10}|'.format(config, 'arg2')  # alignment
    '|      arg0|arg1      |   arg2   |'

    >>> '{0:.{1}f}'.format(1/3.0, 4)
    '0.3333'


String related constants
------------------------

https://docs.python.org/2/library/string.html#string-constants

Examples::

    >>> import string
    >>> string.digits
    '0123456789'
    >>> string.ascii_letters
    'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    >>> string.lowercase  # ascii_lowercase
    'abcdefghijklmnopqrstuvwxyz'
    >>> string.uppercase  # ascii_uppercase
    'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    >>> string.printable
    '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c'

Build-in functions for string
-----------------------------

https://docs.python.org/2/library/string.html#string-functions

.. note::
    As string is not changable, so all the return value is the new copy.

    >>> dir(string)
    >>> dir(s)

Build-in Functions::

    S.find(substr, [start, [end]])
    S.rfind(substr, [start, [end]])
    S.index(substr, [start, [end]]) # similar to find, but maybe index exception.
    S.rindex(substr, [start, [end]])
    S.count(substr, [start, [end]])


    S.replace(oldstr, newstr, [count])
    S.strip([chars])
    S.lstrip([chars])
    S.rstrip([chars])
    S.expandtabs([tabsize])

    S.lower()
    S.upper()
    S.swapcase()
    S.capitalize()
    S.title()

    S.partition(substr)
    S.rpartition(substr)
    S.split([sep, [maxsplit]])
    S.rsplit([sep, [maxsplit]])
    S.splitlines([keepends])
    S.join(sequence)

    S.isalnum()
    S.isalpha()
    S.isdigit()
    S.islower()
    S.isupper()
    S.isspace()
    S.istitle()
    S.startswith(prefix [, start, end])
    S.endswith(suffix [, start, end])

    S.center(width[, fillchar])
    S.ljust(width[, fillchar])
    S.rjust(width[, fillchar])
    S.zfill(width)

    S.translate(table[,deletechars])

    S.encode([encoding,[errors]])
    S.decode([encoding,[errors]])

    string.atoi(s[,base])
    string.atol(s[,base])
    string.atof(s[,base])

Examples::

    >>> st = string.maketrans("0123456789", "abcdefghij")
    >>> "001".translate(st)
    'aab'

    allchars = string.maketrans('', '')   # nothing is changed
    keep = 'abcde'
    alldel = allchars.translate(allchars, keep)   # all execpt characters in keep
    s.translater(allchars , alldel)   # all in keep

    >>> se = "007".encode('base64')
    >>> se.decode('base64')
    '007'


re library
----------

https://docs.python.org/2/library/re.html

::

    re.search(pattern, string, flags=0)
    re.match(pattern, string, flags=0)
    re.fullmatch(pattern, string, flags=0)
    re.split(pattern, string, maxsplit=0, flags=0)
    re.findall(pattern, string, flags=0)
    re.finditer(pattern, string, flags=0)
    re.sub(pattern, repl, string, count=0, flags=0)
    re.escape(string)


textwrap module
---------------

https://docs.python.org/3/library/textwrap.html

::

    textwrap.wrap(text, width=70, **kwargs)
    textwrap.fill(text, width=70, **kwargs)
    textwrap.shorten(text, width, **kwargs)
    textwrap.dedent(text)
    textwrap.indent
    class textwrap.TextWrapper(**kwargs)


Sequences type cast
-------------------

Integer to Binary string::

    # Use built-in function bin()
    bin(n)[2:]

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


list to set::

    # unique the list after from list to set and back to list
    list(set(l))


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


Define and use of Enum
----------------------

enum is standard after python 3.4,  for older version, please try "pip install enum".

::

    from enum import Enum, IntEnum, unique
    try:
        @unique
        class WEEKDAY(Enum):
            MON = 1
            TUS = 2
            WEN = 3
            THU = 4
            FRI = 1
    except ValueError as e:
        print(e)
    
    duplicate values found in <enum 'WEEKDAY'>: FRI -> MON
    
    try:
        class Color(IntEnum):
            RED = 0
            GREEN = 1
            BLUE = 'b'
    except ValueError as e:
        print(e)
        
    invalid literal for int() with base 10: 'b'

    red = class(0)
    print(red is Color.R)       # True
    print(red == 0)             # False

