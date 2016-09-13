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
