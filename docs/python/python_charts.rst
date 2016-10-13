Python Charts
=============


matplotlib
----------

| http://matplotlib.org/
| http://matplotlib.org/gallery.html


pie chart
~~~~~~~~~

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
