import time
from lsm303d import LSM303D

lsm = LSM303D(0x1e)

while True:
    xyz = lsm.accelerometer()

    print(("{:+06.2f} : {:+06.2f} : {:+06.2f}").format(*xyz))

    time.sleep(1.0/50)
