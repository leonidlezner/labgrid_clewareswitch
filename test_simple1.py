import pytest

from labgrid.protocol import CommandProtocol

from clewareswitch.resource import ClewareSwitch
from clewareswitch.driver import ClewareSwitchDriver

def test_target(target):
    #command = target.get_driver(CommandProtocol)
    #result = command.run_check('echo OK')


    d = target.get_driver(ClewareSwitchDriver)

    d.on(1)

    print("serialnumber", d.device.serialnumber)

    #assert 'OK' in result
