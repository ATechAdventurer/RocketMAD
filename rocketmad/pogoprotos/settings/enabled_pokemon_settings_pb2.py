# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/settings/enabled_pokemon_settings.proto

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
  name='pogoprotos/settings/enabled_pokemon_settings.proto',
  package='pogoprotos.settings',
  syntax='proto3',
  serialized_pb=_b('\n2pogoprotos/settings/enabled_pokemon_settings.proto\x12\x13pogoprotos.settings\"\x8f\x01\n\x16\x45nabledPokemonSettings\x12P\n\x15\x65nabled_pokemon_range\x18\x03 \x03(\x0b\x32\x31.pogoprotos.settings.EnabledPokemonSettings.Range\x1a#\n\x05Range\x12\r\n\x05start\x18\x01 \x01(\x05\x12\x0b\n\x03\x65nd\x18\x02 \x01(\x05\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_ENABLEDPOKEMONSETTINGS_RANGE = _descriptor.Descriptor(
  name='Range',
  full_name='pogoprotos.settings.EnabledPokemonSettings.Range',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='start', full_name='pogoprotos.settings.EnabledPokemonSettings.Range.start', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='end', full_name='pogoprotos.settings.EnabledPokemonSettings.Range.end', index=1,
      number=2, type=5, cpp_type=1, label=1,
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
  serialized_start=184,
  serialized_end=219,
)

_ENABLEDPOKEMONSETTINGS = _descriptor.Descriptor(
  name='EnabledPokemonSettings',
  full_name='pogoprotos.settings.EnabledPokemonSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='enabled_pokemon_range', full_name='pogoprotos.settings.EnabledPokemonSettings.enabled_pokemon_range', index=0,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_ENABLEDPOKEMONSETTINGS_RANGE, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=76,
  serialized_end=219,
)

_ENABLEDPOKEMONSETTINGS_RANGE.containing_type = _ENABLEDPOKEMONSETTINGS
_ENABLEDPOKEMONSETTINGS.fields_by_name['enabled_pokemon_range'].message_type = _ENABLEDPOKEMONSETTINGS_RANGE
DESCRIPTOR.message_types_by_name['EnabledPokemonSettings'] = _ENABLEDPOKEMONSETTINGS

EnabledPokemonSettings = _reflection.GeneratedProtocolMessageType('EnabledPokemonSettings', (_message.Message,), dict(

  Range = _reflection.GeneratedProtocolMessageType('Range', (_message.Message,), dict(
    DESCRIPTOR = _ENABLEDPOKEMONSETTINGS_RANGE,
    __module__ = 'pogoprotos.settings.enabled_pokemon_settings_pb2'
    # @@protoc_insertion_point(class_scope:pogoprotos.settings.EnabledPokemonSettings.Range)
    ))
  ,
  DESCRIPTOR = _ENABLEDPOKEMONSETTINGS,
  __module__ = 'pogoprotos.settings.enabled_pokemon_settings_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.settings.EnabledPokemonSettings)
  ))
_sym_db.RegisterMessage(EnabledPokemonSettings)
_sym_db.RegisterMessage(EnabledPokemonSettings.Range)


# @@protoc_insertion_point(module_scope)
