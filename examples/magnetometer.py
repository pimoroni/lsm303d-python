#!/usr/bin/env python

import time
from lsm303d import LSM303D

lsm = LSM303D(0x1d) # Change to 0x1e if you have soldered the address jumper

while True:
    xyz = lsm.magnetometer()

    print(("{:+06.2f} : {:+06.2f} : {:+06.2f}").format(*xyz))

    time.sleep(1.0/50)
