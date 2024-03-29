[WIP] https://guides.github.com/features/mastering-markdown/ 

## Google IoT API [optional]
https://googleapis.dev/python/cloudiot/latest/index.html 
This is to connect and manage devices IE management control plane NOT device data plane.
[TODO] Still need to write APIs for that? Should be client library - HTTP
[TODO] Python requests library

# Irrigation Nation
Digital plant watering system based on Raspberry Pi.

## 1. Install Requirements
First, run the commands in `write_raspbian_instructions.md` to prepare your SD card to boot.
In the likely event you're missing pip on a lite install, 
`sudo apt install python3-pip`. Notice this catches a bunch of other recommended Python packages along with it. 27MB at time of writing Apr 2022. Then, clone this repo and run `pip3 install -r requirements.txt`.

## Run Flask (Optional)
`export FLASK_APP=web_plants.py; flask run`

## 2. Add Scheduler
`crontab -e`
`0 7 2-30/2 * * /home/pi/irrigation-nation/operate_pump.py 120`
https://crontab-generator.org/ for setting and validating your timing
For example, the above will run each morning at 7am for 120 seconds.
Run date to confirm timezone is accurate. Set system clock of device so that Cron works as expected. On Raspberry Pi, use `sudo system-config` then localization and set time zone. On generic linux, this can be done with `sudo timedatectl show-timezones` and `sudo timedatectl set-timezone <TIMEZONE>``

## Github integration [or use Docker]
[GitHub SSH instructions are helpful](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)

`ssh-keygen -t ed25519 -C your@email.com`

`eval "$(ssh-agent -s)"`

`ssh-add ~/.ssh/id_rsa` The private key

Then add the public key to your github account or other
ensure `git remote -v` shows your remotes as ssh destinatinos and not https else it will ask for username and password, not the key.

~/.ssh/config file should have something like this
Host github.com
        AddKeysToAgent yes
        IdentityFile ~/.ssh/github<private key>

## 3. Hardening
Harden your pi by installing uncomplicated firewall, updating default user name, hardening password, and more. Set your routers dhcp to assign it a specific address (often outside DHCP range) so that you can still ssh even while the hostname is changing in local DNS cache. Use the [RasPi Security Guide](https://www.raspberrypi.com/documentation/computers/configuration.html#securing-your-raspberry-pi)

Create your key as above. 

Run `ssh-copy-id -i ~/.ssh/id_rsa.pub user@remote-host` and you'll be prompted for a password to copy your public key to the authorized_hosts file of the pi.

On the local machine, run `ssh-agent $SHELL` to start the agent and `ssh-add <key>` to add your key. From here, you can ssh without a password.

`ufw` Uncomplicated Firewall. Need to be sudo to manage, but need only to allow TCP 22 to setup access. Remember, don't expose 22 directly to the internet. `sudo ufw allow 22/tcp` and `sudo ufw enable`. `sudo ufw status`

## 4. Install DDNS on your device and enable port forwarding
Setup Dynamic DNS at your registrar eg domains.google.com, and then write the configuration. Example in write_ddns.txt

Port map on your router so that your special port reaches the device e.g. 3434 > 22 TCP and perhaps set a static route for the device in case you forget the hostname or are changing it and need to be able to connect.

To disable ipv6 on adapters, `sudo nano /etc/sysctl.conf` and add line `net.ipv6.conf.default.disable_ipv6=1` 


## 5. Install Docker
https://docs.docker.com/engine/install/debian/ 
Use Debian instructions except change the URL for the actual site to Raspbian
```echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/raspbian \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```

## 6. Install Monitoring Agent [optional]
This brings CPU, Memory, Disk, Network and syslog all to GCP for central observability
https://cloud.google.com/monitoring/agent/monitoring/installation 
As of May 4, not built and available for arm64 architecture. The folders are present in the repo, but empty. Remember to add `[arch=arm64]` in the `/etc/apt/sources` listing file.

## Troubleshooting
I used the pre-installed `iwconfig` to check the number of retries, link quality, and link speed when packages were timing out coming down from `pip`. I also use the Speedtest.net CLI version to check my internet end-to-end connectivity. [Ookla CLI](https://www.speedtest.net/apps/cli). It turns out moving a metal broom handle and the surge protector cable further from the pi improved dramatically 5 Mbps to 60 Mbps.

## Hardware
[Raspi Pinout](https://pinout.xyz/)
For the [Sense Hat](https://pythonhosted.org/sense-hat/), use the raspi package instead of pip to install, `sudo apt-get install sense-hat`


### Additional Credit
With explanation & inspiration from https://www.hackster.io/ben-eagan/raspberry-pi-automated-plant-watering-with-website-8af2dc


# Future

Dockerfile for water plants

```
from python-3 . Lite?
sudo apt update && sudo apt upgrade
sudo apt install git ufw
pip install -r requirements.txt
add .

.sh shell script to install ufw, configure, 
ddns // Needs to pull in config at runtime as has password in it
// GCP service account?

CMD python operate-pump.py

```