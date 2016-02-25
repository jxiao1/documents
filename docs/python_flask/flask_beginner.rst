Flask Beginner
==============
Just the records when study the Flask docs 0.10 here:

http://flask.pocoo.org/docs/0.10/


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
        $ virtualenv venv

    Now, whenever you want to work on a project, you only have to activate
    the corresponding environment:

    ``$ . venv/bin/activate``

flask:

    Now you can just enter the following command to get Flask activated
    in your virtualenv:

    ``(venv) $ pip install Flask``

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
'hello flask!' greeting.


Deploying to a Web Server
-------------------------
|
| `Deploying Flask on Heroku`_
| `Deploying WSGI on dotCloud with Flask-specific notes`_
| `Deploying Flask on Webfaction`_
| `Deploying Flask on Google App Engine`_
| `Sharing your Localhost Server with Localtunnel`_
|
| If you manage your own hosts and would like to host yourself,
| see the chapter on `Deployment Options`_.
|

.. _Deploying Flask on Heroku: https://devcenter.heroku.com/articles/getting-started-with-python#introduction
.. _Deploying WSGI on dotCloud with Flask-specific notes: http://flask.pocoo.org/snippets/48/
.. _Deploying Flask on Webfaction: http://flask.pocoo.org/snippets/65/
.. _Deploying Flask on Google App Engine: https://github.com/kamalgill/flask-appengine-template
.. _Sharing your Localhost Server with Localtunnel: http://flask.pocoo.org/snippets/89/
.. _Deployment Options: http://flask.pocoo.org/docs/0.10/deploying/#Deployment
