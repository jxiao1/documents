Shell Switch Root
=================

chroot
------

Example::

    cd $ROOT
    mount -t proc proc proc
    mount -t sysfs sys sys
    mount -t devtmpfs devtmpfs dev
    chroot $ROOT /bin/systemd-tmpfiles --create --remove --boot >/dev/null 2>&1
    
    chroot $ROOT <command-and-args-doing-something>
    RET=$?
    
    chroot $ROOT /bin/systemd-tmpfiles --clean >/dev/null 2>&1
    umount -l dev
    umount -l sys
    umount -l proc
    
    exit $RET


switch_root
-----------

Usually, it's used in initramfs to switch to the real root filesystem.
switch_root moves already mounted /proc, /dev, /sys and /run to newroot
and makes newroot the new root filesystem and starts init process.

Example::

    exec /sbin/switch_root "$ROOTMNT" /sbin/init $@

