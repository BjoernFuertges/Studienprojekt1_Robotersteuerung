# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: webcontroller.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13webcontroller.proto\"&\n\x16MoveInformationRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"r\n\x14MoveInformationReply\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04stop\x18\x02 \x01(\x08\x12\r\n\x05speed\x18\x03 \x01(\x05\x12\x11\n\tdirection\x18\x04 \x01(\t\x12\x0c\n\x04turn\x18\x05 \x01(\t\x12\x0e\n\x06radius\x18\x06 \x01(\x01\"F\n\x17MoveInformationSendLeft\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05speed\x18\x03 \x01(\x05\x12\x0e\n\x06radius\x18\x06 \x01(\x01\"G\n\x18MoveInformationSendRight\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05speed\x18\x03 \x01(\x05\x12\x0e\n\x06radius\x18\x06 \x01(\x01\"H\n\x19MoveInformationSendCenter\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05speed\x18\x03 \x01(\x05\x12\x0e\n\x06radius\x18\x06 \x01(\x01\"I\n\x1aMoveInformationSendForward\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05speed\x18\x03 \x01(\x05\x12\x0e\n\x06radius\x18\x06 \x01(\x01\"J\n\x1bMoveInformationSendBackward\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05speed\x18\x03 \x01(\x05\x12\x0e\n\x06radius\x18\x06 \x01(\x01\"5\n\x17MoveInformationSendStop\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04stop\x18\x02 \x01(\x08\"\x87\x01\n\x18MoveInformationSendReply\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04stop\x18\x02 \x01(\x08\x12\r\n\x05speed\x18\x03 \x01(\x05\x12\x11\n\tdirection\x18\x04 \x01(\t\x12\x0c\n\x04turn\x18\x05 \x01(\t\x12\x0e\n\x06radius\x18\x06 \x01(\x01\x12\x0f\n\x07success\x18\x07 \x01(\x08\x32\xe4\x04\n\x05\x41gent\x12\x43\n\x0fMoveInformation\x12\x17.MoveInformationRequest\x1a\x15.MoveInformationReply\"\x00\x12T\n\x1bMoveInformationDeliveryLeft\x12\x18.MoveInformationSendLeft\x1a\x19.MoveInformationSendReply\"\x00\x12V\n\x1cMoveInformationDeliveryRight\x12\x19.MoveInformationSendRight\x1a\x19.MoveInformationSendReply\"\x00\x12X\n\x1dMoveInformationDeliveryCenter\x12\x1a.MoveInformationSendCenter\x1a\x19.MoveInformationSendReply\"\x00\x12Z\n\x1eMoveInformationDeliveryForward\x12\x1b.MoveInformationSendForward\x1a\x19.MoveInformationSendReply\"\x00\x12\\\n\x1fMoveInformationDeliveryBackward\x12\x1c.MoveInformationSendBackward\x1a\x19.MoveInformationSendReply\"\x00\x12T\n\x1bMoveInformationDeliveryStop\x12\x18.MoveInformationSendStop\x1a\x19.MoveInformationSendReply\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'webcontroller_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _MOVEINFORMATIONREQUEST._serialized_start=23
  _MOVEINFORMATIONREQUEST._serialized_end=61
  _MOVEINFORMATIONREPLY._serialized_start=63
  _MOVEINFORMATIONREPLY._serialized_end=177
  _MOVEINFORMATIONSENDLEFT._serialized_start=179
  _MOVEINFORMATIONSENDLEFT._serialized_end=249
  _MOVEINFORMATIONSENDRIGHT._serialized_start=251
  _MOVEINFORMATIONSENDRIGHT._serialized_end=322
  _MOVEINFORMATIONSENDCENTER._serialized_start=324
  _MOVEINFORMATIONSENDCENTER._serialized_end=396
  _MOVEINFORMATIONSENDFORWARD._serialized_start=398
  _MOVEINFORMATIONSENDFORWARD._serialized_end=471
  _MOVEINFORMATIONSENDBACKWARD._serialized_start=473
  _MOVEINFORMATIONSENDBACKWARD._serialized_end=547
  _MOVEINFORMATIONSENDSTOP._serialized_start=549
  _MOVEINFORMATIONSENDSTOP._serialized_end=602
  _MOVEINFORMATIONSENDREPLY._serialized_start=605
  _MOVEINFORMATIONSENDREPLY._serialized_end=740
  _AGENT._serialized_start=743
  _AGENT._serialized_end=1355
# @@protoc_insertion_point(module_scope)
