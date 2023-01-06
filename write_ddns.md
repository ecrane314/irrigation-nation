# Dynamic DNS for remote access


## Install

`sudo apt install ddclient`

This config will go in `/etc/ddclient.conf` which must only be editable by root. Running `sudo ddclient -verbose` will fix the file if permissions are off, check your ip, and push new info to remote registrar on-demand IF different.

## Port Forwarding
Remember port forwarding on router gateway or this does nothing

## Service

You will most likely want it to run in the background and periodically check/update your IP without manual intervention. To do that, you need to configure ddclient to run as daemon by editing the file `sudo vim /etc/default/ddclient`.

Add the line `run_daemon="true"`

Restart to read your new config `sudo service ddclient restart`

## Security Hardening
Enhance password and change default user from pi to something else [using ddclient](https://serdima.wordpress.com/2018/04/23/tutorial-updating-dynamic-dns-with-ddclient/)

## Sample config

See install for where to put this.

```
protocol=dyndns2

use=web

server=domains.google.com

ssl=yes

login=<from registrar ddns config >

password=<from registrar ddns config>

<subdomain without prefix> e.g. sub.domain.com
```