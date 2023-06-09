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




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13webcontroller.proto\"&\n\x16MoveInformationRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"r\n\x14MoveInformationReply\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04stop\x18\x02 \x01(\x08\x12\r\n\x05speed\x18\x03 \x01(\x05\x12\x11\n\tdirection\x18\x04 \x01(\t\x12\x0c\n\x04turn\x18\x05 \x01(\t\x12\x0e\n\x06radius\x18\x06 \x01(\x01\"\x93\x01\n\x1eMoveInformationReplyWithStatus\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04stop\x18\x02 \x01(\x08\x12\r\n\x05speed\x18\x03 \x01(\x05\x12\x11\n\tdirection\x18\x04 \x01(\t\x12\x0c\n\x04turn\x18\x05 \x01(\t\x12\x0e\n\x06radius\x18\x06 \x01(\x01\x12\x15\n\rpassedToRobot\x18\x07 \x01(\x08\",\n\x1aMoveInformationHasNewReply\x12\x0e\n\x06hasNew\x18\x01 \x01(\x08\"F\n\x17MoveInformationSendLeft\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05speed\x18\x03 \x01(\x05\x12\x0e\n\x06radius\x18\x06 \x01(\x01\"G\n\x18MoveInformationSendRight\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05speed\x18\x03 \x01(\x05\x12\x0e\n\x06radius\x18\x06 \x01(\x01\"H\n\x19MoveInformationSendCenter\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05speed\x18\x03 \x01(\x05\x12\x0e\n\x06radius\x18\x06 \x01(\x01\"I\n\x1aMoveInformationSendForward\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05speed\x18\x03 \x01(\x05\x12\x0e\n\x06radius\x18\x06 \x01(\x01\"J\n\x1bMoveInformationSendBackward\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05speed\x18\x03 \x01(\x05\x12\x0e\n\x06radius\x18\x06 \x01(\x01\"5\n\x17MoveInformationSendStop\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04stop\x18\x02 \x01(\x08\x32\xbc\x0b\n\x05\x41gent\x12\x43\n\x0fMoveInformation\x12\x17.MoveInformationRequest\x1a\x15.MoveInformationReply\"\x00\x12P\n\x1bMoveInformationDeliveryLeft\x12\x18.MoveInformationSendLeft\x1a\x15.MoveInformationReply\"\x00\x12R\n\x1cMoveInformationDeliveryRight\x12\x19.MoveInformationSendRight\x1a\x15.MoveInformationReply\"\x00\x12T\n\x1dMoveInformationDeliveryCenter\x12\x1a.MoveInformationSendCenter\x1a\x15.MoveInformationReply\"\x00\x12V\n\x1eMoveInformationDeliveryForward\x12\x1b.MoveInformationSendForward\x1a\x15.MoveInformationReply\"\x00\x12X\n\x1fMoveInformationDeliveryBackward\x12\x1c.MoveInformationSendBackward\x1a\x15.MoveInformationReply\"\x00\x12U\n!MoveInformationDeliveryChangeLeft\x12\x17.MoveInformationRequest\x1a\x15.MoveInformationReply\"\x00\x12V\n\"MoveInformationDeliveryChangeRight\x12\x17.MoveInformationRequest\x1a\x15.MoveInformationReply\"\x00\x12[\n\'MoveInformationDeliveryChangeLeftChange\x12\x17.MoveInformationRequest\x1a\x15.MoveInformationReply\"\x00\x12\\\n(MoveInformationDeliveryChangeRightChange\x12\x17.MoveInformationRequest\x1a\x15.MoveInformationReply\"\x00\x12W\n#MoveInformationDeliveryChangeCenter\x12\x17.MoveInformationRequest\x1a\x15.MoveInformationReply\"\x00\x12X\n$MoveInformationDeliveryChangeForward\x12\x17.MoveInformationRequest\x1a\x15.MoveInformationReply\"\x00\x12Y\n%MoveInformationDeliveryChangeBackward\x12\x17.MoveInformationRequest\x1a\x15.MoveInformationReply\"\x00\x12P\n\x1bMoveInformationDeliveryStop\x12\x18.MoveInformationSendStop\x1a\x15.MoveInformationReply\"\x00\x12Z\n\x1cMoveInformationGetLastSended\x12\x17.MoveInformationRequest\x1a\x1f.MoveInformationReplyWithStatus\"\x00\x12I\n\x15MoveInformationGetNew\x12\x17.MoveInformationRequest\x1a\x15.MoveInformationReply\"\x00\x12O\n\x15MoveInformationHasNew\x12\x17.MoveInformationRequest\x1a\x1b.MoveInformationHasNewReply\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'webcontroller_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _MOVEINFORMATIONREQUEST._serialized_start=23
  _MOVEINFORMATIONREQUEST._serialized_end=61
  _MOVEINFORMATIONREPLY._serialized_start=63
  _MOVEINFORMATIONREPLY._serialized_end=177
  _MOVEINFORMATIONREPLYWITHSTATUS._serialized_start=180
  _MOVEINFORMATIONREPLYWITHSTATUS._serialized_end=327
  _MOVEINFORMATIONHASNEWREPLY._serialized_start=329
  _MOVEINFORMATIONHASNEWREPLY._serialized_end=373
  _MOVEINFORMATIONSENDLEFT._serialized_start=375
  _MOVEINFORMATIONSENDLEFT._serialized_end=445
  _MOVEINFORMATIONSENDRIGHT._serialized_start=447
  _MOVEINFORMATIONSENDRIGHT._serialized_end=518
  _MOVEINFORMATIONSENDCENTER._serialized_start=520
  _MOVEINFORMATIONSENDCENTER._serialized_end=592
  _MOVEINFORMATIONSENDFORWARD._serialized_start=594
  _MOVEINFORMATIONSENDFORWARD._serialized_end=667
  _MOVEINFORMATIONSENDBACKWARD._serialized_start=669
  _MOVEINFORMATIONSENDBACKWARD._serialized_end=743
  _MOVEINFORMATIONSENDSTOP._serialized_start=745
  _MOVEINFORMATIONSENDSTOP._serialized_end=798
  _AGENT._serialized_start=801
  _AGENT._serialized_end=2269
# @@protoc_insertion_point(module_scope)
