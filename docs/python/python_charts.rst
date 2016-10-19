Python Charts
=============

Data format and libraries
-------------------------

csv:            [Standard Library] csv
json:           [Standard Library] json
excel:          openpyxl
database:       sqlite3/pymongodb

Aligned binary data:  [Standard Library] struct::

    >>> import struct
    >>> struct.unpack_from('5s10s', b'abcde 0123456789')
    (b'abcde', b' 012345678')


matplotlib
----------

| http://matplotlib.org/
| http://matplotlib.org/gallery.html


Installation::

    sudo apt-get install python-numpy python-matplotlib python-scipy


Overview
~~~~~~~~

Path for matplotlibrc::

    ./matplotlibrc
    ~/.config/matplotlib   # get by matplotlib.get_configdir()
    xxx/site-packages/matplotlib/mpl-data/matplotlibrc    # installation path
    
    #matplotlib.matplotlib_fname() get the matplitlibrc file name in use.


**set rc parameters**::

    import matplotlib as mpl
    mpl.rcParams['lines.linewidth'] = 2
    mpl.rcParams['lines.color'] = 'r'

    # call the rc() function
    mpl.rc('lines', linewidth=2, color='r')
    mpl.rcdefaults()


plot
~~~~

Examples::

    import numpy as np
    import matplotlib.pyplot as plt

    x = np.linspace(-np.pi, np.pi, 256, endpoint=True)

    plt.rcParams['lines.linewidth'] = 2
    plt.rcParams['lines.color'] = 'r'
    plt.plot(x, np.sin(x))

    plt.plot(x, np.cos(x), linewidth=3, color='g')

    plt.title('Function $\sin$ and $\cos$')
    plt.xlim(-np.pi, np.pi)
    plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi],
               [r'$-\pi$', r'$-\pi$', r'$0$', r'$+\pi/2$', r'$+\pi$',])        
    #plt.grid()
    plt.show()


date index
~~~~~~~~~~

Examples::

    import datetime
    import numpy as np
    import matplotlib.pyplot as plt                                                                                       
    import matplotlib.dates as mdates

    start = datetime.datetime(2016, 10, 1)
    stop  = datetime.datetime(2016, 10, 8)
    delta = datetime.timedelta(days=1)
    dates = mdates.drange(start, stop, delta)

    values = np.random.rand(len(dates))

    fig, ax = plt.subplots()
    ax.plot_date(dates, values, linestyle='-')

    date_format = mdates.DateFormatter('%Y-%m-%d')
    ax.xaxis.set_major_formatter(date_format)

    fig.autofmt_xdate()

    plt.show()


pie
~~~

Examples::

    import matplotlib.pyplot as plt
    from matplotlib.font_manager import FontProperties

    labels = ['项目1', '项目2', '项目3', '项目4']
    fracs = [60, 25, 5, 10]
    explode = (0.01, 0, 0, 0)
    pathes, texts, autotexts = plt.pie(fracs, labels=labels, explode=explode, counterclock=False,
                                       startangle=90, autopct='%3.1f%%', radius=0.5)

    # Make the labels on the small plot easier to read.
    font_zh = FontProperties(fname='/usr/share/fonts/truetype/arphic/uming.ttc')
    for t in texts:
        t.set_size('smaller')
        t.set_fontproperties(font_zh)  # show labels in zh_CN
    for t in autotexts:
        t.set_size('x-small')
    autotexts[0].set_color('y')

    plt.axis('equal')   # change ellipse to standard circle
    plt.show()          # show in tkinter window

    # save figure (eps, pdf, pgf, png, ps, raw, rgba, svg, svgz)
    fig = plt.gcf()
    fig.set_size_inches(6.4, 6.4)                                                                                     
    fig.savefig('test2png.png', dpi=100)
    fig.savefig('/tmp/test.png')


scatter
~~~~~~~

Examples::

    x = [1, 2, 3, 4]
    y = [5, 4, 3, 2]
    plt.scatter(x, y)

bar
~~~

Examples::

    plt.bar(x, y)


horizontal bar
~~~~~~~~~~~~~~

Examples::

    plt.barh(x, y)


stacked bar
~~~~~~~~~~~

Examples::

    import numpy as np
    import matplotlib.pyplot as plt
    from matplotlib.font_manager import FontProperties

    font_zh = FontProperties(fname='/usr/share/fonts/truetype/arphic/uming.ttc')

    N = 5
    means_1 = (20, 35, 30, 35, 27)
    means_2 = (25, 32, 34, 20, 25)
    means_3 = (1, 3, 4, 2 ,4)

    bottom_2 = means_1
    bottom_3 = [i + j for i, j in zip(means_1, means_2)]

    ind = np.arange(N)    # the x locations for the groups
    width = 0.9           # the width of the bars: can also be len(x) sequence

    p1 = plt.bar(ind, means_1, width, color='#d62728')
    p2 = plt.bar(ind, means_2, width, color='#10e010', bottom=bottom_2)
    p3 = plt.bar(ind, means_3, width, color='#1111e1', bottom=bottom_3)

    plt.ylabel('Values')
    plt.title('This Is The Title')
    plt.xlabel('范围', fontproperties=font_zh)
    plt.ylabel('项目1 -- 项目2 -- 项目3', fontproperties=font_zh)
    plt.xticks(ind, ('X1', 'X2', 'X3', 'X4', 'X5'), fontproperties=font_zh)
    plt.yticks(np.arange(0, 81, 10))
    #plt.legend((p1[0], p2[0], p3[0]), ('Item1', 'Item2', 'Item3'))

    plt.show()

layout
~~~~~~

Examples::

    import numpy as np
    import matplotlib.pyplot as plt 

    t = np.arange(0.0, 1.0, 0.01)

    plt.subplot(121)
    plt.plot(t, np.sin(2 * np.pi * t))

    plt.subplot(122)
    plt.plot(t, np.cos(2 * np.pi * t))
       
    plt.show()


pil
---

http://www.pythonware.com/library/pil/handbook/index.html

