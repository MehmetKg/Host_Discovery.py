from scapy.all import *


eth = Ether(dst="ff:ff:ff:ff:ff:ff")


arp = ARP(pdst="10.10.10.0/24")


bcPckt = eth / arp


ans, unans = srp(bcPckt, timeout=5, verbose=False)

print("Ağda bulunan cihazlar:")
print("#" * 30)
for snd, rcv in ans:
    print(f"IP: {rcv.psrc}  -  MAC: {rcv.hwsrc}")

