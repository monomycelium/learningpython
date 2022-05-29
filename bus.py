import requests
from datetime import datetime
import json

url = "http://datamall2.mytransport.sg/ltaodataservice/BusArrivalv2?BusStopCode=43389"
payload={}
headers = {
  'AccountKey': 'YgpFVWKSQzatgONxbRGkyQ==',
  'accept\'': 'application/json'
}
response = requests.request("GET", url, headers=headers, data=payload)
dataX = json.loads(response.text)['Services'][2]

timeX = datetime.strptime(dataX['NextBus']['EstimatedArrival'], "%Y-%m-%dT%H:%M:%S+08:00") - datetime.now()
timeY = datetime.strptime(dataX['NextBus2']['EstimatedArrival'], "%Y-%m-%dT%H:%M:%S+08:00") - datetime.now()
if len(str(dataX['NextBus3']['EstimatedArrival'])) == len(str(dataX['NextBus2']['EstimatedArrival'])):
    timeZ = datetime.strptime(dataX['NextBus3']['EstimatedArrival'], "%Y-%m-%dT%H:%M:%S+08:00") - datetime.now()

if len(str(timeX)) == len(str(timeY)):
    print(str(timeX)[2:7])
print(str(timeY)[2:7])
if len(str(dataX['NextBus3']['EstimatedArrival'])) == len(str(dataX['NextBus2']['EstimatedArrival'])):
    print(str(timeZ)[2:7])