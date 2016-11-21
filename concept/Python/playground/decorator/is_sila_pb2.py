# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: is_sila.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import stdlib_pb2 as stdlib__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='is_sila.proto',
  package='org.sila_standard.v2.realease_candidate.is_sila',
  syntax='proto3',
  serialized_pb=_b('\n\ris_sila.proto\x12/org.sila_standard.v2.realease_candidate.is_sila\x1a\x0cstdlib.proto2m\n\x07is_sila\x12\'\n\x04wsdl\x12\r.stdlib.Empty\x1a\x0e.stdlib.String\"\x00\x12\x39\n\x16sila_interface_version\x12\r.stdlib.Empty\x1a\x0e.stdlib.String\"\x00\x62\x06proto3')
  ,
  dependencies=[stdlib__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)





import grpc
from grpc.beta import implementations as beta_implementations
from grpc.beta import interfaces as beta_interfaces
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities


class is_silaStub(object):
  """Feature "is_sila"
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.wsdl = channel.unary_unary(
        '/org.sila_standard.v2.realease_candidate.is_sila.is_sila/wsdl',
        request_serializer=stdlib__pb2.Empty.SerializeToString,
        response_deserializer=stdlib__pb2.String.FromString,
        )
    self.sila_interface_version = channel.unary_unary(
        '/org.sila_standard.v2.realease_candidate.is_sila.is_sila/sila_interface_version',
        request_serializer=stdlib__pb2.Empty.SerializeToString,
        response_deserializer=stdlib__pb2.String.FromString,
        )


class is_silaServicer(object):
  """Feature "is_sila"
  """

  def wsdl(self, request, context):
    """Property: WSDL
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def sila_interface_version(self, request, context):
    """Property: SiLA Interface Version
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_is_silaServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'wsdl': grpc.unary_unary_rpc_method_handler(
          servicer.wsdl,
          request_deserializer=stdlib__pb2.Empty.FromString,
          response_serializer=stdlib__pb2.String.SerializeToString,
      ),
      'sila_interface_version': grpc.unary_unary_rpc_method_handler(
          servicer.sila_interface_version,
          request_deserializer=stdlib__pb2.Empty.FromString,
          response_serializer=stdlib__pb2.String.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'org.sila_standard.v2.realease_candidate.is_sila.is_sila', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class Betais_silaServicer(object):
  """Feature "is_sila"
  """
  def wsdl(self, request, context):
    """Property: WSDL
    """
    context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
  def sila_interface_version(self, request, context):
    """Property: SiLA Interface Version
    """
    context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)


class Betais_silaStub(object):
  """Feature "is_sila"
  """
  def wsdl(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
    """Property: WSDL
    """
    raise NotImplementedError()
  wsdl.future = None
  def sila_interface_version(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
    """Property: SiLA Interface Version
    """
    raise NotImplementedError()
  sila_interface_version.future = None


def beta_create_is_sila_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
  request_deserializers = {
    ('org.sila_standard.v2.realease_candidate.is_sila.is_sila', 'sila_interface_version'): stdlib__pb2.Empty.FromString,
    ('org.sila_standard.v2.realease_candidate.is_sila.is_sila', 'wsdl'): stdlib__pb2.Empty.FromString,
  }
  response_serializers = {
    ('org.sila_standard.v2.realease_candidate.is_sila.is_sila', 'sila_interface_version'): stdlib__pb2.String.SerializeToString,
    ('org.sila_standard.v2.realease_candidate.is_sila.is_sila', 'wsdl'): stdlib__pb2.String.SerializeToString,
  }
  method_implementations = {
    ('org.sila_standard.v2.realease_candidate.is_sila.is_sila', 'sila_interface_version'): face_utilities.unary_unary_inline(servicer.sila_interface_version),
    ('org.sila_standard.v2.realease_candidate.is_sila.is_sila', 'wsdl'): face_utilities.unary_unary_inline(servicer.wsdl),
  }
  server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
  return beta_implementations.server(method_implementations, options=server_options)


def beta_create_is_sila_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
  request_serializers = {
    ('org.sila_standard.v2.realease_candidate.is_sila.is_sila', 'sila_interface_version'): stdlib__pb2.Empty.SerializeToString,
    ('org.sila_standard.v2.realease_candidate.is_sila.is_sila', 'wsdl'): stdlib__pb2.Empty.SerializeToString,
  }
  response_deserializers = {
    ('org.sila_standard.v2.realease_candidate.is_sila.is_sila', 'sila_interface_version'): stdlib__pb2.String.FromString,
    ('org.sila_standard.v2.realease_candidate.is_sila.is_sila', 'wsdl'): stdlib__pb2.String.FromString,
  }
  cardinalities = {
    'sila_interface_version': cardinality.Cardinality.UNARY_UNARY,
    'wsdl': cardinality.Cardinality.UNARY_UNARY,
  }
  stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
  return beta_implementations.dynamic_stub(channel, 'org.sila_standard.v2.realease_candidate.is_sila.is_sila', cardinalities, options=stub_options)
# @@protoc_insertion_point(module_scope)
