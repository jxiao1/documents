Linux Systemd
=============
https://www.freedesktop.org/wiki/Software/systemd/
https://en.wikipedia.org/wiki/Systemd
https://github.com/systemd/systemd/blob/master/README

Why systemd
-----------
http://0pointer.de/blog/projects/why.html


Tips And Tricks
---------------

Basic operators::

    $ sudo systemctl start nginx.service
    $ sudo systemctl stop nginx.service
    $ sudo systemctl restart nginx.service
    $ sudo systemctl reload nginx.service
    $ sudo systemctl enable nginx.service
    $ sudo systemctl disable nginx.service

    $ sudo systemctl daemon-reload
    $ systemctl status nginx.service

    $ sudo systemctl poweroff
    $ sudo systemctl reboot

other tools::

    hostnamectl #get/set hostname
    localectl   #get/set local settings, e.g. LANG
    timedatectl #get/set time/date/timezone
        $ sudo timedatectl set-timezone America/New_York
        $ sudo timedatectl set-time YYYY-MM-DD
        $ sudo timedatectl set-time HH:MM:SS

If you only wish to see the journal entries from the current boot::

    $ journalctl -b
    $ journalctl -u nginx.Service

To expand all dependent units recursively::

    systemctl list-dependencies --all nginx.service

Cgroup Tree::

    $ systemd-cgls

Switch the run level::

    $ ln -sf /usr/lib/systemd/system/graphical.target /etc/systemd/system/default.target
    $ ln -sf /usr/lib/systemd/system/multi-user.target /etc/systemd/system/default.target

Unit Dependences::

    $ systemctl show -p "Wants" multi-user.target

    .. note::
        Instead of "Wants" you might also try "WantedBy", "Requires", "RequiredBy",
        "Conflicts", "ConflictedBy", "Before", "After" for the respective types of
        dependencies and their inverse.

Show the main PID::

    systemctl -p MainPID show <service-name>

Mask a service, ensure that service cannot even be started manually anymore::

    $ ln -s /dev/null /etc/systemd/system/ntpd.service
    $ systemctl daemon-reload

You can modify the system state to transition between targets with the isolate option.
This will stop any units that are not tied to the specified target.
Be sure that the target you are isolating does not stop any essential services::

    sudo systemctl isolate multi-user.target

check the boot time::


    $ systemd-analyze                                                                                       
    $ systemd-analyze nginx
    $ systemd-analyze critical-chain
    $ systemd-analyze critical-chain atd.service


Network Target
--------------
https://www.freedesktop.org/wiki/Software/systemd/NetworkTarget/
https://www.freedesktop.org/software/systemd/man/systemd-networkd.service.html


Systemd Units
-------------
service.service, socket.socket, device.device, mount.mount, automount.automount,
swap.swap, target.target, path.path, timer.timer, slice.slice, scope.scope


systemd.unit
~~~~~~~~~~~~
https://www.freedesktop.org/software/systemd/man/systemd.unit.html

[Unit] and [Install] section define the relationship between other units.
[Unit] and [Install] sections configure the common configuration items,
for example dependences, conditions, and other relationship between units.
They are generic sections used in almost all type units.


Each unit may have a type-specific section, e.g. [Service] for a service unit.

Various settings are allowed to be specified more than once, often, multiple settings form a list

If systemd encounters an unknown option, it will write a warning log message
but continue loading the unit. 

If an option or section name is prefixed with X-, it is ignored completely by
systemd. Options within an ignored section do not need the prefix. 
Applications may use this to include additional information in the unit files.

Boolean arguments used in unit files can be written in various formats.
For positive settings the strings 1, yes, true and on are equivalent.
For negative settings, the strings 0, no, false and off are equivalent.

Empty lines and lines starting with # or ; are ignored. This may be used for commenting.
Lines ending in a backslash are concatenated with the following line
while reading and the backslash is replaced by a space character.
This may be used to wrap long lines.

If a unit file is empty (i.e. has the file size 0) or is symlinked to
/dev/null, its configuration will not be loaded and it appears with a
load state of "masked", and cannot be activated. Use this as an effective
way to fully disable a unit, making it impossible to start it even manually.

Unit files are loaded from a set of paths determined during compilation,
described in the two tables below. Unit files found in directories listed
earlier override files with the same name in directories lower in the list::

    /etc/systemd/system     Local configuration
    /run/systemd/system     Runtime units
    /usr/lib/systemd/system Units of installed packages


systemd.service
~~~~~~~~~~~~~~~
https://www.freedesktop.org/software/systemd/man/systemd.service.html

[Service] section configure the service specific configuration options.

Unless DefaultDependencies= is set to false, service units will implicitly
have dependencies of type Requires= and After= on sysinit.target, a dependency
of type After= on basic.target as well as dependencies of type Conflicts= and
Before= on shutdown.target. 

Note that notify type daemon has to support systemd's notification protocol,
else systemd will think the service has not started yet and kill it after a timeout.
(systemd_notify can be sued in script to tell systemd itself is ready.)

systemd.network
~~~~~~~~~~~~~~~
https://www.freedesktop.org/software/systemd/man/systemd.network.html#


systemd.resource-control
~~~~~~~~~~~~~~~~~~~~~~~~
https://www.freedesktop.org/software/systemd/man/systemd.resource-control.html

The resource control configuration options are configured in the [Slice], [Scope],
[Service], [Socket], [Mount], or [Swap] sections, depending on the unit type.


systemd debug
-------------
https://freedesktop.org/wiki/Software/systemd/Debugging/

debug shell
~~~~~~~~~~~
You can enable shell access very early in the startup process to fall back on
and diagnose systemd related boot up issues with various systemctl commands.
It also avtive when shutdown is not finished. Enable it using::

    systemctl enable debug-shell.service

shutdown debug
~~~~~~~~~~~~~~
If normal reboot or poweroff work, but take a suspiciously long time, then
boot with the debug options::

    systemd.log_level=debug systemd.log_target=kmsg log_buf_len=1M enforcing=0

save the following script as /usr/lib/systemd/system-shutdown/debug.sh and
make it executable::

    #!/bin/sh
    mount -o remount,rw /
    dmesg > /shutdown-log.txt
    mount -o remount,ro /

reboot

