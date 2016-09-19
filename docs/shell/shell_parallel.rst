Python Parallel
===============

Example code::

    #!/bin/bash

    SUB_PROCESS_NUM=8
    TMPFILE="/tmp/$$.fifo"

    # Open w/r FIFO on file handler 9
    mkfifo $TMPFILE
    exec 9<>$TMPFILE

    for ((i=0; i<$SUB_PROCESS_NUM; i++)) ; do
        echo ""
    done >&9

    for ((i=0; i<20; i++)) ; do
        read -u 9
        {   # do something here
            echo "${i} start------------------------------"
            sleep 1
            echo "${i} exit-------------------------------"
            
            # must add new line to enable another sub-process
            echo "" >&9
        } &
    done

    # wait for all background process done and exit.
    wait
    exec 9>&-
    rm -f $TMPFILE

