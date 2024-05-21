import pytest


def test_setup_not_present(smbus_not_present, LSM303D):
    lsm303d = LSM303D()
    with pytest.raises(RuntimeError):
        lsm303d.setup()


def test_setup_mock_present(smbus, LSM303D):
    lsm303d = LSM303D()
    lsm303d.setup()
