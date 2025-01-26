import os
import subprocess

def get_active_ips():
    """Fetch active IP addresses from the ARP table."""
    try:
        if os.name == "nt":  # Windows
            output = subprocess.check_output("arp -a", shell=True, text=True)
        else:  # Linux/Unix
            output = subprocess.check_output("ip neigh", shell=True, text=True)

        active_ips = []
        for line in output.splitlines():
            if "dynamic" in line or "REACHABLE" in line:
                parts = line.split()
                active_ips.append(parts[0])  # IP address

        return active_ips
    except Exception as e:
        print(f"Error fetching ARP table: {e}")
        return []

if __name__ == "__main__":
    active_ips = get_active_ips()
    print("\nActive IP addresses found:\n")
    for ip in active_ips:
        print(ip)
