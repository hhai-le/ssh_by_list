#!/usr/bin/env python
import csv
import getpass
import subprocess
import sys
import os


device_list="devices.csv"

# Get the current user
current_user_full = getpass.getuser()
username_parts = current_user_full.split('@')
username_only = username_parts[0]

# Get the keyword to search devices
if len(sys.argv) < 2:
    print("Usage: python3 run_on_devices.py <keyword>")
    sys.exit(1)

keyword = sys.argv[1].lower()

# Read CSV
matches = []
with open("devices.csv", newline="") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if keyword in row["Hostname"].lower():
            matches.append((row["Hostname"], row["IP"]))

if not matches:
    print("No matching devices found.")
    sys.exit(0)

# Show results
for i, (hostname, _) in enumerate(matches, start=1):
    print(f"{i}. {hostname}")

# Choose device
choice = int(input("Choose a device to SSH: ")) - 1
if 0 <= choice < len(matches):
    ip = matches[choice][1]
    print(f"Connecting as {username_only} to {ip} ...")
    if os.name == 'nt':
        subprocess.run(["ssh", f"{current_user_full}@{ip}"],shell=True)
    elif os.name == 'posix':
        subprocess.run(["ssh", f"{username_only}@{ip}"])
else:
    print("Invalid choice.")
