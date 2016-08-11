Python Class
============

Overview
--------

In python, class can be used to create a instance,
But still, it's an object and therefore:

- you can assign it to a variable
- you can copy it
- you can add attributes to it
- you can pass it as a function parameter

Examples::

    >>> class myClass(object):
    ...     pass
    ... 
    >>> type(myClass)
    <type 'type'>
    >>> type(myClass())
    <class '__main__.myClass'>

    >>> print myClass
    <class '__main__.myClass'>
    >>> print myClass()
    <__main__.myClass object at 0x7f5cdbfca210>
    
    >>> new_class = myClass
    >>> print new_class
    <class '__main__.myClass'>


Create Class via type()
-----------------------

Besides define the class by "class" keyword, you can also use type() function::

    var = type(classname, tuple of parent classes, dictionary containing attributes)

For example::

    new_class = type('myClass', (object,), {'test': True})
    >>> type(new_class)
    <type 'type'>
    >>> type(new_class())
    <class '__main__.myClass'>
    >>> print new_class.test
    True

    >>> type(myClass)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      NameError: name 'myClass' is not defined

.. note::
    This is also what python do in the background when you define a class by "class" keyword.


What's metaclasses
------------------
http://stackoverflow.com/questions/100003/what-is-a-metaclass-in-python

We learned that Python classes are objects. Well, metaclasses are what create these objects.
They are the classes' classes, you can picture them this way::

    myClass = metaClass()
    myObject = myClass()

As you know, 'int' is a normal class to create integers, 'str' is a normal class to create strings.
The above "type" is also a class, which is used to create other classes, so, we call it metaclass.

Example for how to define a metaclass (normally, it overwrite __new__ to do some special things)::

    class UpperAttrMetaclass(type):
        def __new__(cls, clsname, bases, dct):
            uppercase_attr = {}
            for name, val in dct.items():
                if not name.startswith('__'):
                    uppercase_attr[name.upper()] = val
                else:
                    uppercase_attr[name] = val
            return super(UpperAttrMetaclass, cls).__new__(cls, clsname, bases, uppercase_attr)


    class myClass(object):
        __metaclass__ = UpperAttrMetaclass  # Use this metaclass instead of default 'type'
        class_attr = "Yes"

    def __init__(self):
        self.inst_attr = "right"
        super(myClass, self).__init__()

    if __name__ == '__main__':
        c = myClass()
        print(c.CLASS_ATTR)      # The class attribute name is changed when call __new__
        print(c.inst_attr)       # instance attribute is not changed because __init__ is called after __new__.


How to search the metaclass:

- If there is __metaclass__ attribute in current class, use it
- Find the first __metaclass__ attribute in parent classes, use it.
- If there is the definiation of __metaclass__ variable in current or imported module(file), use it.
- Otherwise, use type by default.
 
Please note that __metaclass__ can also be a function, for example::

    def upper_attr(future_class_name, future_class_parents, future_class_attr):
        attrs = ((name, value) for name, value in future_class_attr.items() if not name.startswith('__'))

    __metaclass__ = upper_attr  # For all classes in this module which has no their own metaclass.

Most of the time, you don't need metaclass.
Instead of metaclass, you can also use "monkey patching" or "class decorators"


Monkey Patching
---------------

Monkey patching is used to:

- Replace methods/attributes/functions at runtime, e.g. to stub out a function during testing;
- Modify/extend behaviour of a third-party product without maintaining a private copy of the source code;
- Apply a patch at runtime to the objects in memory, instead of the source code on disk;
- Distribute security or behavioural fixes that live alongside the original source code.

Carelessly written or poorly documented monkey patches can lead to problems:

- They can lead to upgrade problems when the patch makes assumptions about the patched object
  that are no longer true; if the product you have changed changes with a new release it may
  very well break your patch. For this reason monkey patches are often made conditional,
  and only applied if appropriate.[4]
- If two modules attempt to monkey patch the same method, one of them (whichever one runs last)
  "wins" and the other patch has no effect, unless monkey patches are written with a pattern
  like alias_method_chain.
- They create a discrepancy between the original source code on disk and the observed behaviour
  that can be very confusing to anyone unaware of the patches' existence.

The following Python example monkey patches the value of Pi from the standard math library::

    >>> import math
    >>> math.pi
    3.141592653589793
    >>> math.pi = 3
    >>> math.pi
    3

Class decorators
----------------

For example::

    class classDecorator(object):
        def __init__(self, func):
       	    super(classDecorator, self).__init__()
       	    self.func = func
       
       	def __call__(self, msg):
       	    print("class decorator ...")
       	    return self.func(msg)

    # echo = classDecorator(echo)
    @classDecorator
    def echo(msg):
        print(msg)

    print(echo)     # echo is a instance of classDecorator now.
    echo('hello')   # equal to classDecorator(echo).__call__('hello')


There is three built-in decorators for class

- @staticmethod
- @classmethod
- @property

Example for @property::

    class Student(object):
        def __init__(self):
            super(Student, self).__init__()
            self._score = 0

        @property               # this define a getter, and also define @score.setter
        def score(self):
            return self._score

        @score.setter           # Optional, proerty will be readonly without this setter.
        def score(self, value):
            if not isinstance(value, int):
                raise ValueError('score must be an integer!')
            if value < 0 or value > 100:
                raise ValueError('score must between 0 ~ 100!')
            self._score = value

    s = Student()
    print s.score       # ==> 0
    s.score = 98
    print s.score       # ==> 98
