import socket

def get_ip(domain: str):
    try:
        ip = socket.gethostbyname(domain)
        return ip
    except socket.gaierror as e:
        return f"Error resolving domain: {e}"

if __name__ == "__main__":
    domain = "weledi.com"
    ip = get_ip(domain)
    print(f"{domain} -> {ip}")
