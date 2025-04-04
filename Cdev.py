import os import sys import subprocess import platform import requests import shutil from datetime import datetime

def banner(): print(""" ============================= Termux Multi-Tool v1.0 ============================= 1. Network Scan 2. Whois Lookup 3. DNS Lookup 4. IP Geolocation 5. System Monitor 6. File Management 7. Exit """)

def network_scan(): target = input("Enter target IP/Range: ") os.system(f"nmap -sV {target}")

def whois_lookup(): domain = input("Enter domain: ") os.system(f"whois {domain}")

def dns_lookup(): domain = input("Enter domain: ") os.system(f"nslookup {domain}")

def ip_geolocation(): ip = input("Enter IP Address: ") response = requests.get(f"http://ip-api.com/json/{ip}").json() for key, value in response.items(): print(f"{key}: {value}")

def system_monitor(): print(f"CPU: {platform.processor()}") print(f"System: {platform.system()} {platform.release()}") print(f"Memory: {shutil.disk_usage('/').used / (1024 ** 3)} GB used")

def file_management(): print("1. Compress File") print("2. Encrypt File") print("3. Secure Delete") choice = input("Choose option: ") file_path = input("Enter file path: ") if choice == '1': os.system(f"tar -czvf {file_path}.tar.gz {file_path}") elif choice == '2': key = input("Enter encryption key: ") os.system(f"openssl enc -aes-256-cbc -salt -in {file_path} -out {file_path}.enc -k {key}") elif choice == '3': os.system(f"shred -u {file_path}") else: print("Invalid option.")

def main(): while True: banner() choice = input("Select an option: ") if choice == '1': network_scan() elif choice == '2': whois_lookup() elif choice == '3': dns_lookup() elif choice == '4': ip_geolocation() elif choice == '5': system_monitor() elif choice == '6': file_management() elif choice == '7': print("Exiting...") sys.exit() else: print("Invalid choice.")

if name == "main": main()

