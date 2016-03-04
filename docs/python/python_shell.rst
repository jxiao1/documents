Python Shell
============

sh
------------
| https://github.com/amoffat/sh
| http://amoffat.github.io/sh/
|

sh (previously pbs) is a full-fledged subprocess interface for Python
that allows you to call any program as if it were a function::

    from sh import ifconfig
    print ifconfig("eth0")

They may be executed on the sh namespace, or imported directly from sh::

    import sh
    print(sh.ifconfig("eth0"))

For commands that have dashes in their names, for example
/usr/bin/google-chrome, substitute the dash for an underscore::

    import sh
    sh.google_chrome("http://google.com")

For commands that take multiple arguments, need to be invoked using
separate string for each argument rather than single string for all:: 

    from sh import ls
    ls("-l", "./")  # ls("-l ./") will not work

For commands with more exotic characters in their names, like .,
or if you just don’t like the “magic”-ness of dynamic lookups,
you may use sh’s Command wrapper and pass in the command name or
the absolute path of the executable::

    import sh
    run = sh.Command("/home/amoffat/run.sh") # Absolute path
    run()
    lscmd = sh.Command("ls")  # Absolute path not needed
    lscmd()
    lscmd('./')

.. note::
    Similarly, sh.Command("ls ./") will not work! Must wrap
    command only and pass parameters later one by one.

Commands support short-form -a and long-form --arg arguments
as keyword arguments::

    # resolves to "curl http://duckduckgo.com/ -o page.html --silent"
    curl("http://duckduckgo.com/", o="page.html", silent=True)

    # or if you prefer not to use keyword arguments, this does the same thing:
    curl("http://duckduckgo.com/", "-o", "page.html", "--silent")

    # resolves to "adduser amoffat --system --shell=/bin/bash --no-create-home"
    adduser("amoffat", system=True, shell="/bin/bash", no_create_home=True)

    # or
    adduser("amoffat", "--system", "--shell", "/bin/bash", "--no-create-home")

Shell style piping is performed using function composition. Just pass one command
as the input to another, and sh will create a pipe between the two::

    # sort this directory by biggest file
    print(sort(du(glob("*"), "-sb"), "-rn"))

    # print(the number of folders and files in /etc
    print(wc(ls("/etc", "-1"), "-l"))


You can redirect the stdin, stdout and stderr streams of a process to a file
or file-like object by the special _in, _out and _err keyword argument::

    ls(_out="files.list")
    ls("nonexistent", _err="error.txt")
    print(tr("[:lower:]", "[:upper:]", _in="sh is awesome")) # SH IS AWESOME

The exit code can be seen through a command’s exit_code property::

    output = ls("/")
    print(output.exit_code) # should be 0


**For other more advance features, please refer to:**
http://amoffat.github.io/sh/


os.system()
-----------
Return 0 for success and others for failure.

test.py::

    import os

    retcode = os.system("cp ./test.py ./test1.py")
    print("retcode is: %d" % retcode);

    retcode = os.system("cp ./not_exist_file.py ./test1.py")
    print("retcode is: %d" % retcode);

$ python ./test.py::

    retcode is: 0
    cp: cannot stat ‘./not_exist_file.py’: No such file or directory
    retcode is: 256


os.popen()
----------
::

    # get the result only
    fouput = os.popen("ls /home/test")
    print fouput.readlines()

    # or use the input only
    finput = os.popen("python TestInput.py", "w")
    finput.write("how are you\n")


subprocess
----------
It's better to use subprocess instead of os.popen() and os.system()
