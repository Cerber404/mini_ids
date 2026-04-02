import socket
import time

def scan_ports(ip, ports):
    print(f"\nScanning {ip}...\n")

    start_time = time.time()
    open_ports = []

    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)

        result = sock.connect_ex((ip, port))

        if result == 0:
            print(f"[OPEN] Port {port}")
            open_ports.append(port)

        sock.close()

    end_time = time.time()

    print("\nScan completed")
    print(f"Open ports: {len(open_ports)}")
    print(f"Time taken: {round(end_time - start_time, 2)} seconds")