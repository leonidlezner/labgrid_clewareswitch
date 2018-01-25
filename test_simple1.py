import pytest

from labgrid.protocol import CommandProtocol
from clewareswitch.resource import ClewareSwitch
from clewareswitch.driver import ClewareSwitchDriver

def test_target(target):
    switch = target.get_driver(ClewareSwitchDriver)

    switch.on(1)

    print("serial", switch.device.serial)

    #assert 'OK' in result
