#!/usr/bin/env python

import time
from lsm303d import LSM303D

lsm = LSM303D(0x1d) # Change to 0x1e if you have soldered the address jumper

while True:
    raw_heading = lsm.raw_heading()
    heading = lsm.heading()

    print(("raw heading: {:0.0f} degrees, compensated heading: {:0.0f} degrees").format(raw_heading, heading))

    time.sleep(1.0/50)
