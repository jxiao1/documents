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


while statement
---------------

Syntax::

    while something:
        ...
    else:
        ...


for statement
-------------

Examples::

    for x in List: ... else: pass
    for  (a, b) in [(1, 2), (3, 4), (5, 6)]: pass

    for line in open('test.txt'): pass    # read one line each time
    for line in open('test.txt').readlines(): pass    # read all into list

    for i in range(0,10, 2):  print L[i]
    for l in L[::2]:  print l       # will copy L[::2] as new list, use more memory than above case.


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

