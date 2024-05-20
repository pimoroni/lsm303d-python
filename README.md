# lsm303d Accelerometer And Compass

[![Build Status](https://shields.io/github/workflow/status/pimoroni/lsm303d-python/Python%20Tests.svg)](https://github.com/pimoroni/sgp30-python/actions/workflows/test.yml)
[![Coverage Status](https://coveralls.io/repos/github/pimoroni/lsm303d-python/badge.svg?branch=master)](https://coveralls.io/github/pimoroni/lsm303d-python?branch=master)
[![PyPi Package](https://img.shields.io/pypi/v/lsm303d.svg)](https://pypi.python.org/pypi/lsm303d)
[![Python Versions](https://img.shields.io/pypi/pyversions/lsm303d.svg)](https://pypi.python.org/pypi/lsm303d)

Suitable for measuring orientation and motion, the lsm303d has a 3-axis accelerometer and compass.

# Installing

Stable library from PyPi:

* Just run `python3 -m pip install lsm303d`

Latest/development library from GitHub:

* `git clone https://github.com/pimoroni/lsm303d-python`
* `cd lsm303d-python`
* `sudo ./install.sh --unstable`


# Changelog
0.0.5
-----

* Require i2cdevice>=0.0.6

0.0.4
-----

* Port to i2cdevice>=0.0.6 set/get API

0.0.3
-----

* BugFix: Fix for compatibility with i2cdevice>=0.0.6

0.0.2
-----

* Bumped i2cdevice dependency to >=0.0.4

0.0.1
-----

* Initial Release
