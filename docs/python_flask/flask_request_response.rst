Flask Request Object
====================

Overview Example
----------------

::

    from flask import request

    @app.route('/login', methods=['POST', 'GET'])
    def login():
        error = None

        if request.method == 'POST':
            if valid_login(request.form['username'],
                           request.form['password']):
                return log_the_user_in(request.form['username'])
            else:
                error = 'Invalid username/password'

        # the code below is executed if the request method
        # was GET or the credentials were invalid
        return render_template('login.html', error=error)


Get the args in the URL
-----------------------
To access parameters submitted in the URL (?key=value)::

    searchword = request.args.get('key', '')


Callback Functions
------------------
|
| @app.before_request
| @app.after_request
| @app.teardown_request
| 


Flask Response Object
=====================
The return value from a view function is automatically converted into
a response object for you. If the return value is a string it’s converted
into a response object with the string as response body, an 200 OK error
code and a text/html mimetype.

The logic that Flask applies to converting return values into response
objects is as follows:

+ If a response object of the correct type is returned it’s directly returned
  from the view.
+ If it’s a string, a response object is created with that data and the default
  parameters.
+ If a tuple is returned the items in the tuple can provide extra information.
  Such tuples have to be in the form (response, status, headers) where at least
  one item has to be in the tuple. The status value will override the status
  code and headers can be a list or dictionary of additional header values.
+ If none of that works, Flask will assume the return value is a valid WSGI
  application and convert that into a response object.

If you want to get hold of the resulting response object inside the view,
you can use the make_response() function. Imagine you have a view like this::

    @app.errorhandler(404)
    def not_found(error):
        return render_template('error.html'), 404

You just need to wrap the return expression with make_response() and
get the response object to modify it, then return it::

    @app.errorhandler(404)
    def not_found(error):
        resp = make_response(render_template('error.html'), 404)
        resp.headers['X-Something'] = 'A value'
        return resp


