import attr
import cleware

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
        
        self.usb = None
        self.device_index = None
        self.num_of_outputs = 8
        
        usb = cleware.CUSBaccess()

        n_devices = usb.OpenCleware()

        for i in range(n_devices):
            devType = usb.GetUSBType(i)
            version = usb.GetVersion(i)
            serial = usb.GetSerialNumber(i)
            
            # Check the serial number
            if serial == self.device.serial:
                ret = usb.ResetDevice(i)
                ret = usb.StartDevice(i)
                #TODO: Check the return value

                self.usb = usb
                self.device_index = i

                # Bring all switches to a defined state
                self.all_off()

                break
            else:
                self.usb = None

        if self.usb is None:
            raise Exception('Can not find any connected Cleware Switches with serial number "{}"'.format(self.device.serial))

    def __del__(self):
        if self.usb is not None:
            self.usb.CloseCleware()

    def check_device(self):
        if self.usb is None or self.device_index is None:
            raise Excpetion('No switch device connected')

    def on(self, index):
        self.check_device()
        self.usb.SetSwitch(self.device_index, 16 + index, 1)

    def off(self, index):
        self.check_device()
        self.usb.SetSwitch(self.device_index, 16 + index, 0)

    def is_on(self, index):
        self.check_device()
        if self.usb.GetSwitch(self.device_index, 16 + index) == 1:
            return True
        else:
            return False

    def all_on(self):
        for i in range(self.num_of_outputs):
            self.on(i)

    def all_off(self):
        for i in range(self.num_of_outputs):
            self.off(i)

    def toggle(self, index):
        self.check_device()
        if self.is_on(index):
            self.off(index)
        else:
            self.on(index)

    def all_toggle(self):
        for i in range(self.num_of_outputs):
            self.toggle(i)


