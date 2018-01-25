import attr

from labgrid.factory import target_factory
from labgrid.driver.common import Driver
from .protocol import SwitchProtocol
from .resource import ClewareSwitch

@target_factory.reg_driver
@attr.s(cmp=False)
class ClewareSwitchDriver(Driver, SwitchProtocol):
    bindings = { 'device': ClewareSwitch }

    def __attrs_post_init__(self):
        super().__attrs_post_init__()

    # TODO: Method for cleaning up

    def on(self, index):
        raise NotImplementedError

    def off(self, index):
        raise NotImplementedError

    def all_on(self):
        raise NotImplementedError

    def all_off(self):
        raise NotImplementedError


