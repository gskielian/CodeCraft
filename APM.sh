#!/bin/bash

for i in `seq 1 60`; do
apmarray[3]='Suse'

while [ 1 ] ; do
apm=`wc -l /var/log/keystroke.log | awk '{print $1}'`
sleep 1
clear
figlet $apm
done

