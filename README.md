# 🛡️ Mini IDS + Network Scanner

## 📌 About the Project

This project is a simple Intrusion Detection System (IDS) combined with a port scanner.

It monitors network traffic in real time, detects suspicious activity, and logs events into a file.


## 🎯 Goal

The main goal is to understand:

* how network traffic works
* how attacks are detected
* how IDS systems operate


## ⚙️ Features

### 🔍 Port Scanner

* scans ports of a target IP
* shows open ports
* displays execution statistics


### 🌐 Packet Sniffer

* captures network packets
* shows source and destination IP


### 🚨 Attack Detection

The system detects:

* **Flood attacks**
  → many packets from one IP

* **Port scanning**
  → access to multiple ports


### 📄 Logging

All events are stored in:

```text id="en_log_file"
logs/alerts.log
```


### ⚙️ Configuration

Settings are stored in `config.json`:

```json id="en_config"
{
  "flood_threshold": 20,
  "scan_threshold": 10,
  "whitelist": ["192.168.1.3"]
}
```


## 🧠 Key Features

* only incoming traffic is analyzed
* the system focuses on the **local network (192.168.x.x)**
* this reduces noise and false positives
* whitelist is used to ignore trusted IPs


## 🚀 Installation

```bash id="en_install"
pip install -r requirements.txt
```


## ▶️ Usage

### 🔹 Run Port Scanner

```bash id="en_scan"
python main.py --scan 192.168.1.1
```


### 🔹 Run IDS Monitor

```bash id="en_monitor"
python main.py --monitor
```


## 🧪 Demo

1. Start IDS:

```bash id="en_demo1"
python main.py --monitor
```

2. From another device:

```bash id="en_demo2"
ping 192.168.1.3
```

or:

```bash id="en_demo3"
nmap -p 1-100 192.168.1.3
```

3. Output:

```text id="en_output"
WARNING: Flood detected from ...
CRITICAL: Port Scan detected from ...
```

## ⚠️ Limitations

* possible false positives
* simplified detection logic
* only local network traffic is analyzed


## 🧠 Conclusion

This project demonstrates a basic IDS system that:

* monitors network traffic
* detects suspicious behavior
* logs security events


## 👨‍💻 Author

Student Project — Mini IDS
