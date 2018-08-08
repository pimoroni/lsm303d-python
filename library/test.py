import time
from lsm303d import LSM303D

lsm = LSM303D(0x1e)

while True:
    t = lsm.temperature()
    m = ''
    a = ''
    h = 0
    t_raw = lsm._lsm303d.values['TEMPERATURE']
    m = lsm.magnetometer()
    a = lsm.accelerometer()
    print("{:04.1f} {:016b}".format(t, t_raw))
    print(m, a)
    time.sleep(1)
