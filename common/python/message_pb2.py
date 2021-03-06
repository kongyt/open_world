# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: message.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='message.proto',
  package='civilization',
  syntax='proto2',
  serialized_pb=_b('\n\rmessage.proto\x12\x0c\x63ivilization\"\x95\x01\n\x07Request\x12.\n\x0bregisterReq\x18\x01 \x01(\x0b\x32\x19.civilization.RegisterReq\x12(\n\x08loginReq\x18\x02 \x01(\x0b\x32\x16.civilization.LoginReq\x12\x30\n\x0creconnectReq\x18\x03 \x01(\x0b\x32\x1a.civilization.ReconnectReq\"\xd3\x01\n\x08Response\x12\x0e\n\x06result\x18\x01 \x02(\x08\x12\x14\n\x0clastResponse\x18\x02 \x02(\x08\x12\x15\n\rerrorDescribe\x18\x03 \x01(\t\x12.\n\x0bregisterRes\x18\x04 \x01(\x0b\x32\x19.civilization.RegisterRes\x12(\n\x08loginRes\x18\x05 \x01(\x0b\x32\x16.civilization.LoginRes\x12\x30\n\x0creconnectRes\x18\x06 \x01(\x0b\x32\x1a.civilization.ReconnectRes\"\r\n\x0bRegisterReq\")\n\x0bRegisterRes\x12\x0c\n\x04uuid\x18\x01 \x02(\t\x12\x0c\n\x04name\x18\x02 \x02(\t\"\x18\n\x08LoginReq\x12\x0c\n\x04uuid\x18\x01 \x02(\t\"\n\n\x08LoginRes\"\x1c\n\x0cReconnectReq\x12\x0c\n\x04uuid\x18\x01 \x02(\t\"\x0e\n\x0cReconnectRes*\x87\x01\n\x03Msg\x12\x0c\n\x08None_Msg\x10\x00\x12\x12\n\x0cRegister_Req\x10\x81\x80\x04\x12\x12\n\x0cRegister_Res\x10\x82\x80\x04\x12\x0f\n\tLogin_Req\x10\x83\x80\x04\x12\x0f\n\tLogin_Res\x10\x84\x80\x04\x12\x13\n\rReconnect_Req\x10\x85\x80\x04\x12\x13\n\rReconnect_Res\x10\x86\x80\x04\x42\"\n com.kongyt.civilization.messages')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_MSG = _descriptor.EnumDescriptor(
  name='Msg',
  full_name='civilization.Msg',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='None_Msg', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Register_Req', index=1, number=65537,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Register_Res', index=2, number=65538,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Login_Req', index=3, number=65539,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Login_Res', index=4, number=65540,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Reconnect_Req', index=5, number=65541,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Reconnect_Res', index=6, number=65542,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=540,
  serialized_end=675,
)
_sym_db.RegisterEnumDescriptor(_MSG)

Msg = enum_type_wrapper.EnumTypeWrapper(_MSG)
None_Msg = 0
Register_Req = 65537
Register_Res = 65538
Login_Req = 65539
Login_Res = 65540
Reconnect_Req = 65541
Reconnect_Res = 65542



_REQUEST = _descriptor.Descriptor(
  name='Request',
  full_name='civilization.Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='registerReq', full_name='civilization.Request.registerReq', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='loginReq', full_name='civilization.Request.loginReq', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='reconnectReq', full_name='civilization.Request.reconnectReq', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=32,
  serialized_end=181,
)


_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='civilization.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='civilization.Response.result', index=0,
      number=1, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lastResponse', full_name='civilization.Response.lastResponse', index=1,
      number=2, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='errorDescribe', full_name='civilization.Response.errorDescribe', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='registerRes', full_name='civilization.Response.registerRes', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='loginRes', full_name='civilization.Response.loginRes', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='reconnectRes', full_name='civilization.Response.reconnectRes', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=184,
  serialized_end=395,
)


_REGISTERREQ = _descriptor.Descriptor(
  name='RegisterReq',
  full_name='civilization.RegisterReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=397,
  serialized_end=410,
)


_REGISTERRES = _descriptor.Descriptor(
  name='RegisterRes',
  full_name='civilization.RegisterRes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uuid', full_name='civilization.RegisterRes.uuid', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='civilization.RegisterRes.name', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=412,
  serialized_end=453,
)


_LOGINREQ = _descriptor.Descriptor(
  name='LoginReq',
  full_name='civilization.LoginReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uuid', full_name='civilization.LoginReq.uuid', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=455,
  serialized_end=479,
)


_LOGINRES = _descriptor.Descriptor(
  name='LoginRes',
  full_name='civilization.LoginRes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=481,
  serialized_end=491,
)


_RECONNECTREQ = _descriptor.Descriptor(
  name='ReconnectReq',
  full_name='civilization.ReconnectReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uuid', full_name='civilization.ReconnectReq.uuid', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=493,
  serialized_end=521,
)


_RECONNECTRES = _descriptor.Descriptor(
  name='ReconnectRes',
  full_name='civilization.ReconnectRes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=523,
  serialized_end=537,
)

_REQUEST.fields_by_name['registerReq'].message_type = _REGISTERREQ
_REQUEST.fields_by_name['loginReq'].message_type = _LOGINREQ
_REQUEST.fields_by_name['reconnectReq'].message_type = _RECONNECTREQ
_RESPONSE.fields_by_name['registerRes'].message_type = _REGISTERRES
_RESPONSE.fields_by_name['loginRes'].message_type = _LOGINRES
_RESPONSE.fields_by_name['reconnectRes'].message_type = _RECONNECTRES
DESCRIPTOR.message_types_by_name['Request'] = _REQUEST
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE
DESCRIPTOR.message_types_by_name['RegisterReq'] = _REGISTERREQ
DESCRIPTOR.message_types_by_name['RegisterRes'] = _REGISTERRES
DESCRIPTOR.message_types_by_name['LoginReq'] = _LOGINREQ
DESCRIPTOR.message_types_by_name['LoginRes'] = _LOGINRES
DESCRIPTOR.message_types_by_name['ReconnectReq'] = _RECONNECTREQ
DESCRIPTOR.message_types_by_name['ReconnectRes'] = _RECONNECTRES
DESCRIPTOR.enum_types_by_name['Msg'] = _MSG

Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), dict(
  DESCRIPTOR = _REQUEST,
  __module__ = 'message_pb2'
  # @@protoc_insertion_point(class_scope:civilization.Request)
  ))
_sym_db.RegisterMessage(Request)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), dict(
  DESCRIPTOR = _RESPONSE,
  __module__ = 'message_pb2'
  # @@protoc_insertion_point(class_scope:civilization.Response)
  ))
_sym_db.RegisterMessage(Response)

RegisterReq = _reflection.GeneratedProtocolMessageType('RegisterReq', (_message.Message,), dict(
  DESCRIPTOR = _REGISTERREQ,
  __module__ = 'message_pb2'
  # @@protoc_insertion_point(class_scope:civilization.RegisterReq)
  ))
_sym_db.RegisterMessage(RegisterReq)

RegisterRes = _reflection.GeneratedProtocolMessageType('RegisterRes', (_message.Message,), dict(
  DESCRIPTOR = _REGISTERRES,
  __module__ = 'message_pb2'
  # @@protoc_insertion_point(class_scope:civilization.RegisterRes)
  ))
_sym_db.RegisterMessage(RegisterRes)

LoginReq = _reflection.GeneratedProtocolMessageType('LoginReq', (_message.Message,), dict(
  DESCRIPTOR = _LOGINREQ,
  __module__ = 'message_pb2'
  # @@protoc_insertion_point(class_scope:civilization.LoginReq)
  ))
_sym_db.RegisterMessage(LoginReq)

LoginRes = _reflection.GeneratedProtocolMessageType('LoginRes', (_message.Message,), dict(
  DESCRIPTOR = _LOGINRES,
  __module__ = 'message_pb2'
  # @@protoc_insertion_point(class_scope:civilization.LoginRes)
  ))
_sym_db.RegisterMessage(LoginRes)

ReconnectReq = _reflection.GeneratedProtocolMessageType('ReconnectReq', (_message.Message,), dict(
  DESCRIPTOR = _RECONNECTREQ,
  __module__ = 'message_pb2'
  # @@protoc_insertion_point(class_scope:civilization.ReconnectReq)
  ))
_sym_db.RegisterMessage(ReconnectReq)

ReconnectRes = _reflection.GeneratedProtocolMessageType('ReconnectRes', (_message.Message,), dict(
  DESCRIPTOR = _RECONNECTRES,
  __module__ = 'message_pb2'
  # @@protoc_insertion_point(class_scope:civilization.ReconnectRes)
  ))
_sym_db.RegisterMessage(ReconnectRes)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n com.kongyt.civilization.messages'))
# @@protoc_insertion_point(module_scope)
