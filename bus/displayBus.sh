while true
do
  kill -9 $(pidof python3)
  python3 /home/pi/LearningPython/bus/displayBus.py &
  sleep 1m
done
