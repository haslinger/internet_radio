# internet_radio
Python script for using a Ubuntu notebook as internet radio appliance (1 key = 1 station)

# Wifi-setup

`/etc/netplan/01-netcfg.yaml`:

```
network:
  version: 2
  renderer: networkd
  ethernets:
    eth1:
      dhcp4: yes
  wifis:
    wlan0:
      dhcp4: yes
      dhcp6: no
      access-points:
        "myssid":
          password: "mypassword"
```

# Auto-Login:

`sudo mkdir  /etc/systemd/system/getty@tty1.service.d`
`sudo nano  /etc/systemd/system/getty@tty1.service.d/override.conf`

```
[Service]
ExecStart=
ExecStart=-/sbin/agetty --autologin myusername --noclear %I $TERM
Type=idle
```

# Update script to latest version


# Tipps:
Disable lirc support (infrared control) by adding to ```~/.mplayer/config```

```
lirc=no
```

* In case headphones are not working delete: `/var/lib/alsa/asound.state`

