import sys
import mock
import pytest


def test_setup_not_present():
    sys.modules['smbus'] = mock.MagicMock()
    from lsm303d import LSM303D
    lsm303d = LSM303D()
    with pytest.raises(RuntimeError):
        lsm303d.setup()


def test_setup_mock_present():
    from tools import SMBusFakeDevice
    smbus = mock.Mock()
    smbus.SMBus = SMBusFakeDevice
    sys.modules['smbus'] = smbus
    from lsm303d import LSM303D
    lsm303d = LSM303D()
    lsm303d.setup()
