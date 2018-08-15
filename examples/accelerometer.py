#!/usr/bin/env python

import time
from lsm303d import LSM303D

lsm = LSM303D(0x1e)

while True:
    xyz = lsm.accelerometer()

    print(("{:+06.2f}g : {:+06.2f}g : {:+06.2f}g").format(*xyz))

    time.sleep(1.0/50)
