# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/settings/passcode_settings.proto

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
  name='pogoprotos/settings/passcode_settings.proto',
  package='pogoprotos.settings',
  syntax='proto3',
  serialized_pb=_b('\n+pogoprotos/settings/passcode_settings.proto\x12\x13pogoprotos.settings\"K\n\x10PasscodeSettings\x12\x1e\n\x16show_passcode_in_store\x18\x01 \x01(\x08\x12\x17\n\x0fuse_passcode_v2\x18\x02 \x01(\x08\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_PASSCODESETTINGS = _descriptor.Descriptor(
  name='PasscodeSettings',
  full_name='pogoprotos.settings.PasscodeSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='show_passcode_in_store', full_name='pogoprotos.settings.PasscodeSettings.show_passcode_in_store', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='use_passcode_v2', full_name='pogoprotos.settings.PasscodeSettings.use_passcode_v2', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=68,
  serialized_end=143,
)

DESCRIPTOR.message_types_by_name['PasscodeSettings'] = _PASSCODESETTINGS

PasscodeSettings = _reflection.GeneratedProtocolMessageType('PasscodeSettings', (_message.Message,), dict(
  DESCRIPTOR = _PASSCODESETTINGS,
  __module__ = 'pogoprotos.settings.passcode_settings_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.settings.PasscodeSettings)
  ))
_sym_db.RegisterMessage(PasscodeSettings)


# @@protoc_insertion_point(module_scope)