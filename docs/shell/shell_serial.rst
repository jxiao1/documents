Shell Serial Device
===================

Example::

    
    RESPONSE="/tmp/.response"

    do_atcommand() {
        atcommand="$1"

        #cat will read the response, then die on timeout
        cat <&5 >$RESPONSE 2>/dev/null &

        echo -ne "$atcommand\r\n" >&5 2>/dev/null || {
            echo "Device busying!"
            return 1
        }

        #wait for cat to die
        wait $!

        return 0
    }


    # Clear old response result file
    echo > $RESPONSE

    # Set modem with timeout of 5/10 a second
    stty -F $dev 115200 -echo igncr -icanon onlcr ixon min 0 time 60 2>/dev/null

    # Open modem on FD 5
    exec 5<>$dev

    do_atcommand "$cmd"

    result=`cat $RESPONSE | sed '/^$/d' | sed -n "/$cmd/{n;p}"`
    [ -n "$result" ] && {
        echo "$result" | grep -q "ERROR" || {
            echo $result
            RETRIES=1
        }
    }

    # Close FD5
    exec 5<&-

    rm -f $RESPONSE
