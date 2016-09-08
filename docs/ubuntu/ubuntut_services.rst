Ubuntu Services
===============

Openssh
-------

::

    sudo apt-get install openssh-server
    # Edit the etc/ssh/sshd_config file
    UseDNS no
    GSSAPIAuthentication no

Vnc
---

Set the vnc server password: ``vncpasswd``
Start the vncserver: ``vncserver``
Start the vncviewer: ``vncviewer IP/HOSTNAME:PORTNUM``
Kill the vncserver: ``vncserver -kill :1``

