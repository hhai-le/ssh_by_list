#!/usr/bin/env python3
import csv
import subprocess
import sys
import os

device_list = "./devices.csv"

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
    hostname, ip = matches[choice]

    # Prompt for username
    username = input(f"Username for {hostname}: ").strip()
    if not username:
        print("Username cannot be empty.")
        sys.exit(1)

    print(f"Connecting as {username} to {ip} ...")

    # SSH options to bypass host key verification
    ssh_opts = [
        "-o", "StrictHostKeyChecking=no",
        "-o", "UserKnownHostsFile=/dev/null"
    ]

    if os.name == 'nt':
        subprocess.run(["ssh"] + ssh_opts + [f"{username}@{ip}"], shell=True)
    elif os.name == 'posix':
        subprocess.run(["ssh"] + ssh_opts + [f"{username}@{ip}"])
else:
    print("Invalid choice.")
