# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: click_news.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='click_news.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x10\x63lick_news.proto\"\'\n\x05input\x12\r\n\x05token\x18\x01 \x01(\t\x12\x0f\n\x07news_id\x18\x02 \x01(\t\"\x18\n\x06output\x12\x0e\n\x06result\x18\x01 \x01(\x05\x32-\n\nclick_news\x12\x1f\n\nclick_news\x12\x06.input\x1a\x07.output\"\x00\x62\x06proto3'
)




_INPUT = _descriptor.Descriptor(
  name='input',
  full_name='input',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='token', full_name='input.token', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='news_id', full_name='input.news_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_end=59,
)


_OUTPUT = _descriptor.Descriptor(
  name='output',
  full_name='output',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='output.result', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=61,
  serialized_end=85,
)

DESCRIPTOR.message_types_by_name['input'] = _INPUT
DESCRIPTOR.message_types_by_name['output'] = _OUTPUT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

input = _reflection.GeneratedProtocolMessageType('input', (_message.Message,), {
  'DESCRIPTOR' : _INPUT,
  '__module__' : 'click_news_pb2'
  # @@protoc_insertion_point(class_scope:input)
  })
_sym_db.RegisterMessage(input)

output = _reflection.GeneratedProtocolMessageType('output', (_message.Message,), {
  'DESCRIPTOR' : _OUTPUT,
  '__module__' : 'click_news_pb2'
  # @@protoc_insertion_point(class_scope:output)
  })
_sym_db.RegisterMessage(output)



_CLICK_NEWS = _descriptor.ServiceDescriptor(
  name='click_news',
  full_name='click_news',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=87,
  serialized_end=132,
  methods=[
  _descriptor.MethodDescriptor(
    name='click_news',
    full_name='click_news.click_news',
    index=0,
    containing_service=None,
    input_type=_INPUT,
    output_type=_OUTPUT,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_CLICK_NEWS)

DESCRIPTOR.services_by_name['click_news'] = _CLICK_NEWS

# @@protoc_insertion_point(module_scope)
