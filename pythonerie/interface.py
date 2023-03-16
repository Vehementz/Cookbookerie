#!/usr/bin/python
from scapy.all import sniff
def process_packet(packet):
    packet.show()
sniff(prn=process_packet)

import scapy
print(scapy.all.IFACES)

# iface = "My interface name, example : enp0s3"
# sniff(prn=process_packet, iface=iface)