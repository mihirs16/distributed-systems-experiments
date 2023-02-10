from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class MatrixReply(_message.Message):
    __slots__ = ["c00", "c01", "c10", "c11"]
    C00_FIELD_NUMBER: _ClassVar[int]
    C01_FIELD_NUMBER: _ClassVar[int]
    C10_FIELD_NUMBER: _ClassVar[int]
    C11_FIELD_NUMBER: _ClassVar[int]
    c00: int
    c01: int
    c10: int
    c11: int
    def __init__(self, c00: _Optional[int] = ..., c01: _Optional[int] = ..., c10: _Optional[int] = ..., c11: _Optional[int] = ...) -> None: ...

class MatrixRequest(_message.Message):
    __slots__ = ["a00", "a01", "a10", "a11", "b00", "b01", "b10", "b11"]
    A00_FIELD_NUMBER: _ClassVar[int]
    A01_FIELD_NUMBER: _ClassVar[int]
    A10_FIELD_NUMBER: _ClassVar[int]
    A11_FIELD_NUMBER: _ClassVar[int]
    B00_FIELD_NUMBER: _ClassVar[int]
    B01_FIELD_NUMBER: _ClassVar[int]
    B10_FIELD_NUMBER: _ClassVar[int]
    B11_FIELD_NUMBER: _ClassVar[int]
    a00: int
    a01: int
    a10: int
    a11: int
    b00: int
    b01: int
    b10: int
    b11: int
    def __init__(self, a00: _Optional[int] = ..., a01: _Optional[int] = ..., a10: _Optional[int] = ..., a11: _Optional[int] = ..., b00: _Optional[int] = ..., b01: _Optional[int] = ..., b10: _Optional[int] = ..., b11: _Optional[int] = ...) -> None: ...
