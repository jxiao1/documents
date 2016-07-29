Python Project
==============

virtualenv
----------

See also: [DOC] "Python Flask" => "Flask Beginner"


Configuration
-------------

#. Use a config.py file or the config module
#. Module "configparser" for ini configuration file
#. Module "json" for json configuration file
#. Module "csv" for csv configuration file
#. Module "xml.etree.ElementTree " for xml configuration file


Unittest
--------

Module "unittest" for unit tests.


Documentation
-------------

Tips:

#. Use some formal template of document
#. Simple sentences
#. One topic for each paragraph
#. More use of present tenses
#. Use real codes as the examples.
#. Good code is always better than many documents.

HowTO:

1. Document project: sphinx + reStructuredText
2. doctest: https://docs.python.org/2/library/doctest.html
3. pydoc: https://docs.python.org/2/library/pydoc.html
4. epydoc tool: http://epydoc.sourceforge.net/

Epydoc is a tool for generating API documentation for Python modules, 
based on their docstrings. For an example of epydoc's output, see the
`API documentation for epydoc itself`_.

A lightweight markup language called epytext can be used to format
docstrings, and to add information about specific fields, such as
parameters and instance variables. Epydoc also understands docstrings
written in reStructuredText_, Javadoc, and plaintext.

.. _API documentation for epydoc itself: http://epydoc.sourceforge.net/api/
.. _reStructuredText: http://epydoc.sourceforge.net/othermarkup.html


License
-------

The lice tool: https://github.com/licenses/lice

::

    lice [opts ...]  ('afl3', 'agpl3', 'apache', 'bsd2', 'bsd3', 'cc0',
    'cc_by', 'cc_by_nc', 'cc_by_nc_nd', 'cc_by_nc_sa', 'cc_by_nd',
    'cc_by_sa', 'cddl', 'epl', 'gpl2', 'gpl3', 'isc', 'lgpl', 'mit',
    'mpl', 'wtfpl', 'zlib')


Package
-------

Module 'setuptools'


Continuous Integration
----------------------

http://buildbot.net/
https://jenkins.io/index.html


Project Template
----------------

https://github.com/audreyr/cookiecutter

