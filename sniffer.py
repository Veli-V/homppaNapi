#! /usr/bin/env python
from scapy.all import *
from subprocess import call
import ConfigParser

def ConfigSectionMap(section):
    dict1 = {}
    options = Config.options(section)
    for option in options:
        try:
            dict1[option] = Config.get(section, option)
            if dict1[option] == -1:
                DebugPrint("skip: %s" % option)
        except:
            print("exception on %s!" % option)
            dict1[option] = None
    return dict1


# read config
Config = ConfigParser.ConfigParser()
Config.read("config.ini")

mac= ConfigSectionMap("dashButton")['mac']
ip = ConfigSectionMap("dashButton")['ip']
print ip + " " + mac

#callback function for sniffing.
def arp_monitor_callback(pkt):
    # if dash button is recogniced. These should be right
    # for some reasen hwsrc is not working
    #if pkt[ARP].hwsrc == mac:
        #print "Nappi1!"
    if pkt[ARP].psrc == ip:
        print "nappi!"
        call('./watch.py', shell=True)
    #this is here for debugging purposes, prints all arp calls out.
    if ARP in pkt and pkt[ARP].op in (1,2): #who-has or is-at
        return pkt.sprintf("%ARP.hwsrc% %ARP.psrc%")

#Sniff, store=0 so doesn't use memory
sniff(prn=arp_monitor_callback, filter="arp", store=0)
