import socket

def scan_port(target_ip, port, timeout=1):
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(timeout)
    result = sock.connect_ex((target_ip, port))
    sock.close()
    return result == 0

if __name__ == "__main__":
    scann= {
        21 : "FTP",
        22 : "SSH",
        23 : "Telnet",
        25 : "SMTP",
        53 : "DNS",
        80 : "HTTP",
        443 : "HTTPS",
        3389 : "RDP"
    }
    ip = socket.gethostbyname("google.com")
    
    #print(f"Port 443 open: {scan_port(ip, 443, timeout=2)}")
    j = 443
    if scan_port(ip,j,timeout = 1): #scannn[] using this returns error for values that are not in key like 1, 2, 3,..it gives error whereas scann.get() never 
        scany = scann.get(j, "Unknown")
        print(f"Port {j} open = {scany}")

    for i in range(1,101):
        if scan_port(ip, i, timeout = 1 ):
            scany = scann.get(i , "Unknown")
            print(f"Port {i} open = {scany}")



r'''for i in range(1,101):
        print(f"Port {i} open: {scan_port(ip,i, timeout = 1)}")'''
r'''    print(f"Resolved IP: {ip}")
    print(f"Port 80 open: {scan_port(ip, 80, timeout=2)}")
    print(f"Port 443 open: {scan_port(ip, 443, timeout=2)}")'''