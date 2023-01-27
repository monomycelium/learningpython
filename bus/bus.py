#!/usr/bin/env python3
import requests
from datetime import datetime
import json
import sys

def fetch_data(bus_stop):
    return(json.loads(requests.request("GET", "http://datamall2.mytransport.sg/ltaodataservice/BusArrivalv2?BusStopCode=%s" % bus_stop, headers={ 'AccountKey': 'YgpFVWKSQzatgONxbRGkyQ==' }, data={}).text)["Services"])

def extract_map(data, bus_service):
    for x in data:
        if x["ServiceNo"] == bus_service:
            break

    if x["ServiceNo"] != bus_service:
        print("bus service `%s` not found in bus stop `%s`. here are other buses that stop there: " % (bus_service, bus_stop))
        list_services(data)
        sys.exit(1)

def list_services(data):
    for x in data:
        print(x["ServiceNo"])

bus_stop = "43389"
bus_service = "189"

data = fetch_data(bus_stop)

extract_map(data, bus_service)

print(x['ServiceNo'])

if len(str(x['NextBus']['EstimatedArrival'])) == 25:
    timeX = datetime.strptime(x['NextBus']['EstimatedArrival'], "%Y-%m-%dT%H:%M:%S+08:00") - datetime.now()
else:
    timeX = None
if len(str(x['NextBus2']['EstimatedArrival'])) == 25:
    timeY = datetime.strptime(x['NextBus2']['EstimatedArrival'], "%Y-%m-%dT%H:%M:%S+08:00") - datetime.now()
else:
    timeY = None
if len(str(x['NextBus3']['EstimatedArrival'])) == 25:
    timeZ = datetime.strptime(x['NextBus3']['EstimatedArrival'], "%Y-%m-%dT%H:%M:%S+08:00") - datetime.now()
else:
    timeZ = None

if len(str(timeX)) == 14:
    print(str(timeX)[2:7])
if len(str(timeY)) == 14:
    print(str(timeY)[2:7])
if len(str(timeZ)) == 14:
    print(str(timeZ)[2:7])