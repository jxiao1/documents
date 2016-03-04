Flask Templates
===============
Generating HTML from within Python is not fun, and actually pretty cumbersome
because you have to do the HTML escaping on your own to keep the application
secure. Because of that Flask configures the Jinja2 template engine for you.


Rendering Templates
-------------------
To render a template you can use the render_template() method.
All you have to do is provide the name of the template and the variables
you want to pass to the template engine as keyword arguments.

Here’s a simple example of how to render a template:

::

    from flask import render_template

    @app.route('/hello/')
    @app.route('/hello/<name>')
    def hello(name=None):
        return render_template('hello.html', name=name)

Flask will look for templates in the templates folder. So if your application
is a module, this folder is next to that module, if it’s a package,  it’s
actually inside your package:

Case 1: a module::

    /application.py
    /templates
        /hello.html

Case 2: a package::

    /application
        /__init__.py
        /templates
                /hello.html

Example of the template::

    <!doctype html>
    <title>Hello from Flask</title>
    {% if name %}
    <h1>Hello {{ name }}!</h1>
    {% else %}
    <h1>Hello World!</h1>
    {% endif %}

.. note::

    Inside templates you also have access to the request, session and g objects
    as well as the get_flashed_messages() function.

    Automatic escaping is enabled, so if name contains HTML it will be escaped
    automatically. If you can trust a variable and you know that it will be safe
    HTML you can mark it as safe by using the Markup class or by using the safe
    filter in the template.


Global Variables within templates
---------------------------------
The following global variables are available within Jinja2 templates by default.

*config*:

    The current configuration object (flask.config) This is now always available,
    even in imported templates.

*request*:

    The current request object (flask.request). This variable is unavailable if
    the template was rendered without an active request context.

*session*:

    The current session object (flask.session). This variable is unavailable if
    the template was rendered without an active request context.

*g*:

    The request-bound object for global variables (flask.g). This variable is
    unavailable if the template was rendered without an active request context.

*url_for()*:

    The flask.url_for() function.

*get_flashed_messages()*

    The flask.get_flashed_messages() function.

Context Processors
------------------
To inject new variables automatically into the context of a template,
context processors exist in Flask. Context processors run before the
template is rendered and have the ability to inject new values into
the template context. A context processor is a function that returns
a dictionary. The keys and values of this dictionary are then merged
with the template context, for all templates in the app::

    @app.context_processor
    def inject_user():
        return dict(user=g.user)

The context processor above makes a variable called user available in the
template with the value of g.user. This example is not very interesting
because g is available in templates anyways, but it gives an idea how this works.

Variables are not limited to values; a context processor can also make
functions available to templates::

    @app.context_processor
    def utility_processor():
        def format_price(amount, currency=u'€'):
            return u'{0:.2f}{1}'.format(amount, currency)
        return dict(format_price=format_price)

The context processor above makes the format_price function available to all templates::

    {{ format_price(0.33) }}

You could also build format_price as a template filter, but this demonstrates
how to pass functions in a context processor.


Syntax of Jinja templates
-------------------------
http://jinja.pocoo.org/docs/dev/templates/

The default Jinja delimiters are configured as follows:

- {% ... %} for Statements
- {{ ... }} for Expressions to print to the template output
- {# ... #} for Comments not included in the template output
- #  ... ## for Line Statements

Examples::

    {# join string and variable value to one string  #}
    {{ "Hello " ~ name ~ "!" }} 

Filters
~~~~~~~
http://jinja.pocoo.org/docs/dev/templates/#builtin-filters

Variables can be modified by filters. Filters are separated from the variable
by a pipe symbol (|) and may have optional arguments in parentheses.
Multiple filters can be chained. The output of one filter is applied to the next.

For example, ``{{ name|striptags|title }}`` will remove all HTML Tags
from variable name and title-case the output (title(striptags(name))).

Filters that accept arguments have parentheses around the arguments, just like
a function call. For example: ``{{ listx|join(', ') }}`` will join a list with
commas (str.join(', ', listx)).

If you want to register your own filters in Jinja2 you have two ways to do that.
You can either put them by hand into the jinja_env.filter of the application::

    def reverse_filter(s):
        return s[::-1]
        app.jinja_env.filters['reverse'] = reverse_filter

Or use the template_filter() decorator::

    @app.template_filter('reverse')
    def reverse_filter(s):
        return s[::-1]

List of Popular Builtin Filters: 

==================== ===========================================================
Filter Name          Description
==================== ===========================================================
abs                  Return the absolute value of the argument.
capitalize           The first character will be uppercase, all others lowercase
title                Return a titlecased version of the value.
lower                Convert a value to lowercase.
upper                Convert a value to uppercase.
indent               Return a copy of string each line indented by 4 spaces. 
center               Centers the value in a field of a given width.
trim                 Strip leading and trailing whitespace.
wordwrap             Wrap string, line length is 79 characters by default. 
default              If the value is undefined it will return the default value.
dictsort             Sort a dict and yeild (key, value) pairs. ('for xx in xx')
escape               Convert &, <, >, ‘, and ” in string to HTML-safe sequences.
filesizeformat       Format the value like a ‘human-readable’ file size (13 kB).
first                Return the first item of a sequence.
last                 Return the last item of a sequence.
random               Return a random item from the sequence.
format               ``{{ "%s - %s"|format("Hello?", "Foo!") }}``
groupby              Group items in dict with the same value to a specified key.
int                  Convert the value into an integer.
float                Convert the value into a floating point number.
list                 Convert the value into a list.
string               Make a string unicode if it isn’t already.
join                 Return the concatenation of the strings in the sequence. 
length               Return the number of items of a sequence or mapping.
wordcount            Count the words in that string.
map()                Filte on a sequence of objects or looks up an attribute.
pprint               Pretty print a variable. Useful for debugging.
select               Filters a sequence of objects. {{ numbers|select("odd") }}
selectattr           Filters a sequence of objects by attribute.
reject               Filters a sequence, {{ numbers|reject("odd") }}
rejectattr           Filters a sequence/objects by applying test to an attribute
replace              Return a copy of the value after replaced old by new.
reverse              Reverse the object.
round                Round a given precision. ``{{ 42.55|round}}`` ->43.0
safe                 Safe means this variable will not be escaped.
striptags            Strip XML tags and replace adjacent whitespace by one space
slice                Slice an iterator
sort                 Sort an iterable.
sum                  ``{{ items|sum(attribute='price') }}``
truncate             ``{{ "foo bar baz"|truncate(9, True) }}`` -> "foo ba..."
urlencode            Escape strings for use in URLs (uses UTF-8 encoding).
urlize               Converts URLs in plain text into clickable links.
xmlattr              Create an XML attribute string based on the items in a dict
==================== ===========================================================

Tests
~~~~~
::

    {% if variable is defined %}
        value of variable: {{ variable }}
    {% else %}
        variable is not defined
    {% endif %}

    {% if foo.expression is equalto 42 %}
        the foo attribute evaluates to the constant 42
    {% endif %}

    {{ users|selectattr("email", "equalto", "foo@bar.invalid") }}

List of Builtin Tests

==================== ===========================================================
Test Name            Description
==================== ===========================================================
callable             Return whether the object is callable (has __call__ method)
defined              Return true if the variable is defined.
undefined            Like defined() but the other way round.
divisibleby          Check if a variable is divisible by the specified number.
iterable             Check if it’s possible to iterate over an object.
escaped              Check if the value is escaped.
equalto              Check if an object has the same value as another object.
sameas               Check if the objects points to the same memory address
odd                  Return true if the variable is odd.
even                 Return true if the variable is even.
lower                Return true if the variable is lowercased.
upper                Return true if the variable is uppercased.
mapping              Return true if the object is a mapping (dict etc.).
none                 Return true if the variable is none.
number               Return true if the variable is a number.
sequence             Return true if the variable is a sequence.
string               Return true if the object is a string.
==================== ===========================================================

Template Inheritance
~~~~~~~~~~~~~~~~~~~~

**extends**::

    {% extends "layout/default.html" %}
    {% extends layout_template if layout_template is defined else 'master.html' %}

**include**::

    {% include 'header.html' %}
    Body
    {% include 'footer.html' %}

    {% include "sidebar.html" ignore missing %}
    {% include "sidebar.html" ignore missing with context %}
    {% include "sidebar.html" ignore missing without context %}
    {% include ['page_detailed.html', 'page.html'] %}
    {% include ['special_sidebar.html', 'sidebar.html'] ignore missing %}

**import:**

Imagine we have a helper module that renders forms (called forms.html)::

    {% macro input(name, value='', type='text') -%}
        <input type="{{ type }}" value="{{ value|e }}" name="{{ name }}">
    {%- endmacro %}

    {%- macro textarea(name, value='', rows=10, cols=40) -%}
        <textarea name="{{ name }}" rows="{{ rows }}" cols="{{ cols
            }}">{{ value|e }}</textarea>
    {%- endmacro %}

The easiest and most flexible way to access a template’s variables and macros
is to import the whole template module into a variable::

    {% import 'forms.html' as forms %}
    <dl>
        <dt>Username</dt>
        <dd>{{ forms.input('username') }}</dd>
        <dt>Password</dt>
        <dd>{{ forms.input('password', type='password') }}</dd>
    </dl>
    <p>{{ forms.textarea('comment') }}</p>

You can import specific names from a template into the current namespace::

    {% from 'forms.html' import input as input_field, textarea %}
    <dl>
        <dt>Username</dt>
        <dd>{{ input_field('username') }}</dd>
        <dt>Password</dt>
        <dd>{{ input_field('password', type='password') }}</dd>
    </dl>
    <p>{{ textarea('comment') }}</p>

.. note::
    By default, included templates are passed the current context and
    imported templates are not. The reason for this is that imports,
    unlike includes, are cached; as imports are often used just as a
    module that holds macros.

    This is only the default behaviour, you can change it if you want to::

        {% from 'forms.html' import input with context %}
        {% include 'header.html' without context %}

block
~~~~~
::

    {% block sidebar %}
        {{ super() }}
        {% for item in seq %}
            <li>{% block loop_item scoped %}{{ item }}{% endblock %}</li>
        {% endfor %}
    {% endblock sidebar %}

.. note::
    supper block is to inherit the contents in the pararnt block.

.. note::
    Blocks can be nested for more complex layouts. However, per
    default blocks may not access variables from outer scopes.
    'item' variable is out of item in above case because it defined
    out of the block. 'scoped' is to fix this kind of issue.

macro block
~~~~~~~~~~~
Macros are comparable with functions in regular programming languages.
They are useful to put often used idioms into reusable functions.

Here’s a small example of a macro that renders a form element::

    {% macro input(name, value='', type='text', size=20) -%}
        <input type="{{ type }}" name="{{ name }}" value="{{
            value|e }}" size="{{ size }}">
    {%- endmacro %}

The macro can then be called like a function in the namespace::

    <p>{{ input('username') }}</p>
    <p>{{ input('password', type='password') }}</p>

.. note::
    If the macro was defined in a different template, you have to import it first.

.. note::
    If a macro name starts with an underscore, it’s not can’t be exported/imported.

call block
~~~~~~~~~~
Here’s an example of how a call block can be used with arguments::

    {% macro dump_users(users) -%}
        <ul>
        {%- for user in users %}
            <li><p>{{ user.username|e }}</p>{{ caller(user) }}</li>
        {%- endfor %}
        </ul>
    {%- endmacro %}

    {# define the caller(user) in above macro block #}
    {% call(user) dump_users(list_of_user) %}
        <dl>
            <dl>Realname</dl>
            <dd>{{ user.realname|e }}</dd>
            <dl>Description</dl>
            <dd>{{ user.description }}</dd>
        </dl>
    {% endcall %}

filter block
~~~~~~~~~~~~
Filter sections allow you to apply regular Jinja2 filters on a block
of template data. Just wrap the code in the special filter section::

    {% filter upper %}
        This text becomes uppercase
    {% endfilter %}

assignments block
~~~~~~~~~~~~~~~~~
::

    {% set navigation = [('index.html', 'Index'), ('about.html', 'About')] %}
    {% set key, value = call_something() %}

    {% set navigation %}
        <li><a href="/">Index</a>
        <li><a href="/downloads">Downloads</a>
    {% endset %}

List of Control Structures
~~~~~~~~~~~~~~~~~~~~~~~~~~
**for:**
Loop over each item in a sequence.

Inside of a for-loop block, you can access some special variables:

=============== ============================================================================================
Variable        Description
=============== ============================================================================================
loop.index      The current iteration of the loop. (1 indexed)
loop.index0     The current iteration of the loop. (0 indexed)
loop.revindex   The number of iterations from the end of the loop (1 indexed)
loop.revindex0  The number of iterations from the end of the loop (0 indexed)
loop.first      True if first iteration.
loop.last       True if last iteration.
loop.length     The number of items in the sequence.
loop.cycle      A helper function to cycle between a list of sequences. See the explanation below.
loop.depth      Indicates how deep in deep in a recursive loop the rendering currently is. Starts at level 1
loop.depth0     Indicates how deep in deep in a recursive loop the rendering currently is. Starts at level 0
=============== ============================================================================================

For example::

    {% for user in users %}
      <li>{{ user.username|e }}</li>
    {% endfor %}


    <dl>
    {% for key, value in my_dict.iteritems() %}
        <dt>{{ key|e }}</dt>
        <dd>{{ value|e }}</dd>
    {% endfor %}
    </dl>

    # will get the value 'odd', 'even' in turn.
    {% for row in rows %}
        <li class="{{ loop.cycle('odd', 'even') }}">{{ row }}</li>
    {% endfor %}

    {% for user in users if not user.hidden %}
        <li>{{ user.username|e }}</li>
    {% endfor %}

    {% for user in users %}
        {%- if loop.index >= 10 %}{% break %}{% endif %}
    {%- endfor %}

    {% for user in users %}
        {%- if loop.index is even %}{% continue %}{% endif %}
        ...
    {% endfor %}

.. note::
    Note, however, that Python dicts are not ordered; so you might want to
    either pass a sorted list or a collections.OrderedDict to the template,
    or use the dictsort filter.

.. note::
    Unlike in Python, it’s not possible to break or continue in a loop. You can,
    however, filter the sequence during iteration, which allows you to skip items.

If no iteration took place because the sequence was empty or
the filtering removed all the items from the sequence,
you can render a default block by using else::

    <ul>
    {% for user in users %}
        <li>{{ user.username|e }}</li>
    {% else %}
        <li><em>no users found</em></li>
    {% endfor %}
    </ul>

.. note:: 
    In Python, else blocks are executed whenever the corresponding loop did not
    break. Since Jinja loops cannot break anyway, a slightly different behavior
    of the else keyword was chosen.

**if:**
The if statement in Jinja is comparable with the Python if statement.

For example::

    {% if users %}
    <ul>
    {% for user in users %}
        <li>{{ user.username|e }}</li>
    {% endfor %}
    </ul>
    {% endif %}


    {% if kenny.sick %}
        Kenny is sick.
    {% elif kenny.dead %}
        You killed Kenny!  You bastard!!!
    {% else %}
        Kenny looks okay --- so far
    {% endif %}

autoescape expression
~~~~~~~~~~~~~~~~~~~~~
::

    {% autoescape true %}
    Autoescaping is active within this block
    {% endautoescape %}

With Statement
~~~~~~~~~~~~~~
::

    {% with %}
    {% set foo = 42 %}
    {{ foo }}           foo is 42 here
    {% endwith %}
    foo is not visible here any longer

i18n
~~~~
::

    {% trans book_title=book.title, author=author.name %}
    This is {{ book_title }} by {{ author }}
    {% endtrans %}

    {# `_` is the alias of the gettext function #}
    {{ _('Hello World!') }}
    {{ gettext('Hello %(name)s!', name='World') }}

