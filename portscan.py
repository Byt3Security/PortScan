import socket
import os
import subprocess
import sys
from colorama import init, Fore, Back

ip = input("IP: ")
portas = range(1, 65536)
subprocess.run("clear")
print(Fore.MAGENTA + "▀█████████▄  ▄██   ▄       ███        ▄████████    ▄████████    ▄████████  ▄████████ ")
print(Fore.MAGENTA + "  ███    ███ ███   ██▄ ▀█████████▄   ███    ███   ███    ███   ███    ███ ███    ███ ")
print(Fore.MAGENTA + "  ███    ███ ███▄▄▄███    ▀███▀▀██   ███    █▀    ███    █▀    ███    █▀  ███    █▀ ")
print(Fore.MAGENTA + " ▄███▄▄▄██▀  ▀▀▀▀▀▀███     ███   ▀  ▄███▄▄▄       ███         ▄███▄▄▄     ███        ")
print(Fore.MAGENTA + "▀▀███▀▀▀██▄  ▄██   ███     ███     ▀▀███▀▀▀     ▀███████████ ▀▀███▀▀▀     ███        ")
print(Fore.MAGENTA + "███    ██▄ ███   ███     ███       ███    █▄           ███   ███    █▄  ███    █▄ ")
print(Fore.MAGENTA + "███    ███ ███   ███     ███       ███    ███    ▄█    ███   ███    ███ ███    ███ ")
print(Fore.MAGENTA + "▄█████████▀   ▀█████▀     ▄████▀     ██████████  ▄████████▀    ██████████ ████████▀ \r\n ")

try:
    resolved_ip = socket.gethostbyname(ip)
    print(f"{ip} ---> {resolved_ip}")
except socket.gaierror:
    print(f"Error resolving IP: {ip}")
    sys.exit()


for porta in portas:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)  # Set a timeout for faster scanning

    res = sock.connect_ex((ip, porta))
    if res == 0:
        print(f"Porta {porta} ABERTA!")
        
     
        try:
            banner = sock.recv(1024)
            print(f"Banner for porta {porta}: {banner.decode().strip()}")
        except Exception:
            print(f"Não existe um banner nessa porta:  {porta}")

    sock.close()

