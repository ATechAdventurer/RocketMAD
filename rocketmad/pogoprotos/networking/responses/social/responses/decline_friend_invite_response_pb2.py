# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/responses/social/responses/decline_friend_invite_response.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/responses/social/responses/decline_friend_invite_response.proto',
  package='pogoprotos.networking.responses.social.responses',
  syntax='proto3',
  serialized_pb=_b('\nUpogoprotos/networking/responses/social/responses/decline_friend_invite_response.proto\x12\x30pogoprotos.networking.responses.social.responses\"\xfc\x01\n\x1b\x44\x65\x63lineFriendInviteResponse\x12\x64\n\x06result\x18\x01 \x01(\x0e\x32T.pogoprotos.networking.responses.social.responses.DeclineFriendInviteResponse.Result\"w\n\x06Result\x12\t\n\x05UNSET\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\x11\n\rERROR_UNKNOWN\x10\x02\x12\x1f\n\x1b\x45RROR_INVITE_DOES_NOT_EXIST\x10\x03\x12!\n\x1d\x45RROR_INVITE_ALREADY_DECLINED\x10\x04\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_DECLINEFRIENDINVITERESPONSE_RESULT = _descriptor.EnumDescriptor(
  name='Result',
  full_name='pogoprotos.networking.responses.social.responses.DeclineFriendInviteResponse.Result',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSET', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUCCESS', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_UNKNOWN', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_INVITE_DOES_NOT_EXIST', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_INVITE_ALREADY_DECLINED', index=4, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=273,
  serialized_end=392,
)
_sym_db.RegisterEnumDescriptor(_DECLINEFRIENDINVITERESPONSE_RESULT)


_DECLINEFRIENDINVITERESPONSE = _descriptor.Descriptor(
  name='DeclineFriendInviteResponse',
  full_name='pogoprotos.networking.responses.social.responses.DeclineFriendInviteResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='pogoprotos.networking.responses.social.responses.DeclineFriendInviteResponse.result', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _DECLINEFRIENDINVITERESPONSE_RESULT,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=140,
  serialized_end=392,
)

_DECLINEFRIENDINVITERESPONSE.fields_by_name['result'].enum_type = _DECLINEFRIENDINVITERESPONSE_RESULT
_DECLINEFRIENDINVITERESPONSE_RESULT.containing_type = _DECLINEFRIENDINVITERESPONSE
DESCRIPTOR.message_types_by_name['DeclineFriendInviteResponse'] = _DECLINEFRIENDINVITERESPONSE

DeclineFriendInviteResponse = _reflection.GeneratedProtocolMessageType('DeclineFriendInviteResponse', (_message.Message,), dict(
  DESCRIPTOR = _DECLINEFRIENDINVITERESPONSE,
  __module__ = 'pogoprotos.networking.responses.social.responses.decline_friend_invite_response_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.responses.social.responses.DeclineFriendInviteResponse)
  ))
_sym_db.RegisterMessage(DeclineFriendInviteResponse)


# @@protoc_insertion_point(module_scope)
