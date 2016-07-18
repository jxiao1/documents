jQuery Mobile
=============

http://jquerymobile.com/

Need to import the following files in turn::

    jquery.mobile.css
    jquery.js
    jquery.mobile.js


Hello World Example::

    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Hello</title>
        <link rel="stylesheet" href="../css/themes/default/jquery.mobile-1.4.5.min.css">
        <script src="../js/jquery.js"></script>
        <script src="../js/jquery.mobile-1.4.5.min.js"></script>
    </head>
    <body>
        <div data-role="page">
            <div data-role="header"><h1>Hello</h1></div>
            <div role="main" class="ui-content"><p>Hello World!</p></div>
            <div data-role="footer"><h4>@2016</h4></div>
        </div>
    </body>
    </html>

