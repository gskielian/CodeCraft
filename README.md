Purpose
=======

I really wanted an RTS style log of how many keystrokes per minute I was entering for the lulz.



## What it looks like:
<p align="center">
<img src="Screen Shot 2013-10-14 at 1.51.13 PM.png">
</p>

## Installation && How to Run

```bash
make
sudo ./eventlog &
sudo python APM.py starwars
```


References
----------
Python code is loosely based on [this gist](https://gist.github.com/electronut/5730160) by [electronut](https://github.com/electronut)

eventlog is based on work by[dannvix's](https://github.com/dannvix) 

Mods to keylogger-osx
=====================
 - Removed the part where it logs the actual keys -- as we only need to count the number of **keypress-events**.
 + records the seconds since Unix epoch
