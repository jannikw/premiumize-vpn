#!/usr/bin/env python3

import subprocess
import os

# Available VPN locations
VPN_LOCATIONS = [
    "at",
    "au",
    "be",
    "ca",
    "ch",
    "cz",
    "de",
    "es",
    "fi",
    "fr",
    "gb",
    "gr",
    "it",
    "jp",
    "nl",
    "pl",
    "sg",
    "us",
]

def service_name(location):
    return f"openvpn-client@vpn-{location}.premiumize.me.service"

def get_status(location):
    result = subprocess.run(["systemctl", "status", service_name(location), "--lines=0"], capture_output=True, encoding="utf-8")
    if "Active: failed" in result.stdout:
        return "failed"
    elif "Active: active" in result.stdout:
        return "active"
    elif "Active: inactive" in result.stdout:
        return "inactive"

    raise Exception(f"no status information found in: {result.stdout}")

def get_current_location():
    try:
        with open("vpn-premiumize.location") as file:
            location = file.read()
            if location in VPN_LOCATIONS:
                return location
    except:
        pass
    
    return VPN_LOCATIONS[0]

def set_current_location(location):
    with open("vpn-premiumize.location", mode="w") as file:
        file.write(location)

def cycle_location(location):
    try:
        index = VPN_LOCATIONS.index(location)
        return VPN_LOCATIONS[(index + 1) % len(VPN_LOCATIONS)]
    except:
        return VPN_LOCATIONS[0]

def print_status():
    current_location = get_current_location()
    current_status = get_status(current_location)

    print(f"{current_location}: {current_status}")

if __name__ == "__main__":
    current_location = get_current_location()
    current_status = get_status(current_location)
    
    current_button = os.environ.get("BLOCK_BUTTON", None)
    if current_button == "1":
        if current_status == "active":
            subprocess.run(["sudo", "systemctl", "stop", service_name(current_location)], capture_output=True)
        else:
            subprocess.run(["sudo", "systemctl", "start", service_name(current_location)], capture_output=True)
    elif current_button == "3":
        if current_status != "active":
            next_location = cycle_location(current_location)
            set_current_location(next_location)

    print_status()
