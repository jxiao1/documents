Python Functional Programming
=============================

| https://docs.python.org/3.5/howto/functional.html
| http://www.oreilly.com/programming/free/files/functional-programming-python.pdf
|


Built-in Functions
------------------

map/filter/reduce

.. note::
    reduce() is in functools library but not a built-in function in python3.

Example::

    >>> import operator, functools
    >>> functools.reduce(operator.add, [1,2,3,4], 0)
    10


Higher-Order Functions
----------------------

Example::

    def compose(*funcs):
        """Return a new function s.t. compose(f,g,...)(x) == f(g(...(x)))"""
        def inner(data, funcs=funcs):
            result = data
            for f in reversed(funcs):
                result = f(result)
            return result
        return inner

    # >>> times2 = lambda x: x*2
    # >>> minus3 = lambda x: x-3
    # >>> mod6 = lambda x: x%6
    # >>> f = compose(mod6, times2, minus3)
    # >>> all(f(i)==((i-3)*2)%6 for i in range(1000000))
    # True


Module: itertools
-----------------

**Infinite iterators**:

=============== =============== =============================================================
Iterator        Arguments       Example
=============== =============== =============================================================
count()         start, [step]   count(10) --> 10 11 12 13 14 ...
cycle()         p               cycle('ABCD') --> A B C D A B C D ...
repeat()        elem [,n]       repeat(10, 3) --> 10 10 10
=============== =============== =============================================================

**Iterators terminating on the shortest input sequence**:

=============== =============== =============================================================
Iterator        Arguments       Example
=============== =============== =============================================================
accumulate()    p [,func]       accumulate([1,2,3,4,5]) --> 1 3 6 10 15
chain()         p, q, ...       chain('ABC', [1,2,3]) --> A B C 1 2 3
compress()      data, selectors compress('ABCDEF', [1,0,1,0,1,1]) --> A C E F
takewhile()     pred, seq       takewhile(lambda x: x<5, [1,4,6,4,1]) --> 1 4
dropwhile()     pred, seq       dropwhile(lambda x: x<5, [1,4,6,4,1]) --> 6 4 1
filterfalse()   pred, seq       filterfalse(lambda x: x%2, range(10)) --> 0 2 4 6 8
groupby()       iterable[,func] sub-iterators grouped by value of keyfunc(v)     
islice()        seq, ...        islice('ABCDEFG', 2, None) --> C D E F G
starmap()       func, seq       starmap(pow, [(2,5), (3,2), (10,3)]) --> 32 9 1000
tee()           it, n           it1, it2, ... itn splits one iterator into n 
zip_longest()   p, q, ...       zip_longest('ABCD', 'xy', fillvalue='-') --> Ax By C- D-
=============== =============== =============================================================

**Combinatoric generators**:

=============== =============== =============================================================
Iterator        Arguments       Example
=============== =============== =============================================================
product()       p,...[repeat=1] product("ABC", "123") =>(A,1),(A,2),(A,3),(B,1),..(C,2),(C,3)
permutations()  p[, r]          permutations([1,2,3], 3)=>(1,2,3),(1,3,2),(2,1,3),(2,3,1),...
combinations()  p, r            combinations([1,2,3], 2)=>(1,2),(1,3),(2,3)
=============== =============== =============================================================

Example::

    >>> list(itertools.tee([1,2,3,4], 2))
    [<itertools.tee object at 0x7feff9d40128>, <itertools.tee object at 0x7feff9d40170>]
    >>> list(itertools.tee([1,2,3,4], 2)[0])
    [1, 2, 3, 4]
    >>> list(itertools.tee([1,2,3,4], 2)[1])
    [1, 2, 3, 4]

    #----------------------------------------------------------------------

    city_list = [('Decatur', 'AL'), ('Huntsville', 'AL'), ('Selma', 'AL'),
                 ('Anchorage', 'AK'), ('Nome', 'AK'),
                 ('Flagstaff', 'AZ'), ('Phoenix', 'AZ'), ('Tucson', 'AZ')]

    def get_state(city_state):
        return city_state[1]

    itertools.groupby(city_list, get_state) =>
     ('AL', iterator-1),
     ('AK', iterator-2),
     ('AZ', iterator-3), ...

     where
     iterator-1 => ('Decatur', 'AL'), ('Huntsville', 'AL'), ('Selma', 'AL')
     iterator-2 => ('Anchorage', 'AK'), ('Nome', 'AK')
     iterator-3 => ('Flagstaff', 'AZ'), ('Phoenix', 'AZ'), ('Tucson', 'AZ')

    #----------------------------------------------------------------------

    >>> list(itertools.combinations_with_replacement([1,2,3], 2))
    [(1, 1), (1, 2), (1, 3), (2, 2), (2, 3), (3, 3)]

    >>> list(itertools.product("01",repeat=3))
    [('0', '0', '0'), ('0', '0', '1'), ('0', '1', '0'), ('0', '1', '1'),
    ('1', '0', '0'), ('1', '0', '1'), ('1', '1', '0'), ('1', '1', '1')]


Module: functools
-----------------

``@functools.lru_cache(maxsize=128, typed=False)``:

    Decorator to wrap a function with a memoizing callable that saves up to the maxsize most recent calls.

``@functools.total_ordering``:

    Decorator to wrap a class, provide at least __eq__() and one of __lt__(), __le__(), __gt__(), or __ge__().
    The others will be included automatically based on above eq and at least one of others.

``functools.partial(func, *args, **keywords)``:
``functools.partialmethod(func, *args, **keywords)``:

    Return a new partial object which when called will behave like func called
    with the positional arguments args and keyword arguments keywords.

``@functools.singledispatch``:

    See also multipledispatch module

``@functools.wraps(func)``:

    Decorator to wrap the internal function of a decorator.

Example::

    >>> from functools import partial
    >>> basetwo = partial(int, base=2)
    >>> basetwo.__doc__ = 'Convert base 2 string to an int.'
    >>> basetwo('10010')  # => 18


Module: operator
----------------

operators in module operator::

    Syntax                  Function
    a + b                   add(a, b)
    seq1 + seq2             concat(seq1, seq2)
    obj in seq              contains(seq, obj)
    a / b                   truediv(a, b)
    a // b                  floordiv(a, b)
    a & b                   and_(a, b)
    a ^ b                   xor(a, b)
    ~a                      invert(a)
    a | b                   or(a, b)
    a ** b                  pow(a, b)
    a is b                  is(a, b)
    a is not b              is_not(a, b)
    obj[k] = v              setitem(obj, k, v)
    del obj[k]              delitem(obj, k)
    obj[k]                  getitem(obj, k)
    a << b                  lshift(a, b)
    a % b                   mod(a, b)
    a * b                   mul(a, b)
    a @ b                   matmul(a, b)
    -a                      neg(a)
    not a                   not_(a)
    +a                      pos(a)
    a >> b                  rshift(a, b)
    seq[i:j] = values       setitem(seq, slice(i, j), values)
    del seq[i:j]            delitem(seq, slice(i, j))
    seq[i:j]                getitem(seq, slice(i, j))
    s % obj                 mod(s, obj)
    a - b                   sub(a, b)
    obj                     truth(obj)
    a < b                   lt(a, b)
    a <= b                  le(a, b)
    a == b                  eq(a, b)
    a != b                  ne(a, b)
    a >= b                  ge(a, b)
    a > b                   gt(a, b)
    a += b                  a = iadd(a, b)
    a &= b                  a = iand(a, b)
    ListA += listB          ListA = iconcat(ListA, listB)
    a //= b                 a = ifloordiv(a, b)
    a <<= b                 a = ilshift(a, b)
    a %= b                  a = imod(a, b)
    a *= b                  a = imul(a, b)
    a @= b                  a = imatmul(a, b)
    a |= b                  a = ior(a, b)
    a **= b                 a = ipow(a, b)
    a >>= b                 a = irshift(a, b)
    a -= b                  a = isub(a, b)
    a /= b                  a = itruediv(a, b)
    a ^= b                  a = ixor(a, b)


Module: multipledispatch
------------------------

Example::

    from multipledispatch import dispatch

    @dispatch(Rock, Rock)
    def beats3(x, y): return None

    @dispatch(Rock, Paper)
    def beats3(x, y): return y

    @dispatch(Rock, Scissors)
    def beats3(x, y): return x

    @dispatch(Paper, Rock)
    def beats3(x, y): return x

    @dispatch(Paper, Paper)
    def beats3(x, y): return None

    @dispatch(Paper, Scissors)
    def beats3(x, y): return x
    
    @dispatch(Scissors, Rock)
    def beats3(x, y): return y
    
    @dispatch(Scissors, Paper)
    def beats3(x, y): return x
    
    @dispatch(Scissors, Scissors)
    def beats3(x, y): return None
    
    @dispatch(object, object)
    def beats3(x, y):
        if not isinstance(x, (Rock, Paper, Scissors)):
            raise TypeError("Unknown first thing")
        else:
            raise TypeError("Unknown second thing")

    # >>> beats3(rock, paper)
    # <__main__.DuckPaper at 0x103b894a8>
    # >>> beats3(rock, 3)
    # TypeError: Unknown second thing


Module: predicative_dispatch
----------------------------

Example::

    from predicative_dispatch import predicate

    @predicate(lambda x: x < 0, lambda y: True)
    def sign(x, y):
        print("x is negative; y is", y)

    @predicate(lambda x: x == 0, lambda y: True)
    def sign(x, y):
        print("x is zero; y is", y)

    @predicate(lambda x: x > 0, lambda y: True)
    def sign(x, y):
        print("x is positive; y is", y)
