import time
import lsm303d
import smbus

bus = smbus.SMBus(1)

lsm = lsm303d.lsm303d(bus, addr=0x1e)

while True:
    t = lsm.temperature()
    m = lsm.magnetometer()
    a = lsm.accelerometer()
    h = lsm.heading()
    print(t, str(m), str(a), h)
    time.sleep(1)
