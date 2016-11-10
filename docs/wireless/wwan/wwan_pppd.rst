PPPD usage
==========

The simple way to use pppd is to provide the peers and chat file.
The following example is for 3G.

/etc/ppp/peers/test::

    debug debug debug
    /dev/ttyACM0
    115200
    logfile /var/log/ppp.log
    nomultilink
    defaultroute
    noipdefault
    ipcp-restart 7
    ipcp-accept-local
    ipcp-accept-remote
    lcp-echo-interval 0
    lcp-echo-failure 999
    modem
    noauth
    nocrtscts
    noipdefault
    noaccomp
    noccp
    novj
    usepeerdns
    persist
    connect '/usr/sbin/chat -v -f /etc/ppp/chat/test'


/etc/ppp/chat/test::

    ABORT BUSY
    ABORT 'NO CARRIER' 
    ABORT VOICE 
    ABORT 'NO DIALTONE'
    ABORT 'NO DIAL TONE'
    ABORT 'NO ANSWER'
    ABORT DELAYED
    ABORT ERROR
    SAY "Initializing\n"
    '' 'ATZ'
    OK 'AT+CGDCONT=1,"IP","$USE_APN"'
    OK 'AT+CFUN=1'
    OK 'AT'
    OK 'ATD*99***1#'
    SAY "Calling UMTS/GPRS"
    TIMEOUT 120
    CONNECT ' '
