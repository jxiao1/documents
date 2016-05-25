unittest WorkFlow
=================

For example, test.py::

    import unittest

    class IntegerArithmeticTestCase(unittest.TestCase):
        def testAdd(self):  ## test method names begin 'test*'
            self.assertEqual((1 + 2), 3)
            self.assertEqual(0 + 1, 1)
        def testMultiply(self):
            self.assertEqual((0 * 10), 0)
            self.assertEqual((5 * 8), 40)

    if __name__ == '__main__':
        unittest.main()

Track the work flow by ``python -mpdb test.py``
The unittest version is V1.0.0 in ubuntu14.04


Import unittest
---------------
Of course, the __init__.py is running when import unittest package.


- from .main import TestProgram, main


unitest subclass
----------------


unittest.main()
---------------
1. Because ``main = TestProgram`` at the end of main.py, so the
unittest.main() is to create instance of clase TestProgram.

2. In the TestProgram __init__() function, ``self.runTests()`` is called.
The default runner is 'TextTestRunner', and run() function of it will be
executed.

3. The startTestRun()(if exists), test() and StopTestRun() (if exists)
functions will be called in order.

result
------

