OpenWRT Quickstart
==================

| https://openwrt.org/
| https://dev.openwrt.org/wiki
| http://wiki.openwrt.org/doc/howto/buildroot.exigence#git
|


Prepare
-------

::

    sudo apt-get install gcc g++ gcc-multilib binutils patch bzip2 make libtool libc6 \
                         automake autoconf gettext texinfo unzip sharutils flex bison \
                         libncurses5-dev ncurses-term zlib1g-dev libssl-dev libz-dev  \
                         build-essential gawk asciidoc git-core git subversion screen quilt


Get Source code
---------------

https://dev.openwrt.org/wiki/GetSource

Master::

    git clone git://git.openwrt.org/openwrt.git

14.07 branch (Barrier Breaker)::

    git clone git://git.openwrt.org/14.07/openwrt.git



Build
-----

::

    cp feeds.conf.default feeds.conf

    ./scripts/feeds update -a     //Update all feeds listed within feeds.conf.default
    ./scripts/feeds install -a       //Install all packages from all feeds

    make defconfig
    make prereq
    make menuconfig                 //example: for x86 generic

            Target System ==> X86
            Subtarget ==> Generic
            Target Profile ==> Generic
            Target Image
                    [*] tar.gz
                    [*] ext4
                    [*] Build VirtualBox image files (VDI)   //for virtualBox test
                    (32) Kernel partition size (in MB)
                    (128) Root filesystem partition size (in MB)
                    [*] Include kernel in root filesystem  --->
                            [*]   include zImage (NEW)  
            

            Any other configuration change according to your project.

    make -j4 V=s  # maby failed because of download packages failed or other problems,
                  # download it to dl folder manually in other way and try again

Where to find bin and vdi::

    bin/x86/openwrt-x86-generic-combined-ext4.vdi
    bin/x86/openwrt-x86-generic-combined-ext4.img.gz


Virtual box img convert
-----------------------
::

    VBoxManage convertfromraw --format VDI openwrt-xxx.img openwrt.vdi


Create Virtual box Machine
--------------------------
::

    name: openwrt-14.04
    type:  linux
    version: linux2.6/3.x(32bit)

    Do not add a virtural hard drive

    Settings-->Storage-->Controller:IDE add above vdi file.
    Settings-->Network-->Adapter1:  
            Attached to: NAT
            Adapter Type: PCnet-PCI II (Am79C970) 
    Settings-->Network-->Adapter2:  
            Attached to: Bridged Adapter
            Adapter Type: Intel PRO/1000 MT Desktop (82540EM) 
    Settings-->Serial Ports-->Enable Serial Port COM1


Boot rootfs in real x86 board/host
----------------------------------

::

    make menuconfig

            Kernel modules
                    USB Support -->
                            <*> kmod-usb-acm
                            <*> kmod-usb-hid
                            <*> kmod-usb-net
                                    <*> kmod-usb-net-dm96010-ether ...
                            <*> kmod-usb-ohci
                            <*> kmod-usb-serial
                                    <*> kmod-usb-serial-cp210x
                            <*> kmod-usb-serial-option
                            <*> kmod-usb-serial-pl2303
                            <*> kmod-usb-uhci
                            <*> kmod-usb-storage
                            <*> kmod-usb-storage-extras

    make -j4 V=s  

    gzip -d bin/x86/openwrt-x86-generic-combined-ext4.img.gz
    sudo dd if=./bin/x86/openwrt-x86-generic-combined-ext4.img of=/dev/sdc bs=512
    sync

