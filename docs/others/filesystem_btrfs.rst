File System btrfs
=================

Create btrfs filesystem
-----------------------
::

    # Create the btrfs filesystem
    mkfs.btrfs -L label /dev/sdc2 
    mount /dev/sdc2 /mnt

    # Show information
    btrfs filesystem show


Modify the btrfs filesystem
---------------------------
::

    # Resize btrfs filesystem online
    btffs filesystem resize 4G /mnt
    btffs filesystem resize +1G /mnt
    btffs filesystem resize -1G /mnt

    # Add/Delete
    btrfs device add /dev/sdc1 /mnt #Don't need mkfs firtly.
    btrfs device delete /dev/sdc1 /mnt
    

Snapshot and Rollback
---------------------
::

    # Create snapshot
    btrfs subvolume snapshot /mnt /mnt/snap1

    # Delete snapshot
    btrfs subvolume delete /mnt/snap1

    # Rollback
    btrfs subvolume list
    btrfs subvolume set-default <id> <path>
    umount /mnt && mount /dev/sdc2 /mnt || reboot
    
