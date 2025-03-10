from scapy.all import *

ipList = []
network_prefix = "10.0.2."

for i in range(1, 251):  # 1'den 250'ye kadar IP'leri tarar
    dst_ip = network_prefix + str(i)

    pingPckt = IP(dst=dst_ip) / ICMP()

    response = sr1(pingPckt, timeout=0.5, verbose=False)

    if response:
        print(f"{dst_ip} is up")
        ipList.append(dst_ip)

print("Reachable IPs:", ipList)
