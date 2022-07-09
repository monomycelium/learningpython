#!/usr/bin/python3
import psutil
mem = psutil.virtual_memory()
print(str(mem.percent) + '%')
