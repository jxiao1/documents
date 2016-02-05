
sphinx
======

    - http://sphinx-doc.org/
    - http://www.sphinx-doc.org/en/stable/contents.html


Install
-------

    - ``$ sudo apt-get install sphinx-common python-sphinx``
    - ``$ sudo apt-get install texlive``


Quick Start
-----------
#. ``$ sphinx-quickstart``

    + *conf.py*: sphinx `configuration file`_
    + *index.rst*: top level document, define project structure
    + *Makefile*: make html/pdf

#. ``$ make html`` or::

     $ sphinx-build -b html  ./ ./_build/html

#. sphinx 生成html 文档，以及利用其他插件生成pdf

    http://www.ibm.com/developerworks/cn/opensource/os-sphinx-documentation/

#. 使用Read the Docs主题:
    ``$ sudo pip install sphinx_rtd_theme``

    edit conf.py:
    ``html_theme = 'sphinx_rtd_theme'``

    .. seealso:: http://www.sphinx-doc.org/en/stable/theming.html


#. 托管到Read the Docs：

    + http://avnpc.com/pages/writing-best-documentation-by-sphinx-github-readthedocs
    + http://docs.readthedocs.org/en/latest/getting_started.html

    |
    | Push到github时，让Read the Docs 自动更新:
    | github 的repo页面，选择 settings tabpage，选择
    | Webhooks & Services => Add service => ReadTheDocs => Active

#. markdown/reStructureText等格式转换

    http://pandoc.org/

#. 文档项目结构

    http://www.sphinx-doc.org/en/stable/markup/toctree.html

.. _configuration file: http://www.sphinx-doc.org/en/stable/config.html
