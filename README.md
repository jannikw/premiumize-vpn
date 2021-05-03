# Premiumize VPN

This package provides the configurations to easily use the VPN service provided by [premiumize.me](https://www.premiumize.me/ref/506346746).
It installs the OpenVPN configurations at `/etc/openvpn/client/`.
This way a connection can be established using `systemctl start openvpn-client@vpn-{location}.premiumize.me.service`, where `{location}` is any of the [supported locations](https://www.premiumize.me/vpn/locations), for example `us`.
The authentication file at `/etc/openvpn/premiumize-auth.txt` must be adjusted to contains your [customer ID](https://www.premiumize.me/account) in the first line and your [API key](https://www.premiumize.me/account) in the second.

The package also installs a drop-in sudo configuration.
This way any user in the group `wheel` can start and stop a VPN connection using `systemctl start`/`systemctl stop`.

## Installation

The package can be installed on Arch Linux using `makepkg -i`

## i3block Support

The package installs a small script to cycle through the available locations and start/stop a connection using `i3blocks`.
Add something like the following to your `i3blocks`config:
```
[vpn-premiumize]
label=VPN 
interval=5
```
Create a symlink for the blocklet to be called by `i3blocks` using `ln -s vpn-premiumize /opt/vpn-preiumize/vpn-premiumize.py`.
The blocklet cycles through the locations when right-clicked and starts/stops a connection when left-clicked.