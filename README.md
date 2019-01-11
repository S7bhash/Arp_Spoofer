# Arp_Spoofer
Arp_Spoof enables arpspoofing in a single execution unlike arpspoof command.

How to use: 
---

Clone the repository to Desktop and then type the following command:

`cd Desktop`

`python spoofer.py -t 192.168.0.104 -r 192.168.0.1`

-t stands for target ip and -r stands for router ip 

Use the command :

`python spoofer.py -h`
to get help and options

Python Version compatibility:
---
This python script coded for python 2.7 
If you are using python 3 then please do following modifications

line 42 :

```print("\r [+] Sent Packets ..."+str(i)), ```

to

```print("\r [+] Sent Packets ..."+str(i),end="")```


line 47 & 48:

```print("\r[+] Ctrl + C detected..!"), ```

```print("\r[+] Restoring Ip...!"), ```

to

```print("\r[+] Ctrl + C detected..!",end="")```

```print("\r[+] Restoring Ip...!",end="")```
