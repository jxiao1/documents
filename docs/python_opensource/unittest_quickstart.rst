unittest Quickstart
===================

https://docs.python.org/2.7/library/unittest.html


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
setUpClass()/tearDownClass  for class level
setUpModule()/tearDownModule() for module level
