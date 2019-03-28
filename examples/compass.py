#!/usr/bin/env python

import time
import math
from lsm303d import LSM303D


def raw_heading(minimums, maximums, zero=0):
    """Return a raw compass heading calculated from the magnetometer data."""

    X = 0
    Y = 2  # Change to 1 if you have the breakout flat

    mag_range = 2
    mag = list(lsm.magnetometer())

    for i in range(len(mag)):
        mag[i] = ((mag_range / (maximums[i] - minimums[i])) * mag[i]) - \
                 (mag_range / 2.0)

    heading = math.atan2(mag[Y], mag[X])

    if heading < 0:
        heading += (2 * math.pi)

    heading_degrees = (round(math.degrees(heading), 2) - zero) % 360

    return heading_degrees


lsm = LSM303D(0x1d)  # Change to 0x1e if you have soldered the address jumper

try:
    input = raw_input
except NameError:
    pass

input("Lay your LSM303D in Breakout Garden flat (LSM303D vertical), \n\
press a key to start, then rotate it 360 degrees, keeping it flat...\n")

t_start = time.time()
t_elapsed = 0

minimums = list(lsm.magnetometer())
maximums = list(lsm.magnetometer())

while t_elapsed < 30:
    mag = lsm.magnetometer()
    for i in range(len(mag)):
        if mag[i] < minimums[i]:
            minimums[i] = mag[i]
        if mag[i] > maximums[i]:
            maximums[i] = mag[i]
    t_elapsed = time.time() - t_start

input("Calibration complete!\n\nIf you want to set a zero (North) point, \n\
then turn your breakout to that point and press a key...\n")

zero = raw_heading(minimums, maximums)

input("Press a key to begin readings!\n")

while True:
    rh = raw_heading(minimums, maximums, zero=zero)
    print("compass heading: {:0.0f} degrees".format(rh, h))
    time.sleep(0.1)
