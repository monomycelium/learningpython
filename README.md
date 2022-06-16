# LearningPython

Isn't Python immaculate? From data oversight to delightful games, the plethora of things you can accomplish is compelling. This repository holds my documentation of what I have been learning through Python. Relish all the blunders I've made!

## Bus Arrival Time

I used LTA's DataMall API to find the estimated arrival time of a particular service at a bus stop using Python.

### `bus.py`

`bus.py` is a Python script that prints the data.

### `interactiveBus.py`

`interactiveBus.py` is another Python script that uses user inputs to show the arrival times for other bus stops.

### `displayBus`

`displayBus.py` displays the data in an I2C LCD connected to a Raspberry Pi. `displayBus.sh` is a script to refresh the data from the API since it was mind-boggling to do so when there was already a loop running to refresh the display every second to match the time.

To run this, use this command on a Raspberry Pi connected to a 16 by 2 I2C LCD:

```
nohup /home/pi/LearningPython/bus/displayBus.sh &
```

An error might be that the address of your I2C LCD is incorrect inside `displayBus.py`. Another common address aside from `0x3F` is `0x27`, but you might have to check your datasheet or use a program to find yours.

To stop the process, run this command:

```
sudo kill -9 $(pidof /bin/sh /home/pi/LearningPython/bus/displayBus.sh python3)
```