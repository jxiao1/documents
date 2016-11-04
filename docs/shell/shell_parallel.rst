Python Parallel
===============

Example 1::

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


Example 2::

    task_start() {
        local name="$1"

        touch $TMPDIR/${name}.monitor_running
        while [ -e "$TMPDIR/${name}.monitor_running" ] ; do
            ...
            # add_task $other_task_name $action
        done
    }

    task_stop() {
        local name="$1"
        rm -rf $TMPDIR/${name}.monitor_running
    }

    add_task() {
        local name=$1
        local action=$2
        grep -o "$name.$action" $JOBFILE >&- 2>&- || {
            echo "$name.$action" >> $JOBFILE 2>&-
        }
    }

    # Process each task in the $jobfile in FIFO order
    do_tasks() {
        local line queued_task

        if [ -f $JOBFILE ] ; then
            mv $JOBFILE ${JOBFILE}.work
            while read line; do
                execute_task() {
                    case $2 in
                        "action1") task_start $action2_task_name &;;
                        "action2") task_start $action1_task_name &;;
                        *) DBG_ERROR "## Unknown task command: $2 ##";;
                    esac
                }
                queued_task=$(echo $line | awk -F "." '{print $1,$2}')
                execute_task $queued_task
            done < ${JOBFILE}.work
            rm -rf ${JOBFILE}.work
        fi
    }

    task_loop() {
        task_start $first_task_name &

        while [ "$task_daemon_running" == 1 ] ; do
            do_tasks
            sleep 1
        done
    }



