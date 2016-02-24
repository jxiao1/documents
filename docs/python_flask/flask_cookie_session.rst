Flask Cookies
=============

To access cookies you can use the cookies attribute.
To set cookies you can use the set_cookie method of response objects.
The cookies attribute of request objects is a dictionary with all the
cookies the client transmits. If you want to use sessions, do not use
the cookies directly but instead use the Sessions in Flask that add
some security on top of cookies for you.

Reading cookies::

    from flask import request

    @app.route('/')
    def index():
        username = request.cookies.get('username')
        # use cookies.get(key) instead of cookies[key] to not get a
        # KeyError if the cookie is missing.

Storing cookies::

    from flask import make_response

    @app.route('/')
    def index():
        resp = make_response(render_template(...))
        resp.set_cookie('username', 'the username')
        return resp

.. note::

    Cookies are set on response objects. Since you normally just return
    strings from the view functions Flask will convert them into response
    objects for you. If you explicitly want to do that you can use the
    make_response() function and then modify it.

If you want to set a cookie at a point where the response object does not
exist yet. This is possible by utilizing the `Deferred Request Callbacks pattern
<http://flask.pocoo.org/docs/0.10/patterns/deferredcallbacks/#deferred-callbacks>`_.

Flask Sessions
==============
Session allows you to store information specific to a user from one request
to the next. This is implemented on top of cookies for you and signs the
cookies cryptographically. What this means is that the user could look at
the contents of your cookie but not modify it, unless they know the secret
key used for signing.

In order to use sessions you have to set a secret key.


Example
-------

::

    from flask import Flask, session, redirect, url_for, escape, request

    app = Flask(__name__)

    @app.route('/')
    def index():
        if 'username' in session:
            return 'Logged in as %s' % escape(session['username'])
        return 'You are not logged in'

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            session['username'] = request.form['username']
            return redirect(url_for('index'))
        return '''
            <form action="" method="post">
                <p><input type=text name=username>
                <p><input type=submit value=Login>
            </form>
        '''

    @app.route('/logout')
    def logout():
        # remove the username from the session if it's there
        session.pop('username', None)
        return redirect(url_for('index'))

    # set the secret key.  keep this really secret:
    app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

.. note::
    The escape() mentioned here does escaping for you if you are not using
    the template engine (as in this example).


How to generate good secret keys
--------------------------------

The problem with random is that it’s hard to judge what is truly random.
And a secret key should be as random as possible. Your operating system has
ways to generate pretty random stuff based on a cryptographic random generator
which can be used to get such a key:

>>> import os
>>> os.urandom(24)
'\xfd{H\xe5<\x95\xf9\xe3\x96.5\xd1\x01O<!\xd5\xa2\xa0\x9fR"\xa1\xa8'

Just take that thing and copy/paste it into your code and you’re done.

.. note::
    Flask will take the values you put into the session object and serialize
    them into a cookie. If you are finding some values do not persist across
    requests, cookies are indeed enabled, and you are not getting a clear
    error message, check the size of the cookie in your page responses compared
    to the size supported by web browsers.

