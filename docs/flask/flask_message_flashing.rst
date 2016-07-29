Flask Message Flashing
======================
http://flask.pocoo.org/docs/0.10/patterns/flashing/#message-flashing-pattern

Good applications and user interfaces are all about feedback. If the user
does not get enough feedback they will probably end up hating the application.

Flask provides a really simple way to give feedback to a user with the
flashing system. The flashing system basically makes it possible to record a
message at the end of a request and access it (only) on the next request.
This is usually combined with a layout template to expose the message.

To flash a message use the flash() method, to get hold of the messages you
can use get_flashed_messages() which is also available in the templates. 
