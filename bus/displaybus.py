#!/usr/bin/python3
import requests
from datetime import datetime
import json

headers = {
  'AccountKey': 'YgpFVWKSQzatgONxbRGkyQ==',
  'accept\'': 'application/json'
}

# code adapted from `lcd_i2c.py` starts here.

import smbus
import time

# I2C Address
I2C_ADDR  = 0x3F
LCD_WIDTH = 16

LCD_CHR = 1
LCD_CMD = 0

LCD_LINE_1 = 0x80
LCD_LINE_2 = 0xC0
LCD_LINE_3 = 0x94
LCD_LINE_4 = 0xD4

LCD_BACKLIGHT  = 0x08

ENABLE = 0b00000100

E_PULSE = 0.0005
E_DELAY = 0.0005

#bus = smbus.SMBus(0)  # Rev 1 Pi uses 0
bus = smbus.SMBus(1) # Rev 2 Pi uses 1

def lcd_init():
  lcd_byte(0x33,LCD_CMD)
  lcd_byte(0x32,LCD_CMD)
  lcd_byte(0x06,LCD_CMD)
  lcd_byte(0x0C,LCD_CMD)
  lcd_byte(0x28,LCD_CMD)
  lcd_byte(0x01,LCD_CMD)
  time.sleep(E_DELAY)

def lcd_byte(bits, mode):
  bits_high = mode | (bits & 0xF0) | LCD_BACKLIGHT
  bits_low = mode | ((bits<<4) & 0xF0) | LCD_BACKLIGHT

  bus.write_byte(I2C_ADDR, bits_high)
  lcd_toggle_enable(bits_high)

  bus.write_byte(I2C_ADDR, bits_low)
  lcd_toggle_enable(bits_low)

def lcd_toggle_enable(bits):
  time.sleep(E_DELAY)
  bus.write_byte(I2C_ADDR, (bits | ENABLE))
  time.sleep(E_PULSE)
  bus.write_byte(I2C_ADDR,(bits & ~ENABLE))
  time.sleep(E_DELAY)

def lcd_string(message,line):

    message = message.ljust(LCD_WIDTH," ")

    lcd_byte(line, LCD_CMD)

    for i in range(LCD_WIDTH):
        lcd_byte(ord(message[i]),LCD_CHR)

def main():
  lcd_init()

  while True:

    response = requests.request("GET", "http://datamall2.mytransport.sg/ltaodataservice/BusArrivalv2?BusStopCode=43389", headers=headers, data={})
    dataX = json.loads(response.text)['Services'][2]

    if len(str(dataX['NextBus2']['EstimatedArrival'])) == 25:
        timeX = datetime.strptime(dataX['NextBus']['EstimatedArrival'], "%Y-%m-%dT%H:%M:%S+08:00")
    else:
        print("Error setting timeX: " + str(datetime.strptime(dataX['NextBus']['EstimatedArrival'], "%Y-%m-%dT%H:%M:%S+08:00")))
        timeX = None
    if len(str(dataX['NextBus2']['EstimatedArrival'])) == 25:
        timeY = datetime.strptime(dataX['NextBus2']['EstimatedArrival'], "%Y-%m-%dT%H:%M:%S+08:00")
    else:
        print("Error setting timeY: " + str(datetime.strptime(dataX['NextBus2']['EstimatedArrival'], "%Y-%m-%dT%H:%M:%S+08:00")))
        timeY = None
    if len(str(dataX['NextBus3']['EstimatedArrival'])) == 25:
        timeZ = datetime.strptime(dataX['NextBus3']['EstimatedArrival'], "%Y-%m-%dT%H:%M:%S+08:00")
    else:
        print("Error setting timeZ: " + str(datetime.strptime(dataX['NextBus3']['EstimatedArrival'], "%Y-%m-%dT%H:%M:%S+08:00")))
        timeZ = None

    for x in range(1, 30):
        if len(str(timeX - datetime.now())) == 14:
            x = str(timeX - datetime.now())[2:7]
        else:
            # print("Error printing time to timeX: " + str(timeX - datetime.now()))
            x = 'Arr  '
        if len(str(timeY - datetime.now())) == 14:
            y = str(timeY - datetime.now())[2:7]
        else:
            # print("Error printing time to timeY: " + str(timeX - datetime.now()))
            y = '     '
        if len(str(timeZ - datetime.now())) == 14:
            z = str(timeZ - datetime.now())[2:7]
        else:
            # print("Error printing time to timeZ: " + str(timeX - datetime.now()))
            z = '     '

        lcd_string(x, LCD_LINE_1)
        lcd_string(y + '      ' + z, LCD_LINE_2)

        time.sleep(1)

if __name__ == '__main__':
    main()
    lcd_byte(0x01, LCD_CMD)

# Copyright for part of this code adapted from Matt Hawkins.
#--------------------------------------
#    ___  ___  _ ____
#   / _ \/ _ \(_) __/__  __ __
#  / , _/ ___/ /\ \/ _ \/ // /
# /_/|_/_/  /_/___/ .__/\_, /
#                /_/   /___/
#
#  lcd_i2c.py
#  LCD test script using I2C backpack.
#  Supports 16x2 and 20x4 screens.
#
# Author : Matt Hawkins
# Date   : 20/09/2015
#
# http://www.raspberrypi-spy.co.uk/
#
# Copyright 2015 Matt Hawkins
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#--------------------------------------