# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: stdlib.proto

import sys
_b = sys.version_info[0] < 3 and (
    lambda x: x) or (lambda x: x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor.FileDescriptor(
    name='stdlib.proto',
    package='stdlib',
    syntax='proto3',
    serialized_pb=_b('\n\x0cstdlib.proto\x12\x06stdlib\"\x07\n\x05\x45mpty\"\x16\n\x06String\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\t\"\x16\n\x06\x44ouble\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x01\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


_EMPTY = _descriptor.Descriptor(
    name='Empty',
    full_name='stdlib.Empty',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
    ],
    extensions=[
    ],
    nested_types=[],
    enum_types=[
    ],
    options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=24,
    serialized_end=31,
)


_STRING = _descriptor.Descriptor(
    name='String',
    full_name='stdlib.String',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='data', full_name='stdlib.String.data', index=0,
            number=1, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
    ],
    extensions=[
    ],
    nested_types=[],
    enum_types=[
    ],
    options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=33,
    serialized_end=55,
)


_DOUBLE = _descriptor.Descriptor(
    name='Double',
    full_name='stdlib.Double',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='data', full_name='stdlib.Double.data', index=0,
            number=1, type=1, cpp_type=5, label=1,
            has_default_value=False, default_value=float(0),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
    ],
    extensions=[
    ],
    nested_types=[],
    enum_types=[
    ],
    options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=57,
    serialized_end=79,
)

DESCRIPTOR.message_types_by_name['Empty'] = _EMPTY
DESCRIPTOR.message_types_by_name['String'] = _STRING
DESCRIPTOR.message_types_by_name['Double'] = _DOUBLE

Empty = _reflection.GeneratedProtocolMessageType('Empty', (_message.Message,), dict(
    DESCRIPTOR=_EMPTY,
    __module__='stdlib_pb2'
    # @@protoc_insertion_point(class_scope:stdlib.Empty)
))
_sym_db.RegisterMessage(Empty)

String = _reflection.GeneratedProtocolMessageType('String', (_message.Message,), dict(
    DESCRIPTOR=_STRING,
    __module__='stdlib_pb2'
    # @@protoc_insertion_point(class_scope:stdlib.String)
))
_sym_db.RegisterMessage(String)

Double = _reflection.GeneratedProtocolMessageType('Double', (_message.Message,), dict(
    DESCRIPTOR=_DOUBLE,
    __module__='stdlib_pb2'
    # @@protoc_insertion_point(class_scope:stdlib.Double)
))
_sym_db.RegisterMessage(Double)


import grpc
from grpc.beta import implementations as beta_implementations
from grpc.beta import interfaces as beta_interfaces
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities
# @@protoc_insertion_point(module_scope)
