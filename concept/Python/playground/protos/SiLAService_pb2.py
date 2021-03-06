# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: SiLAService.proto

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
    name='SiLAService.proto',
    package='SiLAService',
    syntax='proto3',
    serialized_pb=_b('\n\x11SiLAService.proto\x12\x0bSiLAService\"\x07\n\x05\x45mpty\"r\n\x0eIsSiLAResponse\x12\x14\n\x0cserialNumber\x18\x01 \x01(\x03\x12\x14\n\x0cmanufacturer\x18\x02 \x01(\t\x12\r\n\x05model\x18\x03 \x01(\t\x12%\n\x07\x66\x65\x61ture\x18\x04 \x03(\x0b\x32\x14.SiLAService.Feature\"\x7f\n\x07\x46\x65\x61ture\x12\x12\n\nIdentifier\x18\x01 \x01(\t\x12\x0f\n\x07Version\x18\x02 \x01(\t\x12\x13\n\x0b\x44isplayName\x18\x03 \x01(\t\x12\x13\n\x0b\x44\x65scription\x18\x04 \x01(\t\x12%\n\x07\x63ommand\x18\x05 \x03(\x0b\x32\x14.SiLAService.Command\"r\n\x07\x43ommand\x12\x12\n\nIdentifier\x18\x01 \x01(\t\x12\x13\n\x0b\x44isplayName\x18\x02 \x01(\t\x12\x13\n\x0b\x44\x65scription\x18\x03 \x01(\t\x12)\n\tparameter\x18\x04 \x03(\x0b\x32\x16.SiLAService.Parameter\"I\n\tParameter\x12\x12\n\nIdentifier\x18\x01 \x01(\t\x12\x13\n\x0b\x44isplayName\x18\x02 \x01(\t\x12\x13\n\x0b\x44\x65scription\x18\x03 \x01(\t2J\n\x0bSiLAService\x12;\n\x06IsSiLA\x12\x12.SiLAService.Empty\x1a\x1b.SiLAService.IsSiLAResponse\"\x00\x42\x33\n\x14\x63l.grpc.sila_serviceB\x12sila_service_protoP\x01\xa2\x02\x04silab\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


_EMPTY = _descriptor.Descriptor(
    name='Empty',
    full_name='SiLAService.Empty',
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
    serialized_start=34,
    serialized_end=41,
)


_ISSILARESPONSE = _descriptor.Descriptor(
    name='IsSiLAResponse',
    full_name='SiLAService.IsSiLAResponse',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='serialNumber', full_name='SiLAService.IsSiLAResponse.serialNumber', index=0,
            number=1, type=3, cpp_type=2, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='manufacturer', full_name='SiLAService.IsSiLAResponse.manufacturer', index=1,
            number=2, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='model', full_name='SiLAService.IsSiLAResponse.model', index=2,
            number=3, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='feature', full_name='SiLAService.IsSiLAResponse.feature', index=3,
            number=4, type=11, cpp_type=10, label=3,
            has_default_value=False, default_value=[],
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
    serialized_start=43,
    serialized_end=157,
)


_FEATURE = _descriptor.Descriptor(
    name='Feature',
    full_name='SiLAService.Feature',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='Identifier', full_name='SiLAService.Feature.Identifier', index=0,
            number=1, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='Version', full_name='SiLAService.Feature.Version', index=1,
            number=2, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='DisplayName', full_name='SiLAService.Feature.DisplayName', index=2,
            number=3, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='Description', full_name='SiLAService.Feature.Description', index=3,
            number=4, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='command', full_name='SiLAService.Feature.command', index=4,
            number=5, type=11, cpp_type=10, label=3,
            has_default_value=False, default_value=[],
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
    serialized_start=159,
    serialized_end=286,
)


_COMMAND = _descriptor.Descriptor(
    name='Command',
    full_name='SiLAService.Command',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='Identifier', full_name='SiLAService.Command.Identifier', index=0,
            number=1, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='DisplayName', full_name='SiLAService.Command.DisplayName', index=1,
            number=2, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='Description', full_name='SiLAService.Command.Description', index=2,
            number=3, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='parameter', full_name='SiLAService.Command.parameter', index=3,
            number=4, type=11, cpp_type=10, label=3,
            has_default_value=False, default_value=[],
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
    serialized_start=288,
    serialized_end=402,
)


_PARAMETER = _descriptor.Descriptor(
    name='Parameter',
    full_name='SiLAService.Parameter',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='Identifier', full_name='SiLAService.Parameter.Identifier', index=0,
            number=1, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='DisplayName', full_name='SiLAService.Parameter.DisplayName', index=1,
            number=2, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='Description', full_name='SiLAService.Parameter.Description', index=2,
            number=3, type=9, cpp_type=9, label=1,
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
    serialized_start=404,
    serialized_end=477,
)

_ISSILARESPONSE.fields_by_name['feature'].message_type = _FEATURE
_FEATURE.fields_by_name['command'].message_type = _COMMAND
_COMMAND.fields_by_name['parameter'].message_type = _PARAMETER
DESCRIPTOR.message_types_by_name['Empty'] = _EMPTY
DESCRIPTOR.message_types_by_name['IsSiLAResponse'] = _ISSILARESPONSE
DESCRIPTOR.message_types_by_name['Feature'] = _FEATURE
DESCRIPTOR.message_types_by_name['Command'] = _COMMAND
DESCRIPTOR.message_types_by_name['Parameter'] = _PARAMETER

Empty = _reflection.GeneratedProtocolMessageType('Empty', (_message.Message,), dict(
    DESCRIPTOR=_EMPTY,
    __module__='SiLAService_pb2'
    # @@protoc_insertion_point(class_scope:SiLAService.Empty)
))
_sym_db.RegisterMessage(Empty)

IsSiLAResponse = _reflection.GeneratedProtocolMessageType('IsSiLAResponse', (_message.Message,), dict(
    DESCRIPTOR=_ISSILARESPONSE,
    __module__='SiLAService_pb2'
    # @@protoc_insertion_point(class_scope:SiLAService.IsSiLAResponse)
))
_sym_db.RegisterMessage(IsSiLAResponse)

Feature = _reflection.GeneratedProtocolMessageType('Feature', (_message.Message,), dict(
    DESCRIPTOR=_FEATURE,
    __module__='SiLAService_pb2'
    # @@protoc_insertion_point(class_scope:SiLAService.Feature)
))
_sym_db.RegisterMessage(Feature)

Command = _reflection.GeneratedProtocolMessageType('Command', (_message.Message,), dict(
    DESCRIPTOR=_COMMAND,
    __module__='SiLAService_pb2'
    # @@protoc_insertion_point(class_scope:SiLAService.Command)
))
_sym_db.RegisterMessage(Command)

Parameter = _reflection.GeneratedProtocolMessageType('Parameter', (_message.Message,), dict(
    DESCRIPTOR=_PARAMETER,
    __module__='SiLAService_pb2'
    # @@protoc_insertion_point(class_scope:SiLAService.Parameter)
))
_sym_db.RegisterMessage(Parameter)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b(
    '\n\024cl.grpc.sila_serviceB\022sila_service_protoP\001\242\002\004sila'))
import grpc
from grpc.beta import implementations as beta_implementations
from grpc.beta import interfaces as beta_interfaces
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities


class SiLAServiceStub(object):

    def __init__(self, channel):
        """Constructor.

        Args:
          channel: A grpc.Channel.
        """
        self.IsSiLA = channel.unary_unary(
            '/SiLAService.SiLAService/IsSiLA',
            request_serializer=Empty.SerializeToString,
            response_deserializer=IsSiLAResponse.FromString,
        )


class SiLAServiceServicer(object):

    def IsSiLA(self, request, context):
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SiLAServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'IsSiLA': grpc.unary_unary_rpc_method_handler(
            servicer.IsSiLA,
            request_deserializer=Empty.FromString,
            response_serializer=IsSiLAResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'SiLAService.SiLAService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


class BetaSiLAServiceServicer(object):

    def IsSiLA(self, request, context):
        context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)


class BetaSiLAServiceStub(object):

    def IsSiLA(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
        raise NotImplementedError()
    IsSiLA.future = None


def beta_create_SiLAService_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
    request_deserializers = {
        ('SiLAService.SiLAService', 'IsSiLA'): Empty.FromString,
    }
    response_serializers = {
        ('SiLAService.SiLAService', 'IsSiLA'): IsSiLAResponse.SerializeToString,
    }
    method_implementations = {
        ('SiLAService.SiLAService', 'IsSiLA'): face_utilities.unary_unary_inline(servicer.IsSiLA),
    }
    server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers,
                                                         thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
    return beta_implementations.server(method_implementations, options=server_options)


def beta_create_SiLAService_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
    request_serializers = {
        ('SiLAService.SiLAService', 'IsSiLA'): Empty.SerializeToString,
    }
    response_deserializers = {
        ('SiLAService.SiLAService', 'IsSiLA'): IsSiLAResponse.FromString,
    }
    cardinalities = {
        'IsSiLA': cardinality.Cardinality.UNARY_UNARY,
    }
    stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers,
                                                     response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
    return beta_implementations.dynamic_stub(channel, 'SiLAService.SiLAService', cardinalities, options=stub_options)
# @@protoc_insertion_point(module_scope)
