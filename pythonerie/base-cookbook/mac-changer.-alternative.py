#!/usr/bin/env python

#to start the script python mac-changer.py
# command python mac-changer.py --help
# command python mac-changer.py --interface wlan0 --mac 00:11:22:33:44:55

 


import subprocess
import optparse

def change_mac(interface, new_mac):
    print("[+] Changing the MAC address for interface " + interface + " to " + new_mac)
    subprocess.call("ifconfig", shell=True)
    subprocess.call("ifconfig " + interface + " down", shell=True)
    subprocess.call("ifconfig " + interface + " hw ether " + new_mac, shell=True)
    subprocess.call("ifconfig " + interface + " up", shell=True)



parser = optparse.OptionParser()

parser.add_option("-i", "--interface", dest="interface",  help="Interface to change its MAC address")
parser.add_option("-m", "--mac", dest="new_mac",  help="New MAC address")

(options, arguments) = parser.parse_args()



#interface = "wlan0"
#new_mac = "00:11:22:33:44:77"

# interface = input("interface > ")
# new_mac = input("new MAC > ")

interface = options.interface
new_mac = options.new_mac



# Permet de voir les interfaces réseau


change_mac(options.interface, options.new_mac)

