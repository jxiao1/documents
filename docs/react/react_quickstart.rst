React Quick Start
=================

| https://facebook.github.io/react/
| https://facebook.github.io/react/docs/getting-started.html
|
| http://reactjs.cn/react/index.html
| http://reactjs.cn/react/docs/getting-started.html
|

Starter Kit
-----------

Download it here:
https://facebook.github.io/react/docs/getting-started.html#starter-pack

Example code::

    <!DOCTYPE html>
    <html>
      <head>
        <meta charset="UTF-8" />
        <title>Hello React!</title>
        <script src="build/react.js"></script>
        <script src="build/react-dom.js"></script>
        <script src="https://unpkg.com/babel-core@5.8.38/browser.min.js"></script>
      </head>
      <body>
        <div id="example"></div>
        <script type="text/babel">  # babel is a javascript compiler which supports JFX.
          ReactDOM.render(
            <h1>Hello, world!</h1>,
            document.getElementById('example')
          );
        </script>
      </body>
    </html> 


Tutorial
--------

Get the source code here:
https://github.com/reactjs/react-tutorial

There are several simple server implementations included. Please start the Flask server like this::

    pip install -r requirements.txt
    PORT=8080 python server.py

And visit http://localhost:8080/. 


JFX Specification
-----------------

JSX is a XML-like syntax extension to ECMAScript without any defined semantics.
Please refer to: https://facebook.github.io/jsx/

