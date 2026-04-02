import argparse
from scanner import scan_ports
from sniffer import start_sniffing

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("--scan", help="Scan target IP")
    parser.add_argument("--monitor", action="store_true")

    args = parser.parse_args()

    if args.scan:
        scan_ports(args.scan, range(1, 300))

    elif args.monitor:
        start_sniffing()

    else:
        print("Use --scan or --monitor")

if __name__ == "__main__":
    main()