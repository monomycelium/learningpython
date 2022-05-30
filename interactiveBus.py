import requests
from datetime import datetime
import json

busStop = input('Enter Bus Stop Number: ')
busNumber = input('Enter Bus Number: ')
busStop
if busStop == '':
    busStop = '43389'
if busNumber == '':
    busNumber = '189'

headers = {
  'AccountKey': 'YgpFVWKSQzatgONxbRGkyQ==',
  'accept\'': 'application/json'
}
response = requests.request("GET", "http://datamall2.mytransport.sg/ltaodataservice/BusArrivalv2?BusStopCode=%s" % busStop, headers=headers, data={})

i = 0
for x in json.loads(response.text)['Services']:
    if json.loads(response.text)['Services'][int(i)]['ServiceNo'] == busNumber:
        dataX = json.loads(response.text)['Services'][int(i)]
    else:
        i += 1

if dataX != None:
    print(dataX['ServiceNo'])
    
    if len(str(dataX['NextBus2']['EstimatedArrival'])) == 25:
        timeX = datetime.strptime(dataX['NextBus']['EstimatedArrival'], "%Y-%m-%dT%H:%M:%S+08:00") - datetime.now()
    if len(str(dataX['NextBus2']['EstimatedArrival'])) == 25:
        timeY = datetime.strptime(dataX['NextBus2']['EstimatedArrival'], "%Y-%m-%dT%H:%M:%S+08:00") - datetime.now()
    if len(str(dataX['NextBus3']['EstimatedArrival'])) == 25:
        timeZ = datetime.strptime(dataX['NextBus3']['EstimatedArrival'], "%Y-%m-%dT%H:%M:%S+08:00") - datetime.now()

    if len(str(timeX)) == 14:
        print(str(timeX)[2:7])
    if len(str(timeY)) == 14:
        print(str(timeY)[2:7])
    if len(str(timeZ)) == 14:
        print(str(timeZ)[2:7])