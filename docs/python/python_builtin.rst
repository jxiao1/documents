Python Built-in Functions
=========================

https://docs.python.org/2.7/library/functions.html

::

    >>>print dir(__builtins__)  # Or: print dir(sys.modules['__builtin__'])
    ['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BufferError', 'BytesWarning', 'DeprecationWarning', 'EOFError', 'Ellipsis', 'EnvironmentError', 'Exception', 'False', 'FloatingPointError', 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError', 'ImportWarning', 'IndentationError', 'IndexError', 'KeyError', 'KeyboardInterrupt', 'LookupError', 'MemoryError', 'NameError', 'None', 'NotImplemented', 'NotImplementedError', 'OSError', 'OverflowError', 'PendingDeprecationWarning', 'ReferenceError', 'RuntimeError', 'RuntimeWarning', 'StandardError', 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError', 'SystemExit', 'TabError', 'True', 'TypeError', 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning', 'ValueError', 'Warning', 'ZeroDivisionError', '_', '__debug__', '__doc__', '__import__', '__name__', '__package__', 'abs', 'all', 'any', 'apply', 'basestring', 'bin', 'bool', 'buffer', 'bytearray', 'bytes', 'callable', 'chr', 'classmethod', 'cmp', 'coerce', 'compile', 'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'execfile', 'exit', 'file', 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int', 'intern', 'isinstance', 'issubclass', 'iter', 'len', 'license', 'list', 'locals', 'long', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'quit', 'range', 'raw_input', 'reduce', 'reload', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'unichr', 'unicode', 'vars', 'xrange', 'zip']


math
----
::

    abs(x)
    divmod(a, b)
    max()
    min()
    pow(x, y)
    range([start,] stop [,step])   # return list
    xrange([start,] stop [,step])  # iterable
    round(x, [,n])
    sum([item])


logical
-------
::

    all(s)                  # True if all is True
    any(s)                  # True if any is True
    cmp(x, y)
    isinstance(obj, class)  # Trure if obj is a isinstance of class
    sorted()
    reversed(sequence)


conversion
----------
::

    repr(o)
    ascii(x) #python 3
    str()
    bin()
    float()
    hex()
    int()    # equal to math.floor()
    long()
    ord(c)
    chr(i)
    set([item])


I/O
---
::

    input()
    raw_input()
    print()


iteration
---------
::

    enumerate(iterable)

    >>> for i, c in enumerate("Like"):
    ...     print "S[%d]=%c" %(i, c)
    ...
    S[0]=L
    S[1]=i
    S[2]=k
    S[3]=e

    s = 'I like Python'
    >>> reversed(s)
    <reversed object at 0x7f2383001850>
    >>> list(reversed(s))
    ['n', 'o', 'h', 't', 'y', 'P', ' ', 'e', 'k', 'i', 'l', ' ', 'I']
    >>> list(sorted(s))
    [' ', ' ', 'I', 'P', 'e', 'h', 'i', 'k', 'l', 'n', 'o', 't', 'y']


others
------
::

    map(function, sequence, ...)   # list that one to one return after map
    filter(function, sequence)     # list that all ture values
    reduce(function, sequence[, initial])   # final one result after function(lastreturn/initial, next)

    zip(a, b)
    >>> names = ["Alex", "John", "Mike"]
    >>> ages = [15, 36, 42]
    >>> zip(names, ages)
    [('Alex', 15), ('John', 36), ('Mike', 42)]

    unzip()
    >>> zip(*c)   #c=[(1, 4), (2, 5), (3, 6)]
    [(1, 2, 3), (4, 5, 6)]
