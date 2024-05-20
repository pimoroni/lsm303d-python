import time
from lsm303d import LSM303D

lsm = LSM303D(0x1e)

while True:
    t = lsm.temperature()
    m = lsm.magnetometer()
    a = lsm.accelerometer()
    #t_raw = lsm._lsm303d.values['TEMPERATURE']
    #print("{:04.1f} {:016b}".format(t, t_raw))

    values = list(m) + list(a)

    print(("{:+06.2f} : {:+06.2f} : {:+06.2f}   " * 2).format(*values))

    time.sleep(1.0/25)
