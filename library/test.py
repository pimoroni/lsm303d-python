import time
import lsm303d as lsm

while True:
    t = lsm.temperature()
    m = ''
    a = ''
    h = 0
    t_raw = lsm._lsm303d.values['TEMPERATURE']
    #m = lsm.magnetometer()
    #a = lsm.accelerometer()
    #h = lsm.heading()
    print("{:04.1f} {:016b}".format(t, t_raw))
    time.sleep(1)
