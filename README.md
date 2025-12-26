# SSH By List

This simple Python script allows you to search for devices from a CSV list and quickly SSH into them.

## Prerequisites

- Python 3 installed on your system.
- An SSH client available in your system's PATH.

## Setup

1.  Ensure you have `main.py` and `devices.csv` in the same directory.
2.  Edit `devices.csv` to include your list of devices. The format should be:

    ```csv
    Hostname,IP
    Device-Name,192.168.1.10
    Another-Device,10.0.0.5
    ```

## Usage

Run the script with a search keyword as an argument:

```bash
python3 main.py <keyword>
```

### Example

To search for devices containing "SG1" in their hostname:

```bash
python3 main.py SG1
```

1.  The script will list all matching devices found in `devices.csv`.
2.  Select the device you want to connect to by entering its number.
3.  Enter the username for the SSH connection.
4.  The script will initiate the SSH session.

## Features

- **Search**: Filter devices by hostname using a keyword (case-insensitive).
- **Auto-connect**: Automatically runs the `ssh` command with the selected IP.
- **Host Key Verification**: Temporarily disables strict host key checking (`StrictHostKeyChecking=no`) and uses `/dev/null` for known hosts to avoid cluttering your local `known_hosts` file and to facilitate connecting to devices that might be re-imaged often.

## File Structure

- `main.py`: The main Python script.
- `devices.csv`: The data file containing device Hostnames and IP addresses.
