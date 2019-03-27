#!/usr/bin/env python

import time
import math
from lsm303d import LSM303D

def raw_heading(minimums, maximums):
    """Return a raw compass heading calculated from the magnetometer data."""

    X = 0
    Y = 1
    Z = 2

    mag_range = 0.5
    mag = list(lsm.magnetometer())

    for i in range(len(mag)):
        mag[i] = (mag_range / (maximums[i] - minimums[i]) * mag[i]) - (mag_range / 2.0)

    print(mag[:2])
    heading = math.atan2(mag[Y], mag[X])

    if heading < 0:
        heading += 2 * math.pi

    heading_degrees = round(math.degrees(heading), 2)

    return heading_degrees

def heading(minimums, maximums):
    """Return a tilt compensated heading calculated from the magnetometer data.
    Returns None in the case of a calculation error.
    """

    X = 0
    Y = 1
    Z = 2

    mag_range = 0.5
    mag = list(lsm.magnetometer())

    for i in range(len(mag)):
        mag[i] = (mag_range / (maximums[i] - minimums[i]) * mag[i]) - (mag_range / 2.0)

    acc = lsm.accelerometer()

    truncate = [0,0,0]

    for i in range(X, Z+1):
        truncate[i] = math.copysign(min(math.fabs(acc[i]), 1.0), acc[i])
    try:
        pitch = math.asin(-1 * truncate[X])
        roll = math.asin(truncate[Y] / math.cos(pitch)) if abs(math.cos(pitch)) >= abs(truncate[Y]) else 0
        # set roll to zero if pitch approaches -1 or 1

        tiltcomp = [0, 0, 0]
        tiltcomp[X] = mag[X] * math.cos(pitch) + mag[Z] * math.sin(pitch)
        tiltcomp[Y] = mag[X] * math.sin(roll) * math.sin(pitch) + \
                      mag[Y] * math.cos(roll) - mag[Z] * math.sin(roll) * math.cos(pitch)
        tiltcomp[Z] = mag[X] * math.cos(roll) * math.sin(pitch) + \
                      mag[Y] * math.sin(roll) + \
                      mag[Z] * math.cos(roll) * math.cos(pitch)
        tilt_heading = math.atan2(tiltcomp[Y], tiltcomp[X])

        if tilt_heading < 0:
            tilt_heading += 2 * math.pi

        tilt_heading_degrees = round(math.degrees(tilt_heading), 2)
        return tilt_heading_degrees

    except Exception as e:
        print(e)
        return None

lsm = LSM303D(0x1d) # Change to 0x1e if you have soldered the address jumper

try:
    input = raw_input
except NameError:
    pass

input("Press a key to begin calibration and then rotate your LSM303D sensor through every axis of rotation...\n")

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

input("Calibration complete! Press a key to continue...\n")

while True:
    rh = raw_heading(minimums, maximums)
    h = heading(minimums, maximums)
    print("raw heading: {:0.0f} degrees, compensated heading: {:0.0f} degrees".format(rh, h))
    time.sleep(0.1)
