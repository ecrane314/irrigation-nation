[WIP] https://guides.github.com/features/mastering-markdown/ 

# Irrigation Nation
Digital plant watering system based on Raspberry Pi.

## 1. Install Requirements
#in case you're missing pip
`sudo apt install python3-pip`
`pip3 install -r requirements.txt`
## Run Flask (Optional)
`export FLASK_APP=web_plants.py; flask run`

## 2. Add Scheduler
`crontab -e`
`/usr/bin/python3 <absolute path to pump_test.py`
https://crontab-generator.org/ for setting your timing
For example
`0 7 * * * /usr/bin/python3 /home/pi/irrigation-nation/operate_pump.py 120 > /home/pi/log.out` Will run each morning at 7am for 120 seconds.
`0 7 1-31/2 * * /usr/bin/python3 /home/pi/irrigation-nation/operate_pump.py 120 > /home/pi/log.out` Will run every other morning at 7am.

Set system clock of device so that Cron works as expected. On Raspberry Pi, use `sudo system-config` then localization and set time zone. On generic linux, this can be done with `sudo timedatectl show-timezones` and `sudo timedatectl set-timezone <TIMEZONE>``


`ssh-keygen -t ed25512 -C your@email.com`
`eval "$(ssh-agent -s)"`
`ssh-add ~/.ssh/id_rsa` The private key
Then add the public key to your github account or other
ensure `git remote -v` shows your remotes as ssh destinatinos and not https else it will ask for username and password, not the key.


~/.ssh/config file should have something like this
Host github.com
        AddKeysToAgent yes
        IdentityFile ~/.ssh/github<private key>


### Additional Credit
With inspiration from https://www.hackster.io/ben-eagan/raspberry-pi-automated-plant-watering-with-website-8af2dc
> specifically, the inclusion of flask-based front end


