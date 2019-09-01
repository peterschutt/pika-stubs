# Stubs for pika.compat (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

import socket
from typing import Any

PY2: Any
PY3: Any
RE_NUM: Any
SOCKET_ERROR = socket.error
SOCKET_ERROR = OSError
SOL_TCP: Any
basestring: Any
str_or_bytes: Any
xrange = range
unicode_type = str

def dictkeys(dct: Any): ...
def dictvalues(dct: Any): ...
def dict_iteritems(dct: Any): ...
def dict_itervalues(dct: Any): ...
def byte(*args: Any): ...

class long(int): ...

def canonical_str(value: Any): ...
def is_integer(value: Any): ...
basestring = basestring
str_or_bytes = basestring
xrange = xrange
unicode_type = unicode
dictkeys: Any
dictvalues: Any
dict_iteritems: Any
dict_itervalues: Any
byte = chr
long = long

def as_bytes(value: Any): ...
def to_digit(value: Any): ...
def get_linux_version(release_str: Any): ...

HAVE_SIGNAL: Any
EINTR_IS_EXPOSED: Any
LINUX_VERSION: Any
