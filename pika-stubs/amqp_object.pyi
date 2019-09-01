# Stubs for pika.amqp_object (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

class AMQPObject:
    NAME: str = ...
    INDEX: Any = ...

class Class(AMQPObject):
    NAME: str = ...

class Method(AMQPObject):
    NAME: str = ...
    synchronous: bool = ...
    def get_properties(self): ...
    def get_body(self): ...

class Properties(AMQPObject):
    NAME: str = ...
