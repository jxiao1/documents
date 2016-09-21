Linux Performance Test
======================

Run time monitor tools
----------------------
top uptime
ps pstree
free
sysstat sar
mpstat vmstat iostat
netstat ss
numastat
pmap
iptraf
tcpdump wireshark
strace ltrace
dmidecode

Benchmark
---------

sudo apt-get install sysbench

SPEC CPU 2006  (cpu)
STREAM (memory)
FIO (io)
Bonnie++ (disk driver)


Filesystem
----------

iozone

Network
-------

Netperf


Change the system
-----------------
sysctl  (about kernel, io, mem, net)
chrt
nice ionice
taskset
ulimit

ethtool

OOM Killer
----------

sysctl vm.panic_on_oom 1/0
cat /proc/PID/oom_score
echo -17~15 > /proc/PID/oom_adj
echo f >/proc/sysrq-trigger


dtrace
------

http://blog.chinaunix.net/uid-20696246-id-1891965.html

Installation::

    sudo apt-get install build-essential flex libelf-dev libc6-dev-amd64 binutils-dev libdwarf-dev
    wget ftp://crisp.dyndns-server.com/pub/release/website/dtrace/dtrace-20111124.tar.bz2
    make all
    make install
    make load


SystemTap
---------

http://www.cnblogs.com/leaven/archive/2011/01/07/1929431.html


Fanotify
--------

http://www.ibm.com/developerworks/cn/linux/l-cn-fanotify/index.html

Graphic Tool
------------
::

    sudo apt-get install gnuplot
    
    cat /tmp/test
        set xdata time
        set timefmt "%H时%M分%S秒"
        set xlabel 'TIME'
        set ylabel 'CPU'
        set terminal png size 800,600
        set output "/tmp/cpu.png"
        plot '/tmp/1' using 1:3 title '%us' with lines, '/tmp/1' using 1:5 title '%sy' with lines

    gnuplot /tmp/2
