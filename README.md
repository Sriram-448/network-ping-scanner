#  Network Ping Scanner (ICMP Host Discovery)

A Python-based network utility that performs ICMP echo-based host discovery over a given IPv4 subnet. This project demonstrates foundational networking concepts and OS-level command execution.

##  Overview

The scanner accepts a CIDR-formatted network range (e.g., 192.168.1.0/24) and checks host availability by issuing ICMP Echo Requests using the system ping utility.

This project focuses on clarity, correctness, and cross-platform compatibility, making it suitable for beginners learning networking fundamentals.

##  Features

- CIDR-based subnet handling using ipaddress
- ICMP Echo Request-based host detection
- Cross-platform support (Windows / Linux)
- Clear console output indicating host availability

##  Concepts Demonstrated

- IPv4 addressing and subnetting
- ICMP protocol fundamentals
- OS-level command execution from Python
- Sequential network probing logic

##  Current Limitations

- Hosts are scanned sequentially, which impacts performance on larger subnets
- Scan scope is intentionally limited (first 10 hosts)
- No latency (RTT) measurement
- No real-time or continuous monitoring
- Relies on external ping command execution

These limitations are deliberate to keep the implementation beginner-friendly.

##  Planned Improvements

- Asynchronous or concurrent scanning
- Full subnet coverage
- Round-trip time (RTT) extraction
- Continuous monitoring mode
- Structured output (JSON / CSV)
- Raw ICMP implementation (no shell calls)


##  ICMP Explained

Internet Control Message Protocol (ICMP) operates at the network layer and is used for diagnostic and control messaging.

```
When running:

ping 192.168.1.1
```

- An ICMP Echo Request is sent
- The target responds with an Echo Reply
- Receipt of the reply confirms host reachability

##  What This Code Actually Does

- Launches hundreds of ICMP probes simultaneously
- Updates host status every few seconds
- Identifies hosts going UP or DOWN
- Works on Windows and Linux without admin privileges

This is real scanning behavior.













<!-- #  Basic Network Ping Scanner using Python

This is a beginner-friendly Python project that scans a range of IP addresses and checks which devices are "alive" using the `ping` command.

##  What it does

- Accepts a network range like `192.168.1.0/24`
- Pings the first 10 IP addresses
- Prints whether each device is online or offline

##  Tools Used

- Python `os` and `platform` modules
- `ipaddress` for handling subnets
- Works cross-platform (Windows/Linux)

##  What You Learn

- Basic networking concepts (IP, ICMP, ping)
- How devices are discovered on local networks
- Simple scripting for network tasks

##  How to Run

1. Open terminal / command prompt
2. Replace the subnet in the script with your real one (use `ipconfig` or `ifconfig`)
3. Run the script:
   ```bash
   python networkscanner.py

## ICMP

Internet Control Message Protocol
It's a network layer protocol used to send control messages between devices — mainly to report errors and network status.

When you run:
ping 192.168.1.1

This is what happens:

- Your computer sends an ICMP Echo Request
- The target device replies with an ICMP Echo Reply
- If reply is received → the device is alive and reachable -->
