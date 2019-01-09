# Arp_Spoofer

Arp_Spoof enables arpspoofing in a single execution unlike arpspoof command.
This python script coded for python 2.7 
If you are using python 3 then please do following modifications

line 42 :
print("\r [+] Sent Packets ..."+str(i)),

to

print("\r [+] Sent Packets ..."+str(i),end="")


line 47 & 48:
print("\r[+] Ctrl + C detected..!"),
	print("\r[+] Restoring Ip...!"),

to

print("\r[+] Ctrl + C detected..!",end="")
print("\r[+] Restoring Ip...!",end="")
