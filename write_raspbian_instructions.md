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
## Add a user
See link above about headless setup. In the latest releases, April 2022 [pi default use is removed](https://www.raspberrypi.com/news/raspberry-pi-bullseye-update-april-2022/)

`vim userconf.txt` and add `<username>:<encrypted password>`. You can get the encrypted version with OpenSSL in Linux, (MacOS openSSL is different) `echo 'my password' | openssl passwd -6 -stdin`. GCP CloudShell works great for this.

## Post boot
Check this file after booting and ssh'ing in. Remove plaintext passwords if encoded version is there

`vim /etc/wpa_supplicant/wpa_supplicant.conf`
