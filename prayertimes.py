#!/usr/bin/python3
import requests
from datetime import datetime

response = requests.request("GET", "http://www.islamicfinder.us/index.php/api/prayer_times?user_ip=101.127.142.238", headers={}, data={})

import json
dataX = json.loads(response.text)
dataX = datetime.strptime(dataX['results']["Maghrib"], "%I:%M %%%p%%")
print(dataX.strftime("%H:%M"))
