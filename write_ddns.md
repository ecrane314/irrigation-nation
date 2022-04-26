# Dynamic DNS for remote access
This will go in `/etc/ddclient.conf` which must only be editable by root. Running `sudo ddclient` will fix the file if permissions are off and push new info to remote.

## Port Forwarding
Remember port forwarding on router gateway or this does nothing

## Security Hardening
Enhance password and change default user from pi to something else [using ddclient](https://serdima.wordpress.com/2018/04/23/tutorial-updating-dynamic-dns-with-ddclient/)

#TODO  set daemon to update

```
protocol=dyndns2

use=web

server=domains.google.com

ssl=yes

login=<from registrar ddns config >

password=<from registrar ddns config>

<subdomain without prefix> e.g. sub.domain.com
```