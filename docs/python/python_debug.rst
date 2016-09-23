Python Performance and Debug
============================

- https://wiki.python.org/moin/PythonTestingToolsTaxonomy
- http://www.jb51.net/article/63244.htm
- http://blog.jobbole.com/51062/


pdb
---
python -m pdb xxx.py


time
----
time.time()
timeit
/usr/bin/time --verbose python test.py


trace
-----
https://docs.python.org/3/library/trace.html

The trace module allows you to trace program execution, generate annotated statement coverage listings,
print caller/callee relationships and list functions executed during a program run.
It can be used in another program or from the command line.

python -m trace --count -C . somefile.py


cProfile
--------
https://docs.python.org/3/library/profile.html

python -m cProfile -s cumulative test.py


pycallgraph tool
----------------

http://pycallgraph.slowchop.com/en/master/


memory_profiler
---------------
pip install psutil memory_profiler

https://pypi.python.org/pypi/psutil#downloads
https://pypi.python.org/pypi/memory_profiler/

# line by line
python -m memory_profiler test.py

# timing sequence
mprof run test.py  #output to mprofile_xxxx.dat by default
mprof plot mprofile_xxx.dat


line_profiler
-------------
https://pypi.python.org/pypi/line_profiler/
https://github.com/rkern/line_profiler

sudo pip install line_profiler
::

    @profile
    def show_function():
         ...

kernprof.py -l -v test.py


objgraph
--------
https://pypi.python.org/pypi/objgraph/
http://mg.pov.lt/objgraph/

pip install xdot objgraph


guppy
-----
http://guppy-pe.sourceforge.net/

Install: ``sudo pip install guppy``

Example::

    from guppy import hpy
      
    def random_sort3(n):
      hp = hpy()
      print "Heap at the beginning of the functionn", hp.heap()
      l = [random.random() for i in range(n)]
      l.sort()
      print "Heap at the end of the functionn", hp.heap()
      return l
      
    if __name__ == "__main__":
      random_sort3(2000000)

    #hp.heap().more.more  for more defails
