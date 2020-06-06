# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: getreplied.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='getreplied.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x10getreplied.proto\"X\n\treplyInfo\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0f\n\x07replier\x18\x02 \x01(\t\x12\x0f\n\x07repliee\x18\x03 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x04 \x01(\t\x12\x0c\n\x04like\x18\x05 \x01(\x05\"<\n\tReplyPage\x12\x1b\n\x07replies\x18\x01 \x03(\x0b\x32\n.replyInfo\x12\x12\n\ntotalcount\x18\x02 \x01(\x05\";\n\x05input\x12\r\n\x05token\x18\x01 \x01(\t\x12\x0f\n\x07news_id\x18\x02 \x01(\t\x12\x12\n\ncomment_id\x18\x03 \x01(\t\"$\n\x06output\x12\x1a\n\x06result\x18\x01 \x01(\x0b\x32\n.ReplyPage2-\n\ngetreplied\x12\x1f\n\ngetreplied\x12\x06.input\x1a\x07.output\"\x00\x62\x06proto3'
)




_REPLYINFO = _descriptor.Descriptor(
  name='replyInfo',
  full_name='replyInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='replyInfo.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='replier', full_name='replyInfo.replier', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='repliee', full_name='replyInfo.repliee', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='content', full_name='replyInfo.content', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='like', full_name='replyInfo.like', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=20,
  serialized_end=108,
)


_REPLYPAGE = _descriptor.Descriptor(
  name='ReplyPage',
  full_name='ReplyPage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='replies', full_name='ReplyPage.replies', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='totalcount', full_name='ReplyPage.totalcount', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=110,
  serialized_end=170,
)


_INPUT = _descriptor.Descriptor(
  name='input',
  full_name='input',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='token', full_name='input.token', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='news_id', full_name='input.news_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='comment_id', full_name='input.comment_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=172,
  serialized_end=231,
)


_OUTPUT = _descriptor.Descriptor(
  name='output',
  full_name='output',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='output.result', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=233,
  serialized_end=269,
)

_REPLYPAGE.fields_by_name['replies'].message_type = _REPLYINFO
_OUTPUT.fields_by_name['result'].message_type = _REPLYPAGE
DESCRIPTOR.message_types_by_name['replyInfo'] = _REPLYINFO
DESCRIPTOR.message_types_by_name['ReplyPage'] = _REPLYPAGE
DESCRIPTOR.message_types_by_name['input'] = _INPUT
DESCRIPTOR.message_types_by_name['output'] = _OUTPUT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

replyInfo = _reflection.GeneratedProtocolMessageType('replyInfo', (_message.Message,), {
  'DESCRIPTOR' : _REPLYINFO,
  '__module__' : 'getreplied_pb2'
  # @@protoc_insertion_point(class_scope:replyInfo)
  })
_sym_db.RegisterMessage(replyInfo)

ReplyPage = _reflection.GeneratedProtocolMessageType('ReplyPage', (_message.Message,), {
  'DESCRIPTOR' : _REPLYPAGE,
  '__module__' : 'getreplied_pb2'
  # @@protoc_insertion_point(class_scope:ReplyPage)
  })
_sym_db.RegisterMessage(ReplyPage)

input = _reflection.GeneratedProtocolMessageType('input', (_message.Message,), {
  'DESCRIPTOR' : _INPUT,
  '__module__' : 'getreplied_pb2'
  # @@protoc_insertion_point(class_scope:input)
  })
_sym_db.RegisterMessage(input)

output = _reflection.GeneratedProtocolMessageType('output', (_message.Message,), {
  'DESCRIPTOR' : _OUTPUT,
  '__module__' : 'getreplied_pb2'
  # @@protoc_insertion_point(class_scope:output)
  })
_sym_db.RegisterMessage(output)



_GETREPLIED = _descriptor.ServiceDescriptor(
  name='getreplied',
  full_name='getreplied',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=271,
  serialized_end=316,
  methods=[
  _descriptor.MethodDescriptor(
    name='getreplied',
    full_name='getreplied.getreplied',
    index=0,
    containing_service=None,
    input_type=_INPUT,
    output_type=_OUTPUT,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_GETREPLIED)

DESCRIPTOR.services_by_name['getreplied'] = _GETREPLIED

# @@protoc_insertion_point(module_scope)
