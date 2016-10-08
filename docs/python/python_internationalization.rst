Python Internationalization
===========================

gettext
-------

Define Messages by _() function::

    """test.py"""
    import gettext
    
    try:
        gettext.translation('myapp', localedir='locale', languages=['zh_CN']).install()
    except:
        _ = lambda s: s
    
    # ...
    print(_('This is a translatable string.'))


Generate the pot file::

    mkdir -p ./locale/zh_CN/LC_MESSAGES/
    xgettext -o locale/zh_CN/LC_MESSAGES/myapp.pot ./test.py


Generate the po and mo files::

    # edit po file via poedit tool.
    sudo apt-get install poedit

    # /usr/bin/poedit
    # create new translation or edit exist po file.

    # add/edit/save
