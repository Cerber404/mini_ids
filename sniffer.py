from scapy.all import sniff
from detector import detect

# IP твоего компьютера
MY_IP = "192.168.1.3"

def process_packet(packet):
    if packet.haslayer("IP"):
        src_ip = packet["IP"].src
        dst_ip = packet["IP"].dst

        # анализируем только пакеты, направленные к тебе
        if dst_ip != MY_IP:
            return

        # игнорируем пакеты от самого себя
        if src_ip == MY_IP:
            return

        # оставляем только локальную сеть
        if not src_ip.startswith("192.168."):
            return

        # игнорируем multicast и broadcast
        if src_ip.startswith("224.") or src_ip.endswith(".255"):
            return

        port = None

        if packet.haslayer("TCP"):
            port = packet["TCP"].dport

        print(f"Packet: {src_ip} -> {dst_ip}")

        detect(src_ip, port)

def start_sniffing():
    print("Starting packet capture...\n")
    sniff(prn=process_packet, store=False)