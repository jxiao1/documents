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


sudo pip install flask-script       # start server with host/port in CLI
sudo pip install flask-bootstrap    # bootstrap style templates
sudo pip install flask-moment       # For time
sudo pip install flash-wtf          # For form
sudo pip install flask-sqlalchemy   # Manage database such as MySQL, Postgres, SQLite
sudo pip install flask-mail         # For e-mail
sudo pip install flask-login        # Login authentication management
sudo pip install flask-httpauth     # http authentication
sudo pip install flask-restful      # For RESTful API

