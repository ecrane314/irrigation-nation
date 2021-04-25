# Kiosk Installation

Referenced https://desertbot.io/blog/raspberry-pi-touchscreen-kiosk-setup

## Desktop Auto Login asks to install below, 600+ MB
sudo apt-get install lightdm

## Install these without extras to get Chromium going
sudo apt-get install --no-install-recommends xserver-xorg x11-xserver-utils xinit openbox

Openbox window manager will be configured to launch Chromium