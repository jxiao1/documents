WiFi Linux Commands
===================

AP mode
-------

**WiFi AP mode commands**::

    brctl delif br-bridge wlan0
    ifconfig br-bridge down
    brctl delbr br-bridge
    killall hostapd

    #Configure correct WiFi mode
    iw wlan0 del
    iw phy phy0 interface add wlan0 type managed

    /usr/local/bin/hostapd -B /root/examples/wifi-apmode/hostapd.conf

    #Remove the wlan0 interface address and let the bridge do the work
    brctl addbr br-bridge
    ifconfig br-bridge  192.168.1.1
    ifconfig wlan0 0.0.0.0

    #Enable IPv4 forwarding
    echo "1" > /proc/sys/net/ipv4/ip_forward

    #Bring the bridge up
    /sbin/ifconfig br-bridge up

    #Use dnsmasq to provide dns and dhcp functions
    killall dnsmasq
    /usr/sbin/dnsmasq -Z -i br-bridge -F 192.168.1.100,192.168.1.249,255.255.255.0,720m

    #Routing and NAT rules
    /sbin/route add -net 239.0.0.0/8 br-bridge
    /sbin/iptables -A FORWARD -i br-bridge -s 192.168.1.0/24 -j ACCEPT
    /sbin/iptables -A POSTROUTING -t nat -j MASQUERADE


hostapd configuration file example::

    interface=wlan0
    bridge=br-bridge
    driver=nl80211
    logger_syslog=-1
    logger_syslog_level=2
    logger_stdout=-1
    logger_stdout_level=2
    dump_file=/tmp/hostapd.dump
    ctrl_interface=/var/run/hostapd
    ctrl_interface_group=0
    ssid=WRIDPSDK
    country_code=US
    hw_mode=g
    channel=11
    beacon_int=100
    dtim_period=2
    max_num_sta=255
    rts_threshold=2347
    fragm_threshold=2346
    macaddr_acl=0
    auth_algs=3
    ignore_broadcast_ssid=0
    wmm_enabled=1
    wmm_ac_bk_cwmin=4
    wmm_ac_bk_cwmax=10
    wmm_ac_bk_aifs=7
    wmm_ac_bk_txop_limit=0
    wmm_ac_bk_acm=0
    wmm_ac_be_aifs=3
    wmm_ac_be_cwmin=4
    wmm_ac_be_cwmax=10
    wmm_ac_be_txop_limit=0
    wmm_ac_be_acm=0
    wmm_ac_vi_aifs=2
    wmm_ac_vi_cwmin=3
    wmm_ac_vi_cwmax=4
    wmm_ac_vi_txop_limit=94
    wmm_ac_vi_acm=0
    wmm_ac_vo_aifs=2
    wmm_ac_vo_cwmin=2
    wmm_ac_vo_cwmax=3
    wmm_ac_vo_txop_limit=47
    wmm_ac_vo_acm=0
    eap_server=0
    wpa=2
    wpa_passphrase=mypassword
    wpa_key_mgmt=WPA-PSK
    wpa_pairwise=TKIP CCMP
    wpa_group_rekey=600
    wpa_gmk_rekey=86400


Client Mode
-----------

**WiFi Client commands**::

    iw wlan0 del
    iw phy phy0 interface add wlan0 type managed
    iw wlan0 set channel  <channel>
    ifconfig wlan0 up
    # if remote AP uses no security mode, don't need wpa_supplicant
    wpa_supplicant -B -D wext -i wlan0 -c /etc/wpasupplicant.conf
    iw wlan0 connect -w <ap_essid>
    iw wlan0 link  # show connection result information

    #See also other commands
    ifconfig wlan0 down
    dhclient -r wlan0
    ifconfig wlan0 up
    iwconfig wlan0 essid "IDPDK-7AAA"
    iwconfig wlan0 mode Managed
    dhclient wlan0
    dhclient -timeout 5 -pf /var/run/dhclient-wlan0.pid \
      -lf /var/lib/dhclient/dhclient-wlan0.leases wlan0
    
    #Scan APs
    ifconfig wlan0 up
    iw wlan0 scan | grep "SSID:" | sort | uniq

    #List all APs
    iwlist wlan0 scan | grep -B 5 -A 20 "7AAA" | sed '/Address/,/Cell/p;d'

**wpasupplicant.conf examples**

WEP::

    #/etc/wpasupplicant.conf
    ctrl_interface=/var/run/wpa_supplicant
    ctrl_interface_group=wheel

    # Allow all valid ciphers
    network={
        ssid="ap_essid"
        scan_ssid=1
        key_mgmt=NONE
        wep_key0=my_wep_key
    }


WPA2::

    #/etc/wpasupplicant.conf
    ctrl_interface=/var/run/wpa_supplicant
    ctrl_interface_group=wheel

    # Allow all valid ciphers
    network={
        ssid="ap_essid"
        scan_ssid=1
        key_mgmt=WPA-PSK
        psk=my_wpa_key
    }

WPA Enterprise::

    ctrl_interface=/var/run/wpa_supplicant
    ctrl_interface_group=wheel
    network={
        ssid="ap_essid"
        scan_ssid=1
        key_mgmt=WPA-EAP
        pairwise=CCMP TKIP
        group=CCMP TKIP WEP104 WEP40
        eap=PEAP
        identity="username"
        password="password"
    }


Ad-Hoc mode
-----------

To connect to a remote AP with no security Mode::

    iw wlan0 del
    iw phy phy0 interface add wlan0 type adhoc
    iw wlan0 set channel  <channel>
    ifconfig wlan0 up
    iw dev wlan0 ibss join <ssid> <frequency>

The following table shows the channels and their corresponding frequencies
to be used in the joining of the ad-hoc network using the iw command::

    1   -   2412
    2   -   2417
    3   -   2422
    4   -   2427
    5   -   2432
    6   -   2437
    7   -   2442
    8   -   2447
    9   -   2452
    10  -   2457
    11  -   2462
    12  -   2467
    13  -   2472
