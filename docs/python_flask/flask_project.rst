Flask Project
=============

Typical Strucature
------------------

The typical project directory tree::

    .
    ├── app
    │   ├── hello.py
    │   ├── static
    │   └── templates
    ├── config.py
    ├── requirements.txt
    ├── run.py
    ├── tests
    │   └── test_basic.py
    └── venv


Configuration Handling
----------------------
http://flask.pocoo.org/docs/0.10/config/

The config attribute of the Flask object is the place where Flask itself
puts certain configuration values and also where extensions can put their
configuration values. This is also where you can have your own configuration.

The config is a subclass of a dictionary and can be modified just like any dictionary::

    app = Flask(__name__)
    app.config['DEBUG'] = True

Certain configuration values are also forwarded to the Flask object
so you can read and write them from there::

    app.debug = True

To update multiple keys at once you can use the dict.update() method::

    app.config.update(
        DEBUG=True,
        SECRET_KEY='...'
    )

.. note::
    The SERVER_NAME key is used for the subdomain support. Because Flask cannot
    guess the subdomain part without the knowledge of the actual server name,
    this is required if you want to work with subdomains. This is also used for
    the session cookie.

    Please keep in mind that not only Flask has the problem of not knowing what
    subdomains are, your web browser does as well. Most modern web browsers will
    not allow cross-subdomain cookies to be set on a server name without dots in it.
    So if your server name is 'localhost' you will not be able to set a cookie for
    'localhost' and every subdomain of it. Please chose a different server name
    in that case, like 'myapplication.local' and add this name + the subdomains
    you want to use into your host config or setup a local bind.


Configuring from Files
----------------------

Configuration becomes more useful if you can store it in a separate file,
ideally located outside the actual application package. This makes packaging
and distributing your application possible via various package handling tools
(Deploying with Distribute) and finally modifying the configuration file afterwards.

So a common pattern is this::

    app = Flask(__name__)
    app.config.from_object('yourapplication.default_settings')
    app.config.from_envvar('YOURAPPLICATION_SETTINGS')

This first loads the configuration from the yourapplication.default_settings
module and then overrides the values with the contents of the file the
YOURAPPLICATION_SETTINGS environment variable points to. 
This environment variable can be set on Linux or OS X with the export
command in the shell before starting the server::

    $ export YOURAPPLICATION_SETTINGS=/path/to/settings.cfg
    $ python run-app.py
     * Running on http://127.0.0.1:5000/
     * Restarting with reloader...

The configuration files themselves are actual Python files. Only values
in uppercase are actually stored in the config object later on.
So make sure to use uppercase letters for your config keys.

Here is an example of a configuration file::

    # Example configuration
    DEBUG = False
    SECRET_KEY = '?\xbf,\xb4\x8d\xa3"<\x9c\xb0@\x0f5\xab,w\xee\x8d$0\x13\x8b83'

Make sure to load the configuration very early on, so that extensions
have the ability to access the configuration when starting up.
There are other methods on the config object as well to load from individual files. 
For a complete reference, read the `Config`_ object’s documentation.

.. _Config: http://flask.pocoo.org/docs/0.10/api/#flask.Config


Other Examples::

    app.config.from_pyfile('yourconfig.cfg')


    DEBUG = True
    SECRET_KEY = 'development key'
    app.config.from_object(__name__)



Configuration Best Practices
----------------------------
The downside with the approach mentioned earlier is that it makes testing
a little harder. There is no single 100% solution for this problem in general,
but there are a couple of things you can keep in mind to improve that experience:

#. create your application in a function and register blueprints on it.
   That way you can create multiple instances of your application with
   different configurations attached which makes unittesting a lot easier.
   You can use this to pass in configuration as needed.
#. Do not write code that needs the configuration at import time. If you limit
   yourself to request-only accesses to the configuration you can reconfigure
   the object later on as needed.


Development / Production
------------------------
Most applications need more than one configuration. There should be at least
separate configurations for the production server and the one used during development.
The easiest way to handle this is to use a default configuration that is always loaded
and part of the version control, and a separate configuration that overrides the values
as necessary as mentioned in the example above::

    app = Flask(__name__)
    app.config.from_object('yourapplication.default_settings')
    app.config.from_envvar('YOURAPPLICATION_SETTINGS')

Then you just have to add a separate config.py file and 
export YOURAPPLICATION_SETTINGS=/path/to/config.py and you are done.
However there are alternative ways as well. For example you could use imports or subclassing.

An interesting pattern is to use classes and inheritance for configuration::

    class Config(object):
        DEBUG = False
        TESTING = False
        DATABASE_URI = 'sqlite://:memory:'

    class ProductionConfig(Config):
        DATABASE_URI = 'mysql://user@localhost/foo'

    class DevelopmentConfig(Config):
        DEBUG = True

    class TestingConfig(Config):
        TESTING = True

To enable such a config you just have to call into from_object()::

    app.config.from_object('configmodule.ProductionConfig')

There are many different ways and it’s up to you how you want to manage
your configuration files. However here a list of good recommendations:

#.  keep a default configuration in version control repository. 
    Either populate the config with this default configuration or
    import it in your own configuration files before overriding values.
#.  use an environment variable to switch between the configurations.
    You can quickly and easily switch between different configs without
    having to touch the code at all. If you are working often on different
    projects you can even create your own script for sourcing that
    activates a virtualenv and exports the development configuration for you.


Instance Folders
----------------
With Flask 0.8 a new attribute was introduced: Flask.instance_path. It refers
to a new concept called the “instance folder”. The instance folder is designed
to not be under version control and be deployment specific. It’s the perfect
place to drop things that either change at runtime or configuration files.

You can either explicitly provide the path of the instance folder when creating
the Flask application or you can let Flask autodetect the instance folder.
For explicit configuration use the instance_path parameter::

    app = Flask(__name__, instance_path='/path/to/instance/folder')

.. note::
    Please keep in mind that this path must be absolute when provided.

If the instance_path parameter is not provided the following default locations are used::

    Uninstalled module:

    /myapp.py
    /instance

    Uninstalled package:

    /myapp
        /__init__.py
    /instance

    Installed module or package:

    $PREFIX/lib/python2.X/site-packages/myapp
    $PREFIX/var/myapp-instance

.. note::
    $PREFIX is the prefix of your Python installation.
    This can be /usr or the path to your virtualenv.
    You can print the value of sys.prefix to see what the prefix is set to.

Since the config object provided loading of configuration files from
relative filenames we made it possible to change the loading via filenames
to be relative to the instance path if wanted. 
The behavior of relative paths in config files can be flipped between
“relative to the application root” (the default) to “relative to instance folder”
via the instance_relative_config switch to the application constructor::

    app = Flask(__name__, instance_relative_config=True)

Here is a full example of how to configure Flask to preload the config from
a module and then override the config from a file in the config folder::

    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object('yourapplication.default_settings')
    app.config.from_pyfile('application.cfg', silent=True)

The path to the instance folder can be found via the Flask.instance_path.
Flask also provides a shortcut to open a file from the instance folder
with Flask.open_instance_resource().

Example usage for both::

    filename = os.path.join(app.instance_path, 'application.cfg')
    with open(filename) as f:
        config = f.read()

    # or via open_instance_resource:
    with app.open_instance_resource('application.cfg') as f:
        config = f.read()

