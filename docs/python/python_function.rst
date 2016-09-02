Python Functions
================

Overview
--------

def is a statement, and function itself is a object,
for examples::

    if test-some-thing:
        def func();
            pass

    func1 = lambda x:x+10

    fun_name = func1
    fun_name(args)


Return None by default if there is no return.

LEGB search variable: local def => parent def ... => Global => Build in


Parameters
----------

::

    def func(arg, named_arg=None, *args, **kargs): pass
    func(arg1_value, arg2_value, named_arg1=value1, named_arg2=value2)

    # => arg=arg1_value, named_arg=value1, *args=(arg2_value,),  kargs={named_arg2=value2}


Arguments
---------

::

    def test(a, b):
        print a + ' ' + b

    test(a="test", b="function")

    param = ("Hello", "world")
    test(*param)

    dparam = {'a':"Very", 'b':"happy"}
    test(**dparam)

    test(*['hello', 'world'])  # directly without via a variable


Similar to print function::

    >>> print(*{"a":1, 'b':2, "c":3})  # '*' mean keys only
    b c a
    >>> print(*[1,2,3])
    1 2 3
    >>> print(*{1,2,3})
    1 2 3
    >>> print(*(1,2,3), sep='')
    123


lambda expression
-----------------

::

    func = lambda: arg1, arg2 ... argN: expression using arguments 1~N


Decorator Function
------------------

func = decorator_func(func)
cls  = decorator_func(cls)
func = decorator_cls().__call__(func)
cls  = decorator_cls().__call__(cls)
func = decorator_func(args)(func)   # decorator(args) will return sub decorator_func(func)

Function decorator::

    import time
    import functools

    def timeit(func):
        @functools.wraps(func)
        def wrapper():
            start = time.clock()
            func()
            end =time.clock()
            print 'used:', end - start
            return wrapper

    @timeit
    def foo():
        print 'in foo()'

Class decorator::

    class HTML(object):
    """Baking HTML Tags!"""

        def __init__(self, tag="p"):
            print("LOG: Baking Tag <{}>!".format(tag))
            self.tag = tag

        def __call__(self, func):
            return lambda: "<{0}>{1}</{0}>".format(self.tag, func(), self.tag)

    @HTML("div")
    @HTML("p")
    def body():
        return "Hello"

    print(body())       # HTML("div")__call__((HTML("div")__call__(body)))

    LOG: Baking Tag <div>!
    LOG: Baking Tag <p>!
    <div><p>Hello</p></div>


Buildin Functions
-----------------

https://docs.python.org/2/library/functions.html


Other special Functions
-----------------------

http://pyzh.readthedocs.org/en/latest/python-magic-methods-guide.html
https://github.com/RafeKettler/magicmethods
http://www.rafekettler.com/magicmethods.html

