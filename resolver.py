import socket

def resolve_ip_to_hostname(ip_address):
    try:
        hostname, _, _ = socket.gethostbyaddr(ip_address)
        return f"{ip_address} resolved to hostname: {hostname}"
    except socket.herror:
        return f"Error resolving {ip_address}: Not a valid IP address"

def resolve_hostname_to_ip(hostname):
    try:
        ip = socket.gethostbyname(hostname)
        return f"{hostname} resolved to IP address: {ip}"
    except socket.gaierror as e:
        return f"Error resolving {hostname}: {e}"

def main():
    menu = "[1] Resolve IP address to hostname\n[2] Resolve hostname to IP address\n"
    choice = input(menu)

    if choice == '1':
        input_value = input("Enter an IP address: ")
        print(resolve_ip_to_hostname(input_value))
    elif choice == '2':
        input_value = input("Enter a hostname or domain name: ")
        print(resolve_hostname_to_ip(input_value))
    else:
        print("Invalid choice. Please enter '1' or '2' for IP address or hostname resolution.")

if __name__ == "__main__":
    main()
