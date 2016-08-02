Python Statements
=================

https://docs.python.org/3/reference/simple_stmts.html

https://docs.python.org/3/reference/compound_stmts.html


Overview
--------

Simple statements:

- Expression statements
- Assignment statements
- The assert statement
- The pass statement
- The del statement
- The return statement
- The yield statement
- The raise statement
- The break statement
- The continue statement
- The import statement
- The global statement
- The nonlocal statement

Compound statements:

- The if statement
- The while statement
- The for statement
- The try statement
- The with statement
- Function definitions
- Class definitions
- Coroutines


Assignment statement
--------------------

All assignment expression will not return value like C language.
There is syntax error in this expression: ``5 == (x = 5)``.

All assignment are reference copy, but not real deep copy. For example::

    >>> L1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> L2 = L1[::2]    # L2 = [0, 2, 4, 6, 8]
    >>> L1[2] = 20      # L1[2] point to reference of int '20', L2 is still not changed.
    >>> L2
    [0, 2, 4, 6, 8]     # L2[1] is still point to int '2'

    >>> L1[2] = [1, 2]
    >>> L2 = L1[::2]    # Both L1[2] and L2[1] point to the refrence of list [1, 2]
    >>> L1[2][0] = 10   # The first value of list [1, 2] is changed to 10
    >>> L1
    [0, 1, [10, 2], 3, 4, 5, 6, 7, 8, 9]
    >>> L2
    [0, [10, 2], 4, 6, 8]  # So both the value in L1 and L2 are changed, because of the same one reference.


Special assignment examples::

    x, y, z = (1, 2, 3)
    a,b,c,d = 'test'
    a, b = ['111', '222']
    a,b = c, d

    [a, b] = [c, d]
    for (a, b, c) in [(1,2,3), (4,5,6)]: pass

    x = y = z = 1

while statement
---------------

Syntax::

    while something:
        ...
    else:
        ...


if statement
------------

Examples::

    if 0<age<10: pass


for statement
-------------

Examples::

    for x in List/Tuple/String: ... else: pass
    for k in Dict: pass

    for  (a, b) in [(1, 2), (3, 4), (5, 6)]: pass

    for line in open('test.txt'): pass    # read one line each time
    for line in open('test.txt').readlines(): pass    # read all into list
    for line in os.popen('ls -1 /'): pass

    for i in range(0,10, 2):  print L[i]
    for l in L[::2]:  print l       # will copy L[::2] as new list, use more memory than above case.

.. note::
    All object with __next__() method is iteriable,  next(o) is equal to o.__next()


with statement
--------------

Syntax::

    with A() as a:
    with A() as a , B() as b:  # Support this after python 3.1

    # will close file automatically
    with open(r'/home/test/test.txt') as myfile:
         for line in myfile:
            print(line)

Any class with __enter__(), __exit__() method can use with/as statement:

- with will call__enter__(), and return to variable behind as.
- __exit() will always be called at the end of the with/as statement.

Example::

    class TraceBlock:
        def message(self, arg):
            print('running %s' %arg)
        def __enter__(self):
            print('starting trace block')
            return self
        def __exit__(self, exc_type, exc_value, exc_tb):
            if exc_type is None:
                print('exit normal')
            else:
                print('exit with execption %s' % exc_type)
            return False

    with TraceBlock() as action:
        action.message('test1')
        print('reached')

    with TraceBlock() as action:
        action.message('test2')
        raise TypeError
        print('not reached')

