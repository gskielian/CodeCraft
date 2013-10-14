#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python
################################################################################
# showdata.py
#
# Display analog data from Arduino using Python (matplotlib)
# 
# electronut.in
#
################################################################################

import subprocess
import sys, serial
import numpy as np
from time import sleep
from collections import deque

def file_len(fname):
  with open(fname) as f:
    for i, l in enumerate(f):
      pass
    f.close()
    return i + 1

def main():

  total_lines=file_len("/var/log/keystroke.log")
  aList=[]
  for i in range(0,1000):
    aList.append(total_lines)
  index=0;
  vel_lines=0;
  apm=0;
  while True:
    try:
      total_lines=file_len("/var/log/keystroke.log")
      aList.insert(0,total_lines)
      aList.pop()
      vel_lines = aList[0] - aList[99]
      apm = aList[0] - aList[599]
      subprocess.call("figlet -f " + str(sys.argv[1]) +  " APT = "  + str(vel_lines/10)  + '; figlet -f ' + str(sys.argv[1]) +  ' \"APM = ' + str(apm) + '\"', shell=True)
      sleep(0.1)
      subprocess.call("clear",shell=True) 
    except KeyboardInterrupt:
      print 'exiting'
      break
  # close serial

# call main
if __name__ == '__main__':
  main()
