unittest Quickstart
===================

https://docs.python.org/2.7/library/unittest.html

All test case methods must begin with test, and run in the order of name.

Example(test.py)::

    #!/usr/bin/python
    # -*- coding:utf-8 -*-

    import unittest

    class TestStringMethods(unittest.TestCase):  #must based on unitest.TestCase
        def test_upper(self):
            self.assertEqual('foo'.upper(), 'FOO')

        def test_isupper(self):
            self.assertTrue('FOO'.isupper())
            self.assertFalse('Foo'.isupper())

        def test_split(self):
            s = 'hello world'
            self.assertEqual(s.split(), ['hello', 'world'])
            # check that s.split fails when the separator is not a string
            with self.assertRaises(TypeError):
                s.split(2)

    if __name__ == '__main__':   
        #unittest.main()    # run all test cases by default

        #suite =  unittest.TestLoader().loadTestsFromTestCase(TestStringMethods)
        suite = unittest.TestSuite()    # create test suite to test part of the cases
        suite.addTest(TestStringMethods('test_upper'))  
        suite.addTest(TestStringMethods('test_isupper'))  

        unittest.TextTestRunner(verbosity=2).run(suite) 

Run the test case::

    ./test.py
    python -m unittest -v test                     # Run special test module
    python -m unittest -v test.TestStringMethods   # Run special test class in the module
    python -m unittest -v test.TestStringMethods.test_split  #run special test case
    python -m unittest discover ./ "test*.py"      # Discover all test cases.


Important concepts
------------------

test fixture:
    A test fixture represents the preparation needed to perform one or more
    tests, and any associate cleanup actions. This may involve, for example,
    creating temporary or proxy databases, directories, or starting a server
    process.

test case:
    A test case is the smallest unit of testing. It checks for a specific
    response to a particular set of inputs. unittest provides a base class,
    TestCase, which may be used to create new test cases.

test suite:
    A test suite is a collection of test cases, test suites, or both.
    It is used to aggregate tests that should be executed together.

test runner:
    A test runner is a component which orchestrates the execution of tests and
    provides the outcome to the user. The runner may use a graphical interface,
    a textual interface, or return a special value to indicate the results of
    executing the tests. 


Fixtures
--------
setUp/tearDown() for test case level
setUpClass()/tearDownClass  for class level, need the `@classmethod` decorator.
setUpModule()/tearDownModule() for module level


Skip/ExpectFaiure
-----------------

The following decorators implement test skipping and expected failures:

**@unittest.skip(reason)**:
Unconditionally skip the decorated test. reason should describe why the test is being skipped.

**@unittest.skipIf(condition, reason)**:
Skip the decorated test if condition is true.

**@unittest.skipUnless(condition, reason)**:
Skip the decorated test unless condition is true.

**@unittest.expectedFailure()**:
Mark the test as an expected failure. If the test fails when run, the test is not counted as a failure.

Skipped tests will not have setUp() or tearDown() run around them.
Skipped classes will not have setUpClass() or tearDownClass() run.


Asserts
-------

=============================== ==============================================
Method                          Checks that
=============================== ==============================================
assertEqual(a, b)               a == b   
assertNotEqual(a, b)            a != b   
assertTrue(x)                   bool(x) is True          
assertFalse(x)                  bool(x) is False         
assertIs(a, b)                  a is b
assertIsNot(a, b)               a is not b
assertIsNone(x)                 x is None
assertIsNotNone(x)              x is not None
assertIn(a, b)                  a in b
assertNotIn(a, b)               a not in b
assertIsInstance(a, b)          isinstance(a, b)
assertNotIsInstance(a, b)       not isinstance(a, b)
assertAlmostEqual(a, b)         round(a-b, 7) == 0     
assertNotAlmostEqual(a, b)      round(a-b, 7) != 0      
assertGreater(a, b)             a > b
assertGreaterEqual(a, b)        a >= b
assertLess(a, b)                a < b
assertLessEqual(a, b)           a <= b
assertRegexpMatches(s, r)       r.search(s)
assertNotRegexpMatches(s, r)    not r.search(s)
assertItemsEqual(a, b)          sorted(a) == sorted(b)
assertDictContainsSubset(a, b)  all the key/value pairs in a exist in b
=============================== ==============================================

