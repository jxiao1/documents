Shell Project
=============

Logo
----

Generate logo by figlet::

    git clone https://github.com/cmatsuoka/figlet
    cd figlet
    make figlet

    ./showfigfonts -d ./fonts
    ./figlet MyApp -f ./fonts/standard.flf


Self Decompress
---------------

Example::

    #! /bin/bash

    UNZIP_DIR=`mktemp -d /tmp/mytool.$$.XXXX`
    PAYLOAD_OFFSET=`grep -an -m1 "^ARCHIVE_MARKER:" $0 | cut -d: -f1`

    tail -n +$((PAYLOAD_OFFSET+1)) $0 | tar zxf - --ignore-command-error -C ${UNZIP_DIR} 2>/dev/null
    exec ${UNZIP_DIR}/mytool.sh "$@"
    exit $?

    ARCHIVE_MARKER:
    ...#The tar file here

