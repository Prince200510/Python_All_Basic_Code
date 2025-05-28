import socket

def is_valid(ip):
    try:
        socket.inet_aton(ip)
        return True
    except socket.error:
        return False

ip = input('Enter an IP Address:')
if is_valid(ip):
    print('Valid IP Address')
else:
    print('Invalid IP Address')
    

# without socket
def is_valid_ipv4(ip):
    parts = ip.split('.')
    
    if len(parts) != 4:
        return False
    
    for part in parts:
        if not part.isdigit():
            return False
        
        num = int(part)
        if num < 0 or num > 255:
            return False
    return True

ipv4 = input('Enter a ipv4 address :')
if is_valid_ipv4(ipv4):
    print('Valid IPv4 Address')
else:
    print('Invalid IPv4 Address')
        