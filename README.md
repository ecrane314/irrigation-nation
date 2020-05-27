[WIP] https://guides.github.com/features/mastering-markdown/ 

# Irrigation Nation
Digital plant watering system based on Raspberry Pi.

## 1. Install Requirements
`pip3 install -r requirements.txt`
## 3. Run Flask (Optional)
`export FLASK_APP=web_plants.py; flask run`

## 2. Add Scheduler
`crontab -e`
`/usr/bin/python3 <absolute path to pump_test.py`
https://crontab-generator.org/ for setting your timing


### Additional Credit
With inspiration from https://www.hackster.io/ben-eagan/raspberry-pi-automated-plant-watering-with-website-8af2dc
> specifically, the inclusion of flask-based front end
