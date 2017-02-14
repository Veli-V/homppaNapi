#! /usr/bin/env python
from scapy.all import *
from subprocess import call

def arp_monitor_callback(pkt):
    if pkt[ARP].hwsrc == '34:D2:70:DA:5D:9D':
        print "Nappi1!"
    if pkt[ARP].psrc == '192.168.11.7':
        print "nappi!"
        # call('./testi.sh', shell=True)
    if ARP in pkt and pkt[ARP].op in (1,2): #who-has or is-at
        return pkt.sprintf("%ARP.hwsrc% %ARP.psrc%")

sniff(prn=arp_monitor_callback, filter="arp", store=0)
