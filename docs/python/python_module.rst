Python Modules
==============

The Paths for Import
--------------------

Specified by sys.path, the default path in order:

1. Current directory
2. PYTHONPATH (path1:path2...)
3. Standard installation directories
4. Specified by xxx.pth file (one line for each path)

Of course, we can append path in to sys.path like this::

    sys.path.append('Path-for-mymoudule')
    import mymodule


How to Import Modules
---------------------

| ``import xxx``:
| ``import xxx, yyy``:
| ``import <package-name>.<module-name>``:

Compile and execute all the code in the module, and import itself like a object into current name space.

| ``import xxx as yyy``:

Same as import, but also rename the module object in current name space.

| ``from xxx import yyy``:

Compile and execute all the code in the module, and only import yyy into current name space.

| ``from xxx import *``:

Compile and execute all the code in the module, and import each in it into current name space.

| ``from xxx import yyy as zzz``:

Same as "from xxx import yyy", but also rename it to "zzz".

| ``from .xxx improt yyy``:
| ``from ..xxx improt yyy``:
| ``from . improt yyy``:
| ``from .. import yyy``:

Require the current module and the "xxx" module are in the same package.


.. note::
    variables/functions start with _X will not be imported by ``from xxx import *``

    When call the properties from outside of class, need to add class name like this '_className__x'.


.. note::
    import requires using module name later, but from import the name directly, must be careful.


.. note::
    import、from can also import pyc, package directory, c module, zip archive.


__init__.py
-----------

All code in __init__.py will be execute when first import the package.

List __all__ in __init__.py defines the module which will be imported when ``from xxx import *``.
Otherwise, you must use 'import' to import the sub modules one by one manually.


Local Import
------------
As the same as def, import and from also are statements, and can be used any where,
such as in if/else,  or inside of a function::

    def square_root(a):
        # This import is into the square_root functions local scope
        import math
        return math.sqrt(a)


Optional Import
---------------

::

    try:
        # Python 2.x
        from urlparse import urljoin
        from urllib2 import urlopen
    except ImportError:
        # Python 3.x
        from urllib.parse import urljoin
        from urllib.request import urlopen
