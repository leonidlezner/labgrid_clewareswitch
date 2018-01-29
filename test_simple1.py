import pytest

from labgrid.protocol import CommandProtocol
from clewareswitch.resource import ClewareSwitch
from clewareswitch.driver import ClewareSwitchDriver

import time

def test_target(target):
    switch = target.get_driver(ClewareSwitchDriver)

    #switch.on(0)
    #switch.off(0)

    switch.all_off()

    time.sleep(1)

    switch.all_toggle()

    print("serial", switch.device.serial)

    #assert 'OK' in result
