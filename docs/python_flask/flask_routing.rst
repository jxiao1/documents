Flask Routing
=============

::

    @app.route('/')
    def index(): pass

    @app.route('/hello')
    def hello(): pass


Variable in the URL
-------------------

``<variable_name>`` or ``<converter:variable_name>``

=========== ===============================================
Converters   Description
=========== ===============================================
string       accepts any text without a slash (the default)
int          accepts integers
float        like int but for floating point values
path         like the default but also accepts slashes
=========== ===============================================

::

    @app.route('/user/<username>')
    def show_user_profile(username): pass

    @app.route('/post/<int:post_id>')
    def show_post(post_id): pass

    # Support variable and also default value
    @app.route('/hello/')
    @app.route('/hello/<name>')
    def hello(name=None): pass


Trailing slash in the URL
-------------------------
Flask’s URL rules are based on Werkzeug’s routing module.

::

    # '/projects' is redirected to '/projects/'
    @app.route('/projects/')
    def projects(): pass

    # '/about/' will result in 404 error
    @app.route('/about')
    def about(): pass


URL Building
------------
To build a URL to a specific function you can use the url_for() function.
It accepts the name of the function as first argument and a number of keyword
arguments, each corresponding to the variable part of the URL rule.
Unknown variable parts are appended to the URL as query parameters.

Here are some examples::

    from flask import Flask, url_for
    app = Flask(__name__)
    
    @app.route('/')
    def index(): pass

    @app.route('/login')
    def login(): pass

    @app.route('/user/<username>')
    def profile(username): pass

    with app.test_request_context():
        print url_for('index')
        print url_for('login')
        print url_for('login', next='/')
        print url_for('profile', username='John Doe')

The result::

    /
    /login
    /login?next=/
    /user/John%20Doe

.. note::

    The_request_context() method tells Flask to behave as though it is handling a request,
    even though we are interacting with it through a Python shell.
    (see also: http://flask.pocoo.org/docs/0.10/quickstart/#context-locals).


HTTP Methods
------------
By default, a route only answers to GET requests, but that can be changed by providing
the methods argument to the route() decorator.

::

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            do_the_login()
        else:
            show_the_login_form()


Static files
------------
Dynamic web applications also need static files. That’s usually where the CSS
and JavaScript files are coming from. Ideally your web server is configured
to serve them for you, but during development Flask can do that as well.
Just create a folder called static in your package or next to your module
and it will be available at /static on the application.

To generate URLs for static files, use the special 'static' endpoint name:

``url_for('static', filename='style.css')``

The file has to be stored on the filesystem as static/style.css.


Redirects
---------
To redirect a user to another endpoint, use the redirect() function;
to abort a request early with an error code, use the abort() function::

    from flask import abort, redirect, url_for

    @app.route('/')
    def index():
        return redirect(url_for('login'))

    @app.route('/login')
    def login():
        abort(401)
        this_is_never_executed()


Error Pages
-----------
By default a black and white error page is shown for each error code.
You can use the errorhandler() decorator to customize the error page::

    from flask import render_template

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template('page_not_found.html'), 404

.. note::

    The 404 after the render_template() call. This tells Flask that
    the status code of that page should be 404 which means not found.
    By default 200 is assumed which translates to: all went well.


Flask Bluepoint
===============
