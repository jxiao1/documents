sphinx
======

- http://sphinx-doc.org/
- http://www.sphinx-doc.org/en/stable/contents.html
- http://www.ibm.com/developerworks/cn/opensource/os-sphinx-documentation/

Install
-------

    - ``$ sudo apt-get install sphinx-common python-sphinx texlive``
    - ``$ sudo pip install recommonmark``
    - ``$ sudo pip install sphinx_rtd_theme``


Quick Start
-----------
#. ``$ sphinx-quickstart``

::

    + *conf.py*: sphinx `configuration file`_
    + *index.rst*: top level document, define project structure
    + *Makefile*: make html/pdf

#. ``$ make html`` or ``$ sphinx-build -b html  ./ ./_build/html``


Configuration
-------------
http://www.sphinx-doc.org/en/stable/config.html


Theme
-----
http://www.sphinx-doc.org/en/stable/theming.html

For example, use the "Read the Docs" theme::

    $ sudo pip install sphinx_rtd_theme

    $ vi conf.py
    html_theme = 'sphinx_rtd_theme'


Document structure
------------------
http://www.sphinx-doc.org/en/stable/markup/toctree.html


Deploy to Read the Docs
-----------------------

http://avnpc.com/pages/writing-best-documentation-by-sphinx-github-readthedocs

http://docs.readthedocs.org/en/latest/getting_started.html

.. note::
    When push to github, let "Read the Docs" updeate automatically:
    github repo page => settings tabpage => Webhooks & Services => Add service => ReadTheDocs => Active


Convert file format
-------------------

http://pandoc.org/

For example, between markdown and reStructureText.


Convert to blog
---------------

http://ablog.readthedocs.io/

