Flask Beginner
==============

| Flask docs 0.10 here: http://flask.pocoo.org/docs/0.10/
| Flask docs in CN: http://dormousehole.readthedocs.io
| Flask on OSChian: http://www.oschina.net/translate/tag/flask
| Flask mega tutorial: http://www.pythondoc.com/flask-mega-tutorial/index.html
| Explore Flask: http://www.pythondoc.com/exploreflask/index.html
| Resources and plugins: https://github.com/humiaozuzu/awesome-flask
| 
| Other references: http://www.jeffknupp.com/blog/2014/03/03/what-is-a-web-framework/
| See also other documents(CN) here: http://www.pythondoc.com/
|
| https://github.com/realpython/discover-flask
| http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world
|

Installation
------------
http://flask.pocoo.org/docs/0.10/installation/#installation

virtualenv:

    Virtualenv enables multiple side-by-side installations of Python,
    one for each project. It doesn’t actually install separate copies
    of Python, but it does provide a clever way to keep different project
    environments isolated.

    ``$ sudo easy_install virtualenv``

    Or even better:

    ``$ sudo pip install virtualenv``

    Maybe it’s even in your package manager. If you use Ubuntu, try:

    ``$ sudo apt-get install python-virtualenv``

    Once you have virtualenv installed, just fire up a shell and create
    your own environment::

        $ mkdir myproject
        $ cd myproject
        $ virtualenv [--python=python3] venv  # default is python2

    Now, whenever you want to work on a project, you only have to activate
    the corresponding environment:

    ``$ . venv/bin/activate`` or ``$ source venv/bin/activate``

    After all, if you want to exit the virtualenv:

    ``(venv) $ deactivate``

flask:

    Now you can just enter the following command to get Flask activated
    in your virtualenv:

    ``(venv) $ pip install flask jinja2 werkzeug``

    Any time, you can generate the required packages list like this:

    ``(venv) $ pip freeze > ./requirements.txt``

    And set up the same virtual environment in other place list this:

    ``(venv) $ pip install -r requirements.txt``


Quickstart
----------
http://flask.pocoo.org/docs/0.10/quickstart/#quickstart

A minimal Flask application looks something like this:

Create hello.py::

    from flask import Flask                                                                                                                                                                                             
    app = Flask(__name__)

    @app.route('/user/<name>')
    def hello(name):
        return 'Hello %s!' % name

    if __name__ == '__main__':
        # Listen any client host
        # Never use debug mode in product project
        app.run(host='0.0.0.0', debug=True)

.. note::
    If you enable debug support the server will reload itself on code changes,
    and it will also provide you with a helpful debugger if things go wrong.
    Because of security risk, never use debug mode on production machines.

Start the service::

    $ python hello.py >/dev/null 2>&1 &

Now head over to http://127.0.0.1:5000/user/flask, and you should see your
'hello flask!' greeting.  Or in command line mode::

    $ curl -i http://127.0.0.1:5000/user/flask


Project Template
----------------

https://github.com/sloria/cookiecutter-flask


Deploying to a Web Server
-------------------------
|
| `Deploying Flash on Cherrypy WSGI server`_
| `Deploying Flask on pythonanywhere`_
| `Deploying Flask on Heroku`_
| `Deploying WSGI on dotCloud with Flask-specific notes`_
| `Deploying Flask on Webfaction`_
| `Deploying Flask on Google App Engine`_
| `Sharing your Localhost Server with Localtunnel`_
|
| If you manage your own hosts and would like to host yourself,
| see the chapter on `Deployment Options`_.
|

.. _Deploying Flash on Cherrypy WSGI server: http://flask.pocoo.org/snippets/24/
.. _Deploying Flask on pythonanywhere: https://www.pythonanywhere.com/pricing/
.. _Deploying Flask on Heroku: https://devcenter.heroku.com/articles/getting-started-with-python#introduction
.. _Deploying WSGI on dotCloud with Flask-specific notes: http://flask.pocoo.org/snippets/48/
.. _Deploying Flask on Webfaction: http://flask.pocoo.org/snippets/65/
.. _Deploying Flask on Google App Engine: https://github.com/kamalgill/flask-appengine-template
.. _Sharing your Localhost Server with Localtunnel: http://flask.pocoo.org/snippets/89/
.. _Deployment Options: http://flask.pocoo.org/docs/0.10/deploying/#Deployment


Books
-----

Flask Web Development: Developing Web Application with Python

Author: Miguel Grinberg
github: https://github.com/miguelgrinberg
Example source code: https://github.com/miguelgrinberg/flasky
Blog: http://blog.miguelgrinberg.com

