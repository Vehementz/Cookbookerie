#!/usr/bin/env python
from scapy.layers.http import HTTPRequest
packet.haslayer(HTTPRequest)
method = packet[HTTPRequest].Method.decode()

import scapy.all as scapy
ip = packet[scapy.IP].src


from datetime import datetime, timezone, timedelta
epoch = datetime.now(tz=timezone.utc).timestamp()

