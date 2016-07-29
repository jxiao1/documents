Flask Logging
=============
http://flask.pocoo.org/docs/0.10/errorhandling/

Sometimes you might be in a situation where you deal with data that should
be correct, but actually is not. For example you may have some client-side
code that sends an HTTP request to the server but it’s obviously malformed.
This might be caused by a user tampering with the data, or the client code
failing. Most of the time it’s okay to reply with 400 Bad Request in that
situation, but sometimes that won’t do and the code has to continue working.

You may still want to log that something fishy happened. This is where loggers
come in handy. As of Flask 0.3 a logger is preconfigured for you to use.

Here are some example log calls::

    app.logger.debug('A value for debugging')
    app.logger.warning('A warning occurred (%d apples)', 42)
    app.logger.error('An error occurred')

The attached logger is a standard logging Logger, so head over to the
official `logging documentation`_ for more information.

.. _logging documentation: https://docs.python.org/2/library/logging.html


Logger handlers
---------------

There are a couple of handlers provided by the logging system out of the box,
but not all of them are useful for basic error logging.
The most interesting are probably the following:
|
|    SMTPhandler         - logs messages by sending out a email
|    FileHandler         - logs messages to a file on the filesystem.
|    RotatingFileHandler - logs messages to a file on the filesystem
|                          and will rotate after a certain number of messages.
|    SysLogHandler       - logs messages to a UNIX syslog.
|


Example codes for SMTPhandler::

    if not app.debug:
        import logging
        from logging.handlers import SMTPHandler
        mail_handler = SMTPHandler('host-ip-or-name',
                                   'from@example.com',
                                   [to-list1@example.com],
                                   'Email-title')
        mail_handler.setLevel(logging.ERROR)
        app.logger.addHandler(mail_handler)

    ...

    app.logger.error('Some content in the E-mail!')


.. note::
    The from address will not be checked, so it doesn't need to be a
    valid address. However, if it's invalid, it can not be replied.

Better format
-------------

Email Format::

    from logging import Formatter
    mail_handler.setFormatter(Formatter('''
    Message type:       %(levelname)s
    Location:           %(pathname)s:%(lineno)d
    Module:             %(module)s
    Function:           %(funcName)s
    Time:               %(asctime)s

    Message:

    %(message)s
    '''))

Log file Format::

    from logging import Formatter
    file_handler.setFormatter(Formatter(
        '%(asctime)s %(levelname)s: %(message)s '
        '[in %(pathname)s:%(lineno)d]'
    ))
