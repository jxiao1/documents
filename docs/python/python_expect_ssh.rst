Python Expect
=============

pexpect
-------
https://pexpect.readthedocs.org/en/stable/
http://www.bx.psu.edu/~nate/pexpect/pexpect.html

Examples:
http://www.pythonforbeginners.com/systems-programming/how-to-use-the-pexpect-module-in-python


Python SSH
==========

pxssh
-----
https://pexpect.readthedocs.org/en/stable/api/pxssh.html

Example::

    import pxssh
    import getpass
    try:
        s = pxssh.pxssh()
        hostname = raw_input('hostname: ')
        username = raw_input('username: ')
        password = getpass.getpass('password: ')

        s.login (hostname, username, password, original_prompt='[$#>]')

        s.sendline ('uptime')
        s.prompt()
        print s.before

        s.sendline ('ls -l')
        s.prompt()
        print s.before

        s.logout()

    except pxssh.ExceptionPxssh, e:
        print "pxssh failed on login."
        print str(e)


parmmiko
--------

http://www.paramiko.org/


Installation::

    sudo pip install pycrypto
    sudo pip install paramiko

Example::

    import paramiko

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, 22, user, passwd, timeout=7200)
    stdin, stdout, stderr = ssh.exec_command("uptime")
    print(stdout.readlines())
    stdin, stdout, stderr = ssh.exec_command("uname -a")
    print(stdout.readlines())
    ssh.close()


fabric
------

http://www.fabfile.org/

