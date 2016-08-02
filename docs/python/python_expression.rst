Python Expressions and Operators
================================

https://docs.python.org/3/reference/expressions.html

http://www.runoob.com/python/python-operators.html


Overview
--------

Arithmetic conversions:

- If either argument is a complex number, the other is converted to complex;
- otherwise, if either argument is a floating point number, the other is converted to floating point;
- otherwise, both must be integers and no conversion is necessary.


The power operator
Unary arithmetic and bitwise operations
Binary arithmetic operations
Shifting operations
Binary bitwise operations
Comparisons
Boolean operations
Conditional expressions
Lambdas
Expression lists
Evaluation order
Operator precedence


Logical expressions
-------------------

False::

    False None 0 "" () [] {}    

Examples::

    name = input("Please enter your name: ")  or 'Unknown'
    x = A or B or C or default

    x = 1 if 5<6 else 0


List Comprehensions
-------------------

Examples::

    [line.rstrip().replace(' ', '#') for line in open('testfile')]

    >>> [a**2 + b**2 for (a, b) in zip(range(1,5),range(1,5))] 
    [2, 8, 18, 32]
    
    [x[0]**2 + x[1]**2 for x in zip(range(1,5),range(1,5))]  # zip两个序列
    [2, 8, 18, 32]

    [i**2 for i in range(0,5) if i > 2]    # 附带条件判断的

    [a**2 + b**2 for a in range(1,5) for b in range(1,5)]  # 两个序列的全排列组合
    [2, 5, 10, 17, 5, 8, 13, 20, 10, 13, 18, 25, 17, 20, 25, 32]


Dictionary Comprehensions
-------------------------

    # dict([(str(i), i**2) for i in range(0,5)])
    >>> {str(i):i**2 for i in range(0,5)} 
    {'3': 9, '4': 16, '0': 0, '2': 4, '1': 1}


Generator Expression
--------------------

Examples::

    total = sum(num * num for num in xrange(1, 101))

    month_codes = dict((fn(i+1), code)
                        for i, code in enumerate('FGHJKMNQUVXZ')
                        for fn in (int, str))
