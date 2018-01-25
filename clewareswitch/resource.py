import attr

from labgrid.factory import target_factory
from labgrid.resource.common import Resource

@target_factory.reg_resource
@attr.s(cmp=False)
class ClewareSwitch(Resource):
    """The ClewareSwitch describes a USB switch made by Cleware
    Args:
        serial (int): serial number of the switch
    """
    serial = attr.ib(validator=attr.validators.instance_of(int))




