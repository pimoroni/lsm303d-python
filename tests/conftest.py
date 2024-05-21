import sys

import mock
import pytest
from tools import SMBusFakeDevice


@pytest.fixture()
def smbus_not_present():
    sys.modules['smbus2'] = mock.MagicMock()
    yield sys.modules['smbus2']
    del sys.modules['smbus2']


@pytest.fixture()
def smbus():
    sys.modules['smbus2'] = mock.MagicMock()
    sys.modules['smbus2'].SMBus = SMBusFakeDevice
    yield sys.modules['smbus2']
    del sys.modules['smbus2']


@pytest.fixture()
def LSM303D():
    from lsm303d import LSM303D
    yield LSM303D
    del sys.modules['lsm303d']