# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: device.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import SiLAService_pb2 as SiLAService__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='device.proto',
  package='service',
  syntax='proto3',
  serialized_pb=_b('\n\x0c\x64\x65vice.proto\x12\x07service\x1a\x11SiLAService.proto\"\x1f\n\rStreamRequest\x12\x0e\n\x06length\x18\x01 \x01(\x05\"A\n\tDatapoint\x12\r\n\x05value\x18\x01 \x01(\x01\x12%\n\x04unit\x18\x02 \x01(\x0e\x32\x17.service.TemperaturUnit*9\n\x0eTemperaturUnit\x12\x0b\n\x07\x43\x45LCIUS\x10\x00\x12\n\n\x06KELVIN\x10\x01\x12\x0e\n\nFAHRENHEIT\x10\x02\x32\x8b\x01\n\x0bThermometer\x12\x37\n\x0bTemperature\x12\x12.SiLAService.Empty\x1a\x12.service.Datapoint\"\x00\x12\x43\n\x11TemperatureStream\x12\x16.service.StreamRequest\x1a\x12.service.Datapoint\"\x00\x30\x01\x42%\n\x0e\x63l.grpc.deviceB\x0b\x64\x65viceProtoP\x01\xa2\x02\x03\x64\x65vb\x06proto3')
  ,
  dependencies=[SiLAService__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_TEMPERATURUNIT = _descriptor.EnumDescriptor(
  name='TemperaturUnit',
  full_name='service.TemperaturUnit',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='CELCIUS', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='KELVIN', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAHRENHEIT', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=144,
  serialized_end=201,
)
_sym_db.RegisterEnumDescriptor(_TEMPERATURUNIT)

TemperaturUnit = enum_type_wrapper.EnumTypeWrapper(_TEMPERATURUNIT)
CELCIUS = 0
KELVIN = 1
FAHRENHEIT = 2



_STREAMREQUEST = _descriptor.Descriptor(
  name='StreamRequest',
  full_name='service.StreamRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='length', full_name='service.StreamRequest.length', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=44,
  serialized_end=75,
)


_DATAPOINT = _descriptor.Descriptor(
  name='Datapoint',
  full_name='service.Datapoint',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='service.Datapoint.value', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unit', full_name='service.Datapoint.unit', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=77,
  serialized_end=142,
)

_DATAPOINT.fields_by_name['unit'].enum_type = _TEMPERATURUNIT
DESCRIPTOR.message_types_by_name['StreamRequest'] = _STREAMREQUEST
DESCRIPTOR.message_types_by_name['Datapoint'] = _DATAPOINT
DESCRIPTOR.enum_types_by_name['TemperaturUnit'] = _TEMPERATURUNIT

StreamRequest = _reflection.GeneratedProtocolMessageType('StreamRequest', (_message.Message,), dict(
  DESCRIPTOR = _STREAMREQUEST,
  __module__ = 'device_pb2'
  # @@protoc_insertion_point(class_scope:service.StreamRequest)
  ))
_sym_db.RegisterMessage(StreamRequest)

Datapoint = _reflection.GeneratedProtocolMessageType('Datapoint', (_message.Message,), dict(
  DESCRIPTOR = _DATAPOINT,
  __module__ = 'device_pb2'
  # @@protoc_insertion_point(class_scope:service.Datapoint)
  ))
_sym_db.RegisterMessage(Datapoint)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\016cl.grpc.deviceB\013deviceProtoP\001\242\002\003dev'))
import grpc
from grpc.beta import implementations as beta_implementations
from grpc.beta import interfaces as beta_interfaces
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities


class ThermometerStub(object):
  """Thermometer Service Definition
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Temperature = channel.unary_unary(
        '/service.Thermometer/Temperature',
        request_serializer=SiLAService__pb2.Empty.SerializeToString,
        response_deserializer=Datapoint.FromString,
        )
    self.TemperatureStream = channel.unary_stream(
        '/service.Thermometer/TemperatureStream',
        request_serializer=StreamRequest.SerializeToString,
        response_deserializer=Datapoint.FromString,
        )


class ThermometerServicer(object):
  """Thermometer Service Definition
  """

  def Temperature(self, request, context):
    """Sends the current seconds
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def TemperatureStream(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ThermometerServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Temperature': grpc.unary_unary_rpc_method_handler(
          servicer.Temperature,
          request_deserializer=SiLAService__pb2.Empty.FromString,
          response_serializer=Datapoint.SerializeToString,
      ),
      'TemperatureStream': grpc.unary_stream_rpc_method_handler(
          servicer.TemperatureStream,
          request_deserializer=StreamRequest.FromString,
          response_serializer=Datapoint.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'service.Thermometer', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class BetaThermometerServicer(object):
  """Thermometer Service Definition
  """
  def Temperature(self, request, context):
    """Sends the current seconds
    """
    context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
  def TemperatureStream(self, request, context):
    context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)


class BetaThermometerStub(object):
  """Thermometer Service Definition
  """
  def Temperature(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
    """Sends the current seconds
    """
    raise NotImplementedError()
  Temperature.future = None
  def TemperatureStream(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
    raise NotImplementedError()


def beta_create_Thermometer_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
  request_deserializers = {
    ('service.Thermometer', 'Temperature'): SiLAService__pb2.Empty.FromString,
    ('service.Thermometer', 'TemperatureStream'): StreamRequest.FromString,
  }
  response_serializers = {
    ('service.Thermometer', 'Temperature'): Datapoint.SerializeToString,
    ('service.Thermometer', 'TemperatureStream'): Datapoint.SerializeToString,
  }
  method_implementations = {
    ('service.Thermometer', 'Temperature'): face_utilities.unary_unary_inline(servicer.Temperature),
    ('service.Thermometer', 'TemperatureStream'): face_utilities.unary_stream_inline(servicer.TemperatureStream),
  }
  server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
  return beta_implementations.server(method_implementations, options=server_options)


def beta_create_Thermometer_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
  request_serializers = {
    ('service.Thermometer', 'Temperature'): SiLAService__pb2.Empty.SerializeToString,
    ('service.Thermometer', 'TemperatureStream'): StreamRequest.SerializeToString,
  }
  response_deserializers = {
    ('service.Thermometer', 'Temperature'): Datapoint.FromString,
    ('service.Thermometer', 'TemperatureStream'): Datapoint.FromString,
  }
  cardinalities = {
    'Temperature': cardinality.Cardinality.UNARY_UNARY,
    'TemperatureStream': cardinality.Cardinality.UNARY_STREAM,
  }
  stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
  return beta_implementations.dynamic_stub(channel, 'service.Thermometer', cardinalities, options=stub_options)
# @@protoc_insertion_point(module_scope)