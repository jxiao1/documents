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

http://www.phperz.com/article/15/0901/153299.html


How to install extensions: ``sudo pip install extension-name``.

Flask-Assets
~~~~~~~~~~~~

http://flask-assets.readthedocs.io/en/latest/

Flask-Assets helps you to integrate webassets, which is to merge and compress JavaScript and CSS files.

flask-script
~~~~~~~~~~~~

http://flask-script.readthedocs.io/en/latest/

Start server with some options in command line, such as host/port/debug.

Examples::

    # "from flask_script import Manager" for python3
    from flask.ext.script import Manager
    from project.main import app

    manager = Manager(app)

    manager.run()

flask-bootstrap
~~~~~~~~~~~~~~~

Please refer to the examples here: http://getbootstrap.com

Please extends the bootstrap/base.html, and fill your blocks.

After using flask-bootstrap, you can use bootstrap/wtf.html for extending wtf form automatically.

For example::

    {% import "bootstrap/wtf.html" as wtf %}

    {% block page_content %}
        <div class="page-header">
            <h2>登录</h2>
        </div>
        <div class="col-md-4">
            {{ wtf.quick_form(form) }}
            ...
    </div>
    {% endblock %}


flask-moment
~~~~~~~~~~~~

To handle the date/time issue in flask.

flask-sqlalchemy
~~~~~~~~~~~~~~~~

http://flask-sqlalchemy.pocoo.org/2.1/

Manage database such as MySQL, Postgres, SQLite

Example::

    from flask import Flask
    from flask_sqlalchemy import SQLAlchemy
    from datetime import datetime

    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
    db = SQLAlchemy(app)
    db.create_all()


    class Post(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        title = db.Column(db.String(80))
        body = db.Column(db.Text)
        pub_date = db.Column(db.DateTime)

        category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
        category = db.relationship('Category',
            backref=db.backref('posts', lazy='dynamic'))

        def __init__(self, title, body, category, pub_date=None):
            self.title = title
            self.body = body
            if pub_date is None:
                pub_date = datetime.utcnow()
            self.pub_date = pub_date
            self.category = category

        def __repr__(self):
            return '<Post %r>' % self.title


    class Category(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(50))

        def __init__(self, name):
            self.name = name

        def __repr__(self):
            return '<Category %r>' % self.name


    py = Category('Python')
    p = Post('Hello Python!', 'Python is pretty cool', py)
    db.session.add(py)
    db.session.add(p)
    db.session.commit()

flask-login
~~~~~~~~~~~

https://flask-login.readthedocs.io/en/latest/

Login authentication management, login information can be saved in cookie in browser's access session.


Example::

    from flask_login import LoginManager

    login_manager = LoginManager()
    login_manager.session_protection = 'Strong'
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    #We must provide user_loader callback, too.
    @login_manager.user_loader
    def load_user(user_id):
        return User.get(user_id)

    #Where the User is a special class which must provide four properties or methods.
    # - is_authenticated
    # - is_active
    # - is_anonymous
    # - get_id()
    #To make implementing a user class easier, you can inherit from UserMixin,
    #which provides default implementations for all of these properties or methods.
    class User(UserMixin, db.Model):
        pass

    from flask_login import login_required
    @main.route('/')
    @login_required
    def index():
        return render_template('main/index.html')


flash-wtf
~~~~~~~~~

| http://flask-wtf.readthedocs.io/en/latest/
| https://wtforms.readthedocs.io/en/latest/
|

For create form based on Python language APIs.

flask-httpauth
~~~~~~~~~~~~~~

http://flask-httpauth.readthedocs.io/en/latest/

HTTP authentication for RESTful API via token.

Basic Password Example::

    from flask_httpauth import HTTPBasicAuth
    from flask_restful import Api

    http_auth = HTTPBasicAuth()
    api = Api(prefix='/api/v1.0', decorators=[http_auth.login_required])

    @http_auth.verify_password
    def verify_pw(username, password):
        user = User.query.filter_by(username=username).first()
        if not user or not user.confirmed:
            return False
        return user.verify_password(password)
    
    @http_auth.error_handler
    def auth_error():
        return make_response(401, {'error': 'unauthorized'})

Token Authentication Example::

    # app/models.py
    from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
    from flask import current_app

    class User(UserMixin, db.modle):
            ...

        def generate_auth_token(self, expiration):
            s = Serializer(current_app.config['SECRET_KEY'],
                           expires_in=expiration)
            return s.dumps({'id': self.id}).decode('ascii')

        @staticmethod
        def verify_auth_token(token):
            s = Serializer(current_app.config['SECRET_KEY'])
            try:
                data = s.loads(token)
            except:
                return None
            return User.query.get(data['id'])

    # app/api/authentication.py
    from flask import g
    from ..extensions import http_auth
    from ..database import User
    from ..utils import make_response
    from ..auth.views import auth

    @http_auth.verify_password
    def verify_pw(username_or_token, password):
        if username_or_token == '':
            return False
        if password == '':
            g.current_user = User.verify_auth_token(username_or_token)
            g.token_used = True
            return g.current_user is not None
        user = User.query.filter_by(username=username_or_token).first()
        if not user or not user.confirmed:
            return False
        g.current_user = user
        g.token_used = False
        return user.verify_password(password)
    
    # We can define a '/token' routing in app/blueprint or Api instance.
    @auth.route('/token')
    @http_auth.login_required
    def get_token():
        if g.current_user.is_anonymous or g.token_used:
            return make_response(401, {'error': 'unauthorized'})
        return make_response(200, {
            'token': g.current_user.generate_auth_token(expiration=3600),
            'expiration': 3600})


    # For define /token in Api
    class apiToken(Resource):
        def get(self):
        if g.current_user.is_anonymous or g.token_used:
            return make_response(401, {'error': 'unauthorized'})
        return make_response(200, {
            'token': g.current_user.generate_auth_token(expiration=3600),
            'expiration': 3600})
    api.add_resource(apiToken, '/token')

Need to get token firstly like this::

    curl -s -u admin:admin -H "Content-Type: application/json" \
        http://127.0.0.1:5000/token

And then you can use token for authentication now::

    curl -s -u <TOKEN>: -H "Content-Type: application/json" \
        http://127.0.0.1:5000/api/v1.0/xxx

flask-mail
~~~~~~~~~~

| http://pythonhosted.org/Flask-Mail/
| https://github.com/mattupstate/flask-mail
|

For sending e-mail in flask. Please note that it's not flask-email

Example::

    from flask import Flask
    from flask_mail import Mail, Message
    import os

    app = Flask(__name__)
    app.config.update(
        DEBUG = True,
        MAIL_SERVER='smtp.live.com',
        MAIL_PROT=25,
        MAIL_USE_TLS = True,
        MAIL_USE_SSL = False,
        MAIL_USERNAME = 'username@hotmail.com',
        MAIL_PASSWORD = 'password',
        MAIL_DEBUG = True
    )

    mail = Mail(app)

    subject = 'hello'
    msg = Message(subject,
                  sender='example@example.com',
                  recipients=['example@example.com'])
    msg.body = "This is the content of test email"
    with app.open_resource("./test.jpg") as f:
        msg.attach("image.jpg", "image/jpg", f.read())

    mail.send(msg)

flask-restful
~~~~~~~~~~~~~

| http://flask-restful-cn.readthedocs.io/en/latest/
| http://flask-restful-cn.readthedocs.io/zh/latest/
| http://www.pythondoc.com/Flask-RESTful/quickstart.html
|

Flask-RESTful is an extension for Flask that adds support for quickly building REST APIs.

Example::

    from flask import Flask, request
    from flask.ext.restful import Resource, Api

    app = Flask(__name__)
    api = Api(app)

    todos = {}

    class TodoSimple(Resource):
        def get(self, todo_id):
            return {todo_id: todos[todo_id]}

        def put(self, todo_id):
            todos[todo_id] = request.form['data']
            return {todo_id: todos[todo_id]}

    api.add_resource(TodoSimple, '/<string:todo_id>')

    if __name__ == '__main__':
        app.run(debug=True)

flask-debugtoolbar
~~~~~~~~~~~~~~~~~~

| http://flask-debugtoolbar.readthedocs.io/en/latest/
| https://github.com/mgood/flask-debugtoolbar
| http://www.phperz.com/article/15/0901/153299.html
| 

Example::

    from flask import Flask
    from flask_debugtoolbar import DebugToolbarExtension

    app = Flask(__name__)

    # the toolbar is only enabled in debug mode:
    app.debug = True

    # set a 'SECRET_KEY' to enable the Flask session cookies
    app.config['SECRET_KEY'] = '<replace with a secret key>'

    toolbar = DebugToolbarExtension()
    toolbar.init_app(app)


flask_moment
~~~~~~~~~~~~

Handle the local time

