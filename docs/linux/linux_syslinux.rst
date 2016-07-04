Linux syslinux
==============
https://wiki.archlinux.org/index.php/syslinux
http://git.kernel.org/cgit/boot/syslinux/syslinux.git/tree/doc/menu.txt
http://git.kernel.org/cgit/boot/syslinux/syslinux.git/

Syslinux is a collection of boot loaders capable of booting from hard drives,
CDs, and over the network via PXE.

It supports the FAT, ext2, ext3, ext4, and Btrfs file systems. 


Change Logs
-----------
http://www.syslinux.org/wiki/index.php?title=The_Syslinux_Project


Boot process overview
---------------------
1. Stage 1 : Part 1 - Load MBR - At boot, the BIOS loads the 440 byte MBR boot code at the start of the disk
   (/usr/lib/syslinux/bios/mbr.bin or /usr/lib/syslinux/bios/gptmbr.bin).

2. Stage 1 : Part 2 - Search active partition. The Stage 1 MBR boot code looks
   for the partition that is marked as active (boot flag in MBR disks). 
   Let us assume this is the /boot partition for example.

3. Stage 2 : Part 1 - Execute volume boot record - The Stage 1 MBR boot code
   executes the Volume Boot Record (VBR) of the /boot partition. In the case
   of syslinux, the VBR boot code is the starting sector of /boot/syslinux/ldlinux.sys
   which is created by the extlinux --install command.
4. Stage 2 : Part 2 - Execute /boot/syslinux/ldlinux.sys - The VBR will load rest of
   /boot/syslinux/ldlinux.sys. The sector location of /boot/syslinux/ldlinux.sys
   should not change, otherwise syslinux will not boot.

.. Note::
    In the case of Btrfs, the above method will not work since files move around
    resulting in changing of the sector location of ldlinux.sys. Therefore, in
    BTRFS the entire ldlinux.sys code is embedded in the space following the VBR
    and is not installed at /boot/syslinux/ldlinux.sys unlike the case of other filesystems.

5. Stage 3 - Load /boot/syslinux/ldlinux.c32 - The /boot/syslinux/ldlinux.sys
   will load the /boot/syslinux/ldlinux.c32 (core module) that contains the
   rest of core part of syslinux that could not be fit into ldlinux.sys
   (due to file-size constraints). The ldlinux.c32 should be present in every
   syslinux installation and should match the version of ldlinux.sys installed
   in the partition. Otherwise syslinux will fail to boot.
   See http://bugzilla.syslinux.org/show_bug.cgi?id=7 for more info.

6. Stage 4 - Search and Load configuration file - Once Syslinux is fully loaded,
   it looks for /boot/syslinux/syslinux.cfg (or /boot/syslinux/extlinux.conf in
   some cases) and loads it if it is found. If no configuration file is found,
   you will be dropped to a syslinux boot: prompt. This step and rest of non-core
   part of syslinux (`/boot/syslinux/*.c32` modules, excluding lib*.c32 and ldlinux.c32)
   require `/boot/syslinux/lib*.c32` (library) modules to be present 
   (http://www.syslinux.org/wiki/index.php/Common_Problems#ELF). The lib*.c32
   library modules and non-core `*.c32` modules should match the version of ldlinux.sys
   installed in the partition.


Limitations of UEFI Syslinux
----------------------------
#. UEFI Syslinux application syslinux.efi cannot be signed by sbsign (from sbsigntool)
   for UEFI Secure Boot. Bug report - http://bugzilla.syslinux.org/show_bug.cgi?id=8
#. Using TAB to edit kernel parameters in UEFI Syslinux menu lead to garbaged display
   (text on top of one-another). Bug report - http://bugzilla.syslinux.org/show_bug.cgi?id=9
#. UEFI Syslinux does not support chainloading other EFI applications like UEFI Shell
   or Windows Boot Manager. Enhancement request - http://bugzilla.syslinux.org/show_bug.cgi?id=17
#. In some cases, UEFI Syslinux might not boot in some Virtual Machines like QEMU/OVMF
   or VirtualBox or some VMware products/versions and in some UEFI emulation environments
   like DUET. A Syslinux contributor has confirmed no such issues present on
   VMware Workstation 10.0.2 and Syslinux-6.02 or later.
   Bug reports - http://bugzilla.syslinux.org/show_bug.cgi?id=21 and http://bugzilla.syslinux.org/show_bug.cgi?id=23
#. Memdisk is not available for UEFI. Enhancement request - http://bugzilla.syslinux.org/show_bug.cgi?id=30
