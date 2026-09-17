import socket

def scan_port(target_ip, port, timeout=1):
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(timeout)
    result = sock.connect_ex((target_ip, port))
    sock.close()
    return result == 0

if __name__ == "__main__":
    ip = socket.gethostbyname("google.com")
    print(f"Resolved IP: {ip}")
    print(f"Port 80 open: {scan_port(ip, 80, timeout=2)}")
    print(f"Port 443 open: {scan_port(ip, 443, timeout=2)}")