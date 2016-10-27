Python Data Analysis
====================

Installations
-------------

Canopy(epdfree)
~~~~~~~~~~~~~~~

http://www.enthought.com

::

    sudo bash ./canopy-1.7.4-rh5-64.sh
    # Agree on the license and select installation directory

    # start
    /home/jxiao1/Canopy/canopy

ipython
~~~~~~~

::

    sudo apt-get install ipython ipython-notebook

    # start
    ipython
    ipython noteboot --pylab=inline


numpy
-----

- https://docs.scipy.org/doc/numpy-1.10.1/contents.html
- http://www.numpy.org/
- https://docs.scipy.org/doc/
- https://docs.scipy.org/doc/numpy-dev/user/quickstart.html

Overview
~~~~~~~~

NumPy’s main object is the homogeneous multidimensional array(class ndarray).
It is a table of elements (usually numbers), all of the same type,
indexed by a tuple of positive integers.
In Numpy dimensions are called axes. The number of axes is rank.

In the below example below, the array has rank 2 (it is 2-dimensional).
The first dimension (axis) has a length of 2, the second dimension has a length of 3.

::
    [[ 1., 0., 0.],
     [ 0., 1., 2.]]


Create ndarray
~~~~~~~~~~~~~~

Examples::

    import numpy as np
    a = np.arange(15).reshape(3, 5)     # arange(0, 15, 1)
    b = np.linspace(0, 2, 9)            # 9 numbers from 0 to 2.0, including 2.0
    c = np.random.random((2,3))         # 2 X 3 array

    a = np.array([2,3,4])
    b = np.array([(1.5,2,3), (4,5,6)])

    np.empty((2,3))                     # value is not initialized, what in memory. 
    np.zeros((3,4))                     # value is initialized to '0'
    np.ones((2,3,4), dtype=np.int16)    # value is initialized to '1'
    np.eye(4)                           # 4x4 array I 

    f= lambda x, y: 10*x+y
    np.fromfunction(f,(5,4),dtype=int)
    Out[176]: 
    array([[ 0,  1,  2,  3],
           [10, 11, 12, 13],
           [20, 21, 22, 23],
           [30, 31, 32, 33],
           [40, 41, 42, 43]])

.. note::
    reshape and slice only return new view of the array, but not copied the data.
    change the new view will change the sharing data buffer. If you want to copy
    data, copy() is required.
    ``d = a.copy()``


Data types
~~~~~~~~~~

https://docs.scipy.org/doc/numpy-1.10.1/user/basics.types.html

dtype is np.float64 in most cases by default.

::

    ============= ============== =======================================================================
    Data type     Character Code Description
    ============= ============== =======================================================================
    object        O              Python Object
    string_       SN             String with fixed length of N, e.g. S10 
    unicode_      UN             Unicode with fixed length of N, e.g. U10
    bool_         ?              Boolean (True or False) stored as a byte
    int8          i1             Byte (-128 to 127)
    int16         i2             Integer (-32768 to 32767)
    int32         i4             Integer (-2147483648 to 2147483647)
    int64         i8             Integer (-9223372036854775808 to 9223372036854775807)
    uint8         u1             Unsigned integer (0 to 255)
    uint16        u2             Unsigned integer (0 to 65535)
    uint32        u4             Unsigned integer (0 to 4294967295)
    uint64        u8             Unsigned integer (0 to 18446744073709551615)
    float16       f2             Half precision float: sign bit, 5 bits exponent, 10 bits mantissa
    float32       f4/f           Single precision float: sign bit, 8 bits exponent, 23 bits mantissa
    float64       f8/d           Double precision float: sign bit, 11 bits exponent, 52 bits mantissa
    float128      f16/d          Extend double precision float.
    complex64     c8             Complex number, represented by two 32-bit floats (real and imaginary)
    complex128    c16            Complex number, represented by two 64-bit floats (real and imaginary)
    complex256    c32            Represented by two 128-bit floats (real and imaginary components)
    ============= ============== =======================================================================

Examples::

    a = np.array([1.0, 2, 3])                   # dtype('float64')
    a = np.array([1.0, 2, 3], dtype=np.int32)   # dtyoe('int32')
    a = a.astype(np.int64)                      # dtype('int64')
    a.astype(int).dtype                         # dtype('int64'),  convert pythyon type to numpy type.
    a.astype('f').dtype                         # dtype('float32'), use the character codes
    

Array Operations
~~~~~~~~~~~~~~~~

- https://docs.scipy.org/doc/numpy-1.10.1/reference/routines.math.html
- https://docs.scipy.org/doc/numpy-1.10.1/reference/routines.logic.html

**basic**::

    a = np.array( [20,30,40,50] )
    b = np.arange( 4 )
    c = a-b
    b**2
    b > 10                              # return the dtype=bool array
    b += a
    a *= 3


**index**::

    a = np.array(12).reshape(4, 3)
    a[0][0]                             # the element at raw 0 column 0
    a[1:3]                              # raw from 1 to 3 (not included)
    a[::-1]                             # raw in inverted sequence
    a[1]                                # the second raw
    a[-1]                               # the last raw
    a[:, 1]                             # column 1 in each raw
    a[1:3, [1, 2]]                      # column 1, 2 in raw 1, 2
    a[1:5:2, ::3]                       # 1:5:2 for raw and ::3 for column

    x = np.arange(10,1,-1)
    x[np.array([3, 3, 1, 8])]           # array([7, 7, 9, 2])

    a_idx = np.array([1, 2, 1])
    a[a_idx]                            # select item at index 1, 2 ,1
    a_idx = np.array([[1, 3], [2, 4]])
    a[a_idx]                            # new array ([[a[1], a[3]], [a[2], a[4]])

    y = np.arange(35).reshape(5,7)
    y[np.array([0,2,4])]                        # array([[ 0,  1,  2,  3,  4,  5,  6],
                                                         [14, 15, 16, 17, 18, 19, 20],
                                                         [28, 29, 30, 31, 32, 33, 34]])
    y[np.array([0,2,4]), np.array([0,1,2])]     # array([ 0, 15, 30])
    y[[0,2,4]][:, [0,1,2]]                      # array([[ 0,  1,  2],
                                                         [14, 15, 16],
                                                         [28, 29, 30]])

    y[y>20]     # array([21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34])
    y[np.array([False, False, False,  True,  True])]  # the raws 3 and 4, which is true

    y[y<10] = 10   # set all elements which are little than 10 to 10

    x = np.arange(30).reshape(2,3,5)
    b = np.array([[True, True, False], [False, True, True]])
    x[b]                                        # raw 0, 1 in x[0], raw 1, 2 in x[1], total 4x5

    y[np.array([0,2,4]),1:3]                    # raw 0, 2, 4 column 1~2

**newaxis**::

    x = np.arange(5)
    xx = x[:,np.newaxis]                # 5x1 array([[0],[1],[2],[3],[4]])
    xy = x[np.newaxis, :]               # 1x5 array([[0, 1, 2, 3, 4]])
    xx + xy                             # 5x5

**functions**::

    #a.ufunc or np.ufunc(a)
    abs
    fabs
    sqrt
    square
    exp
    log/log10/log2
    sign                                # return 1 (>0), 0(=0), -1(<0)
    ceil                                # min integer that >= e for e in elements in a
    floor                               # max integer that <= e for e in elements in a
    rint
    modf
    isnan
    isfinite
    isinf
    cos/sin
    tan
    logical_not

    #np.ufunc(a, b)
    add
    subtract
    multiply
    divide/floor_divide
    power
    maximum, fmax
    minimum, fmin
    mod
    copysign
    greater/greater_equal
    less/less_equal
    equal/not_equal
    logical_and/logical_or
    logical_xor

    # functions for bool
    any()
    all()

    # functions for set
    unique(x)
    intersect1d(x, y)                   # in both x and y
    union1d(x, y)                       # in x or y
    in1d(x, y)                          # bool arrary than x[i] in y
    setdiff1d(x, y)                     # in x and not in y
    setxor1d(x, y)                      # only in x or only in y

    #function for statistics
    a.sum()                             # sum of all values
    a.sum(axis=0)                       # sum of each axis
    a.min()
    a.max()
    a.mean()                            # average
    a.std()     
    a.argmin()                          # index of min
    a.argmax()                          # index of max
    a.cumsum()                          # 累计和
    a.cumprod()                         # 累计积

    # examples
    (a > 0).sum()                       # number of element which is greater than 0
    np.add(a, b)

    for row in b:
    for element in b.flat:
    list(b.flat)
    
    a = np.floor(10*np.random.random((3,4)))
    a.ravel()
    a.reshape(6,-1)     # -1 means automaticall get 12/6 =2
    b1 = np.array([False,True,True])
    a[b1,:]             # a[b1], show second and third raws which is True

    a = np.floor(10*np.random.random((2,12)))
    np.hsplit(a,3)   # Split a into 3
    np.hsplit(a,(3,4))   # Split a after the third and the fourth column

    x = np.arange(0,10,2)                     # x=([0,2,4,6,8])
    y = np.arange(5)                          # y=([0,1,2,3,4])
    m = np.vstack([x,y])                      # m=([[0,2,4,6,8],
                                              #     [0,1,2,3,4]])
    xy = np.hstack([x,y])                     # xy =([0,2,4,6,8,0,1,2,3,4])

    b = np.sort(a)


Data input and output
~~~~~~~~~~~~~~~~~~~~~

https://docs.scipy.org/doc/numpy-1.10.1/reference/routines.io.html

::

    np.save('filename.npy', a)               # save array a as filename.npy dat file
    a = np.load('filename.npy')              # load filename.npy to array a

    np.savez('filename.npz', a=arr_a, b=arr_b)  # save array arr_a and arr_b in one file as filename.npz
    arch = np.load('filename.npy')              # load filename.npz to dictionary {'a': arr_a, 'b': arr_b}

    np.savetxt('filename.txt', a, fmt='%4d', delimiter=' ', newline='\n', header='', footer='')
    a = np.loadtxt('filename.txt', delimiter=',')


Random sampling
~~~~~~~~~~~~~~~

https://docs.scipy.org/doc/numpy-dev/reference/routines.random.html
https://docs.scipy.org/doc/numpy-1.10.1/reference/routines.random.html#simple-random-data

Examples::

    np.random.rand(10)                          # 10 samples in [0, 1)
    np.random.rand(2, 4)                        # 2 X 4 array, values in [0,1)
    np.random.randn(2, 4)                         # Return samples from “standard normal” distribution.
    np.random.randint(0, 10, 10)                # int in [0, 10)
    np.random.random_integers(0, 10, 10)        # int in [0, 10]
    np.random.random(10)                        # floats in [0.0, 1.0)                  
    np.random.choice([1, 2, 3, 4], 10)          # 10 samples in the give array [1, 2, 3, 4]


pandas
------

http://pandas.pydata.org/pandas-docs/stable/index.html


Data Structures
~~~~~~~~~~~~~~~

http://pandas.pydata.org/pandas-docs/stable/dsintro.html

**Series**

Series is similar as the dictionary, but support more operations.


Example::

    # the common import way
    import numpy as np
    import pandas as pd
    from pandas import Series, DataFrame

    pd.Series(np.random.randn(5))
    pd.Series(np.random.randn(5), index=['a', 'b', 'c', 'd', 'e'])

    pd.Series({'a' : 0., 'b' : 1., 'c' : 2.})
    pd.Series(5, index=['a', 'b', 'c', 'd', 'e'])

    # like a ndarray
    s = pd.Series({'a' : 0., 'b' : 1., 'c' : 2.})
    s[0]                # 0.0
    s[1:]               # slice from 1 to end, 'b' and 'c' are left

    s[s > s.median()]   # equal to s[[False, False, True]], only 'c' is left

    s[[0, 0, 1]]        # select 'a', 'a', 'b'
    s[[2, 1]]           # select 'c' and 'b'

    # like a dictionary
    s['a']              # 0.0
    s.get('e', np.nan)  # support get function too.

    np.square(s)        # square for each
    s * 2               # i * 2 for i in s

    s.name = 'something'
    s.rename('otherthing')


**DataFrame**

DataFrame is a 2-dimensional labeled data structure with columns of potentially different types.
You can think of it like a spreadsheet or SQL table, or a dict of Series objects.
It is generally the most commonly used pandas object.
Like Series, DataFrame accepts many different kinds of input:

-  Dict of 1D ndarrays, lists, dicts, or Series
-  2-D numpy.ndarray
-  Structured or record ndarray
-  A Series
-  Another DataFrame

Examples::

    # From dictionary of lists
    #---------------------------------------------------------------------------
    d = {'Column1': [1, 2, 3, 4],
         'Column2': [1., 2., 3., 4.]}
    pd.DataFrame(d, index=['a', 'b', 'c', 'd'])

    Out[51]: 
          Column1  Column2
       a        1      1.0
       b        2      2.0
       c        3      3.0
       d        4      4.0

    pd.DataFrame({'a' : [1, 0, 1], 'b' : [0, 1, 1] }, dtype=bool)
    Out[74]: 
              a      b
       0   True  False
       1  False   True
       2   True   True

    # From ndarrays
    #---------------------------------------------------------------------------
    dates = pd.date_range('2013-01-01', periods=3)
    pd.DataFrame(np.random.randn(3,2), index=dates, columns=list('AB'))
    Out[63]: 
                       A         B
    2013-01-01  1.017122 -0.509179
    2013-01-02 -0.165409 -0.185033
    2013-01-03 -0.108724 -0.775507

    # From dictionary for series
    #---------------------------------------------------------------------------
    d = {'Column1': pd.Series([1., 2., 3.], index=['a', 'b', 'c']),
         'Column2': pd.Series([1., 2., 3., 4.], index=['a', 'b', 'c', 'd'])}
    pd.DataFrame(d)
    
    # Select part of the data, and indexs
    pd.DataFrame(d, index=['c', 'b', 'a'], columns=['Column1', 'Column3'])
    Out[47]: 
          Column1 Column3
       c      3.0     NaN
       b      2.0     NaN
       a      1.0     NaN


    # From dict of objects that can be converted to series-like.
    #---------------------------------------------------------------------------
    In [10]: df2 = pd.DataFrame({ 'A' : 1.,
    ....:                      'B' : pd.Timestamp('20130102'),
    ....:                      'C' : pd.Series(1,index=list(range(4)),dtype='float32'),
    ....:                      'D' : np.array([3] * 4,dtype='int32'),
    ....:                      'E' : pd.Categorical(["test","train","test","train"]),
    ....:                      'F' : 'foo' })
    ....: 

    In [11]: df2
    Out[11]: 
         A          B    C  D      E    F
    0  1.0 2013-01-02  1.0  3   test  foo
    1  1.0 2013-01-02  1.0  3  train  foo
    2  1.0 2013-01-02  1.0  3   test  foo
    3  1.0 2013-01-02  1.0  3  train  foo

    #From structured or record array
    #---------------------------------------------------------------------------
    data = np.zeros((2,), dtype=[('A', 'i4'),('B', 'f4'),('C', 'a10')])
    data[:] = [(1,2.,'Hello'), (2,3.,"World")]

    pd.DataFrame(data)
    Out[44]: 
          A    B      C
       0  1  2.0  Hello
       1  2  3.0  World

    pd.DataFrame(data, index=['first', 'second'])
    Out[45]: 
               A    B      C
       first   1  2.0  Hello
       second  2  3.0  World

    pd.DataFrame(data, columns=['C', 'A'])
    Out[46]: 
              C  A
       0  Hello  1
       1  World  2

    pd.DataFrame.from_records(data, index='C')
    Out[53]: 
              A    B
       C            
       Hello  1  2.0
       World  2  3.0

    #From a list of dicts
    #---------------------------------------------------------------------------
    data2 = [{'a': 1, 'b': 2}, {'a': 5, 'b': 10, 'c': 20}]

    pd.DataFrame(data2, index=['R1', 'R2'])
    Out[48]: 
           a   b     c
       R1  1   2   NaN
       R2  5  10  20.0


Series Operations
~~~~~~~~~~~~~~~~~

Examples::

    s1 = pd.Series(np.random.randn(4))
    s1[s1>0]

    s1 * 2
    s1 + 5

    s1.index
    s1.values

    s2 = pd.Series(s1.values,index=['norm_'+ str(i) for i in xrange(4)])
    s2['norm_1':'norm_3']       # raws from 'norm_1' to 'norm_3' (included)
    s2[['norm_1','norm_3']]     # raws 'norm_1' and 'norm_3'

    data = pd.Series([1, 2.1, np.nan, None, '', 0])
    data.isnull()       # only np.nan and None is null.


DataFrame Operations
~~~~~~~~~~~~~~~~~~~~

**Indexing/Selection**::

    df['A']
    df[['A', 'B']]
    df[0:3]

    df.loc['bar':'kar']
    df.loc['2013-01-03', 'A']
    df.loc['2013-01-03':'2013-01-06', ['A', 'B']]
    
    df.iloc[1,1]
    df.iloc[3:5,0:2]
    df.iloc[[1,2,4],[0,2]]
    df.iloc[:,1:3]

    df.ix('2013-01-03', 'A')
    df.at[dates[0],'A']
    df.iat[1,1]

    df[df.A > 0]
    df.loc[(df.A > 0) & (df.C >0), 'B']

    crit1 = df.A > 0
    crit2 = df.B > 0
    crit3 = df.C > 0
    crit = crit1 & crit2 & crit3
    df[crit]

    df[~((df.A <= 6) & (df.index.isin([0,2,4])))]  # ~ means not

=============================== ================ ===========
Operation                       Syntax           Result
=============================== ================ ===========
Select column                   df['col']/df.col Series
Select row by label             df.loc[label]    Series
Select row by integer location  df.iloc[loc]     Series
Slice rows                      df[5:10]         DataFrame
Select Columns                  df[['A', 'B']]   DataFrame
Select rows by boolean vector   df[bool_vec]     DataFrame
=============================== ================ ===========

**Deletion**::

    del df['Column1']

**Addtion**::

    df['Status'] = 'ready'  # Set the whole new column 'Status' to 'ready'

    df['ColumnN'] = df['Column1'] * df['Column2']
    df['ColumnN'] = df['Status'] == 'ready'

    df.insert(1, 'Column1-copy', df['Column1'])

**Copy**::

    df2 = df.copy()

**Data view**::

    df.index
    df.columns
    df.values

    df.head(2)  # first 5 by default
    df.tail(3)  # last 5 by default

    df.describe()  # Quick statistic summary of your data

    df.sort_index(axis=1, ascending=False)
    df.sort_values(by='B')


**Missing Data**

    df1.dropna(how='all', axis=1)
    df1.fillna(value=5, inplace=True)
    df1.fillna({1:10, 2:20})  # 10 for column 1 and 20 for column 2
    pd.isnull(df1)
    pd.notnull(df1)

**Data alignment and arithmetic**::

    df - df.iloc[0]
    df.sub(df.iloc[0], axis=1)

    df.sub(df['A'], axis=0)

    df*5 + 2

    df.T

    np.square(df)
    

**Join**::

    pd.merge(df1, df2, on='key_index')

**Concat**::

    pd.concat(list_of_dfs)

**Append**::

    pd.append(df, df.iloc[3], ignore_index=True)  # Generate new index

**Group**::

    df.groupby('A').sum()

**Sort**::

    df.sort_values(by='A')


**if/then**::

    df.ix[df.A >= 0,'B'] = True; df

    df_mask = pd.DataFrame({'A' : [True] * 4, 'B' : [False] * 4,'C' : [True,False] * 2})
    df.where(df_mask, 1000)   # Set all 'False' to the value 1000

    # add new column 'result' to show status of value 'A', 'high' if >5, otherwise 'low'.
    df['result'] = np.where(df['A'] > 5,'high','low'); df



Plot in Pandas
~~~~~~~~~~~~~~

Both Series and DataFrame support plot function.

Examples::

    ts = pd.Series(np.random.randn(10, index=pd.date_range('1/1/2000', periods=10))
    ts1.cumsum()  # the sum of all previous values
    ts1.plot()

    df = pd.DataFrame(np.random.randn(10, 4), index=ts.index, columns=['A', 'B', 'C', 'D'])
    df1 = df.cumsum()
    pf = plt.figure()
    pf.legend(loc='best')
    df.plot()
    df1.plot(kind='bar')


Data import and export
~~~~~~~~~~~~~~~~~~~~~~

**csv**::

    pd.read_csv('foo.csv')
    df.to_csv('foo.csv')

**excel**::

    pd.read_excel('foo.xlsx', 'Sheet1', index_col=None, na_values=['NA'])
    df.to_excel('foo.xlsx', sheet_name='Sheet1')

**binary file**::

    # offsets are larger than the size of the type because of struct padding
    names = 'count', 'avg', 'scale'
    formats = 'i4', 'f8', 'f4'
    offsets = 0, 8, 16

    dt = np.dtype({'names': names, 'offsets': offsets, 'formats': formats}, align=True)
    df = pd.DataFrame(np.fromfile('binary.dat', dt))

