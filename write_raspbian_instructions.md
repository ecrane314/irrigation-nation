# Write OS to SDCard
https://desertbot.io/blog/setup-pi-zero-w-headless-wifi. Download from official site and sha256 hash to check the download is correct

`shasum -a 256 <file>` and compare to site.

## dd to disk
Use dd to write img disk image. `diskutil list` and unmount your disk e.g. `diskutil unmountDisk /dev/disk2`

Confirm input and output then write image to card

`sudo dd bs=1m if=~/Downloads/2020-02-13-raspbian-buster-lite.img of=/dev/disk2`

[headless setup](https://www.raspberrypi.com/documentation/computers/configuration.html#setting-up-a-headless-raspberry-pi)

## Allow ssh
The presense of ssh file lets you login. Do this on new sd card boot volume. `touch /Volumes/boot/ssh`

## Setup Network
Wpa supplicant utility lets it learn your network. Format file as below. Check ssh touch step if you have since booted

`vim /Volumes/boot/wpa_supplicant.conf`

```ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
country=<Insert 2 letter ISO 3166-1 country code here>
update_config=1

network={
 ssid="<Name of your wireless LAN>"
 psk="<Password for your wireless LAN>"
}
```

## Post boot
Check this file after booting. Remove plaintext passwords if encoded version is there

`vim /etc/wpa_supplicant/wpa_supplicant.conf`
