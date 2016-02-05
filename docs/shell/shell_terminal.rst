Shell Terminal
==============

**terminal color**::

    ESC="\e" or "\033"

    ESC[0m       # reset all (colors and brightness)
    ESC[1m       # bright
    ESC[2m       # dim (looks same as normal brightness)
    ESC[22m      # normal brightness

    # FOREGROUND:
    ESC[30m      # black
    ESC[31m      # red
    ESC[32m      # green
    ESC[33m      # yellow
    ESC[34m      # blue
    ESC[35m      # magenta
    ESC[36m      # cyan
    ESC[37m      # white
    ESC[39m      # reset

    # BACKGROUND
    ESC[40m      # black
    ESC[41m      # red
    ESC[42m      # green
    ESC[43m      # yellow
    ESC[44m      # blue
    ESC[45m      # magenta
    ESC[46m      # cyan
    ESC[47m      # white
    ESC[49m      # reset


**Other Control code**::

    ESC[4m       # under line  
    ESC[5m       # blink
    ESC[7m       # enable echo
    ESC[8m       # disable echo
    ESC[nA       # move up <n> lines
    ESC[nB       # move up <n> lines  
    ESC[nC       # move right <n> colums  
    ESC[nD       # move left <n> colums 
    ESC[y;xH     # set the cursor position
    ESC[2J       # clear full screen
    ESC[K        # clear from current to end of the line
    ESC[s        # save the cursor position
    ESC[u        # restore the cursor position
    ESC[?25l     # hidden the cursor
    ESC[?25h     # display the cursor


**References**

    http://invisible-island.net/xterm/ctlseqs/ctlseqs.html

