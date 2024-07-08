#!/usr/bin/python
from scapy.all import sniff
def process_packet(packet):
    packet.show()
sniff(prn=process_packet)



# print(scapy.all.IFACES)


"""scapy est une librairie de manipulation des trames et des interfaces réseaux. Nous allons nous en servir pour examiner le trafic sur une des interfaces de notre ordinateur. Pour cela nous allons utiliser la fonction sniff qui peut prendre parmi ses paramètres une fonction callback qui sera exécutée sur chaque paquet sniffé.

⚠️ Attention, pour pouvoir utiliser la fonction sniff de scapy sur linux, il faut avoir un privilège particulier. Pour ce faire, nous avons deux possibilités :

    Lancer notre script en tant que root en utilisant la commande sudo python3 sniff.py
    Donner le privilège en question à python en utilisant la commande sudo setcap cap_net_raw=eip /usr/bin/python3.8

    pip install scapy
"""






# import scapy
# print(scapy.all.IFACES)

#### choisir l’interface que vous voulez cibler avec la fonction sniff grâce au paramètre iface :

# iface = "My interface name, example : enp0s3"
# sniff(prn=process_packet, iface=iface)