# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: net_conn.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import primitive_pb2 as primitive__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0enet_conn.proto\x12\x08net_conn\x1a\x0fprimitive.proto\"\x92\x02\n\x0f\x43onnectionEvent\x12,\n\x06\x63losed\x18\x01 \x01(\x0b\x32\x1a.net_conn.ClosedConnectionH\x00\x12.\n\x07\x65victed\x18\x02 \x01(\x0b\x32\x1b.net_conn.EvictedConnectionH\x00\x12.\n\x07inbound\x18\x03 \x01(\x0b\x32\x1b.net_conn.InboundConnectionH\x00\x12\x30\n\x08outbound\x18\x04 \x01(\x0b\x32\x1c.net_conn.OutboundConnectionH\x00\x12\x36\n\x0bmisbehaving\x18\x05 \x01(\x0b\x32\x1f.net_conn.MisbehavingConnectionH\x00\x42\x07\n\x05\x65vent\"w\n\nConnection\x12\x0f\n\x07peer_id\x18\x01 \x02(\x04\x12\x0c\n\x04\x61\x64\x64r\x18\x02 \x02(\t\x12&\n\tconn_type\x18\x03 \x02(\x0e\x32\x13.primitive.ConnType\x12\x0f\n\x07network\x18\x04 \x02(\r\x12\x11\n\tnet_group\x18\x05 \x02(\x04\"P\n\x10\x43losedConnection\x12\"\n\x04\x63onn\x18\x01 \x02(\x0b\x32\x14.net_conn.Connection\x12\x18\n\x10time_established\x18\x02 \x02(\x04\"Q\n\x11\x45victedConnection\x12\"\n\x04\x63onn\x18\x01 \x02(\x0b\x32\x14.net_conn.Connection\x12\x18\n\x10time_established\x18\x02 \x02(\x04\"U\n\x11InboundConnection\x12\"\n\x04\x63onn\x18\x01 \x02(\x0b\x32\x14.net_conn.Connection\x12\x1c\n\x14\x65xisting_connections\x18\x02 \x02(\x04\"V\n\x12OutboundConnection\x12\"\n\x04\x63onn\x18\x01 \x02(\x0b\x32\x14.net_conn.Connection\x12\x1c\n\x14\x65xisting_connections\x18\x02 \x02(\x04\"\x7f\n\x15MisbehavingConnection\x12\n\n\x02id\x18\x01 \x02(\x04\x12\x14\n\x0cscore_before\x18\x02 \x02(\x05\x12\x16\n\x0escore_increase\x18\x03 \x02(\x05\x12\x10\n\x08xmessage\x18\x04 \x02(\t\x12\x1a\n\x12threshold_exceeded\x18\x05 \x02(\x08')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'net_conn_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _CONNECTIONEVENT._serialized_start=46
  _CONNECTIONEVENT._serialized_end=320
  _CONNECTION._serialized_start=322
  _CONNECTION._serialized_end=441
  _CLOSEDCONNECTION._serialized_start=443
  _CLOSEDCONNECTION._serialized_end=523
  _EVICTEDCONNECTION._serialized_start=525
  _EVICTEDCONNECTION._serialized_end=606
  _INBOUNDCONNECTION._serialized_start=608
  _INBOUNDCONNECTION._serialized_end=693
  _OUTBOUNDCONNECTION._serialized_start=695
  _OUTBOUNDCONNECTION._serialized_end=781
  _MISBEHAVINGCONNECTION._serialized_start=783
  _MISBEHAVINGCONNECTION._serialized_end=910
# @@protoc_insertion_point(module_scope)