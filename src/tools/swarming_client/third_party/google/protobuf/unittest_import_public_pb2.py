# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/protobuf/unittest_import_public.proto

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
  name='google/protobuf/unittest_import_public.proto',
  package='protobuf_unittest_import',
  syntax='proto2',
  serialized_pb=_b('\n,google/protobuf/unittest_import_public.proto\x12\x18protobuf_unittest_import\" \n\x13PublicImportMessage\x12\t\n\x01\x65\x18\x01 \x01(\x05\x42\x1a\n\x18\x63om.google.protobuf.test')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_PUBLICIMPORTMESSAGE = _descriptor.Descriptor(
  name='PublicImportMessage',
  full_name='protobuf_unittest_import.PublicImportMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='e', full_name='protobuf_unittest_import.PublicImportMessage.e', index=0,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=74,
  serialized_end=106,
)

DESCRIPTOR.message_types_by_name['PublicImportMessage'] = _PUBLICIMPORTMESSAGE

PublicImportMessage = _reflection.GeneratedProtocolMessageType('PublicImportMessage', (_message.Message,), dict(
  DESCRIPTOR = _PUBLICIMPORTMESSAGE,
  __module__ = 'google.protobuf.unittest_import_public_pb2'
  # @@protoc_insertion_point(class_scope:protobuf_unittest_import.PublicImportMessage)
  ))
_sym_db.RegisterMessage(PublicImportMessage)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\030com.google.protobuf.test'))
# @@protoc_insertion_point(module_scope)