Flask Extension
===============
Flask extensions are listed on the `Flask Extension Registry`_ and can be
downloaded with easy_install or pip. If you add a Flask extension as
dependency to your requirements.rst or setup.py file they are usually
installed with a simple command or when your application installs.


Using Extensions
----------------
Extensions typically have documentation that goes along that shows
how to use it. There are no general rules in how extensions are supposed
to behave but they are imported from common locations.

If you have an extension called Flask-Foo or Foo-Flask it will be always
importable from flask.ext.foo:

``from flask.ext import foo``

.. _Flask Extension Registry: http://flask.pocoo.org/extensions/


Popular Extensions
------------------

How to install extensions: ``sudo pip install extension-name``.

**Flask-Assets**:

http://flask-assets.readthedocs.io/en/latest/

Flask-Assets helps you to integrate webassets, which is to merge and compress JavaScript and CSS files.

**Other extensions**:

#. flask-script       # start server with host/port in CLI
#. flask-bootstrap    # bootstrap style templates
#. flask-moment       # For time
#. flash-wtf          # For form
#. flask-sqlalchemy   # Manage database such as MySQL, Postgres, SQLite
#. flask-mail         # For e-mail
#. flask-login        # Login authentication management
#. flask-httpauth     # http authentication
#. flask-restful      # For RESTful API

