Python Standard Library
=======================


glob
----

The glob module finds all the pathnames matching a specified pattern
according to the rules used by the Unix shell. 

::

    glob.glob('./*.rst')


functools
---------

partial::

    def f(a, b=1):
        return a + b

    f2 = functools.partial(f, 1)
    f2()                # => 2
    f2(2)               # => 3

    blocks = []
    for block in iter(partial(f.read, 32), ''):
        blocks.append(block)

wraps::

    def deco(func):
        @functools.wraps(func)   # will copy __doc__, __name_- and so on
        def wrapper(*args, **kwargs)
            return func(*args, **kwargs)
        return wrapper

functools.total_ordering:

functools.cmp_to_key:


collections
-----------

