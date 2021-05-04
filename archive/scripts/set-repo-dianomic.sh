#!/usr/bin/env sh


#EC Additions vs lab
#Adjust architecture
#TODO add uname -m for architecture inline?

sudo apt-get -y install automake python-dev python3-dev libpython2.7-dev libpython3.7-dev jq git

#echo "deb [arch=x86_64] http://archives.dianomic.com/foglamp/nightly/ubuntu1804/x86_64/ ./" | sudo tee -a /etc/apt/sources.list.d/foglamp.list
#echo "deb [arch=arm64] http://archives.dianomic.com/foglamp/nightly/mendel/aarch64/ ./" | sudo tee -a /etc/apt/sources.list.d/foglamp.list
echo "deb [arch=armv7l] http://archives.dianomic.com/foglamp/nightly/buster/armv7l/ ./" | sudo tee -a /etc/apt/sources.list.d/foglamp.list

wget -O - http://archives.dianomic.com/KEY.gpg | sudo apt-key add -

sudo apt-get update

sudo apt-get -y install foglamp foglamp-gui

