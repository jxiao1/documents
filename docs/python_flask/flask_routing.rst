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
A Blueprint object works similarly to a Flask application object,
but it is not actually an application. It is a set of operations
which can be registered on an application, even multiple times.
We can group views and resources in many subclass blueprint and
flexibly register them to application later.

Basic example
-------------
::

    from flask import Blueprint, render_template, abort
    from jinja2 import TemplateNotFound

    simple_page = Blueprint('simple_page', __name__,
                            template_folder='templates')

    @simple_page.route('/', defaults={'page': 'index'})
    @simple_page.route('/<page>')
    def show(page):
        try:
            return render_template('pages/%s.html' % page)
        except TemplateNotFound:
            abort(404)


Registering Blueprints
----------------------
::

    from flask import Flask
    from yourapplication.simple_page import simple_page

    app = Flask(__name__)
    app.register_blueprint(simple_page)

If you check the rules registered on the application, you will find these::

    [<Rule '/static/<filename>' (HEAD, OPTIONS, GET) -> static>,
     <Rule '/<page>' (HEAD, OPTIONS, GET) -> simple_page.show>,
     <Rule '/' (HEAD, OPTIONS, GET) -> simple_page.show>]

Blueprints however can also be mounted at different locations::

    app.register_blueprint(simple_page, url_prefix='/pages')

And sure enough, these are the generated rules::

    [<Rule '/static/<filename>' (HEAD, OPTIONS, GET) -> static>,
     <Rule '/pages/<page>' (HEAD, OPTIONS, GET) -> simple_page.show>,
     <Rule '/pages/' (HEAD, OPTIONS, GET) -> simple_page.show>]

On top of that you can register blueprints multiple times though not
every blueprint might respond properly to that. In fact it depends on
how the blueprint is implemented if it can be mounted more than once.


Blueprint Resources
-------------------
Sometimes you might want to introduce a blueprint only for the resources.

Like for regular applications, blueprints are considered to be contained
in a folder. While multiple blueprints can originate from the same folder,
it does not have to be the case and it’s usually not recommended.

The folder is inferred from the second argument to Blueprint which is usually
__name__. This argument specifies what logical Python module or package
corresponds to the blueprint. If it points to an actual Python package that
package (which is a folder on the filesystem) is the resource folder. If it’s
a module, the package the module is contained in will be the resource folder.
The *Blueprint.root_path* property show what the resource folder is::

    >>> simple_page.root_path
    '/Users/username/TestProject/yourapplication'

To quickly open sources from this folder you can use the open_resource() function::

    with simple_page.open_resource('static/style.css') as f:
        code = f.read()

Static Files
------------

A blueprint can expose a folder with static files by providing a path to a
folder on the filesystem via the static_folder keyword argument. It can either
be an absolute path or one relative to the folder of the blueprint::

    admin = Blueprint('admin', __name__, static_folder='static')

By default the rightmost part of the path is where it is exposed on the web.
Because the folder is called static here it will be available at the location
of the blueprint + /static. Say the blueprint is registered for /admin the
static folder will be at /admin/static.

The endpoint is named blueprint_name.static so you can generate URLs to
it like you would do to the static folder of the application::

    url_for('admin.static', filename='style.css')

Templates
---------

If you want the blueprint to expose templates you can do that by providing
the template_folder parameter to the Blueprint constructor::

    admin = Blueprint('admin', __name__, template_folder='templates')

As for static files, the path can be absolute or relative to the blueprint
resource folder. The template folder is added to the searchpath of templates
but with a lower priority than the actual application’s template folder.
That way you can easily override templates that a blueprint provides in the
actual application.

So if you have a blueprint in the folder yourapplication/admin and you want to
render the template 'admin/index.html' and you have provided templates as a
template_folder you will have to create a file like this:
yourapplication/admin/templates/admin/index.html.

Building URLs
-------------
If you want to link from one page to another you can use the url_for() function
just like you normally would do just that you prefix the URL endpoint with the
name of the blueprint and a dot (.)::

    url_for('admin.index')

Additionally if you are in a view function of a blueprint or a rendered template
and you want to link to another endpoint of the same blueprint, you can use
relative redirects by prefixing the endpoint with a dot only::

    url_for('.index')

This will link to admin.index for instance in case the current request
was dispatched to any other admin blueprint endpoint.

