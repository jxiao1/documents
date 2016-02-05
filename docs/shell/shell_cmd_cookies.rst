Shell Magic Commands
====================

Daily Commands
--------------

#. Run some thing in the background screen session

    ``screen -d -m -S session_name "comman"``

    .. seealso:: ``screen --help`` or ``tmux --help``

#. Run the last command by root account

    ``sudo !!``

#. Go to the last cd history directory.

    ``cd -``

#. Replace in last command and then run.

    ``^old^new``

#. Show ASCII Table

    ``man ascii``

#. find and rm

    ``find ./ -name "xxx.xx" -exec rm -rf {} \;``

#. ssh remote command, no need to copy script to server

    ``ssh user@server bash </path/to/script.sh``


Network Commands
----------------

#. port monitor

    ``netstat -tlnp``

#. Get the external IP of this host

    ``curl ifconfig.me``
