#!/usr/bin/env python3
"""
Simple TCP port scanner for CYB midterm.
Authorized targets: localhost (127.0.0.1) and scanme.nmap.org only.
"""

import socket
import time

def scan_port(host: str, port: int, timeout: float = 0.5) -> bool:
    """
    Attempt to connect to a single TCP port.
    Returns True if open, False otherwise.
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(timeout)
        try:
            result = s.connect_ex((host, port))
            return result == 0
        except socket.gaierror:
            print(f"[ERROR] Hostname could not be resolved: {host}")
            return False
        except OSError as e:
            print(f"[ERROR] Socket error on port {port}: {e}")
            return False

def validate_port(port_str: str) -> int:
    """
    Validate and convert a port string to an integer.
    Raises ValueError if invalid.
    """
    port = int(port_str)
    if port < 1 or port > 65535:
        raise ValueError("Port must be between 1 and 65535.")
    return port

def main():
    print("=== Simple Port Scanner (Educational Use Only) ===")
    host = input("Enter target host (127.0.0.1 or scanme.nmap.org): ").strip()

    if host not in ("127.0.0.1", "localhost", "scanme.nmap.org"):
        print("[ERROR] Unauthorized target. Only localhost and scanme.nmap.org are allowed.")
        return

    try:
        start_port = validate_port(input("Enter start port: ").strip())
        end_port = validate_port(input("Enter end port: ").strip())
        if start_port > end_port:
            raise ValueError("Start port must be less than or equal to end port.")
    except ValueError as e:
        print(f"[ERROR] Invalid port input: {e}")
        return

    print(f"\n[INFO] Scanning {host} from port {start_port} to {end_port} ...")
    start_time = time.time()

    open_ports = []

    for port in range(start_port, end_port + 1):
        is_open = scan_port(host, port)
        status = "OPEN" if is_open else "closed"
        print(f"Port {port}: {status}")
        if is_open:
            open_ports.append(port)

        # Ethical scanning: small delay to avoid aggressive behavior
        time.sleep(0.05)

    duration = time.time() - start_time
    print("\n=== Scan complete ===")
    print(f"Target: {host}")
    print(f"Open ports: {open_ports if open_ports else 'None detected'}")
    print(f"Scan duration: {duration:.2f} seconds")

if __name__ == "__main__":
    main()
