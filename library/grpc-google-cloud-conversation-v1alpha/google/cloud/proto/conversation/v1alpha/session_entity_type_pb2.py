# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/proto/conversation/v1alpha/session_entity_type.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.cloud.proto.conversation.v1alpha import entity_type_pb2 as google_dot_cloud_dot_proto_dot_conversation_dot_v1alpha_dot_entity__type__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/cloud/proto/conversation/v1alpha/session_entity_type.proto',
  package='google.cloud.conversation.v1alpha',
  syntax='proto3',
  serialized_pb=_b('\nAgoogle/cloud/proto/conversation/v1alpha/session_entity_type.proto\x12!google.cloud.conversation.v1alpha\x1a\x1cgoogle/api/annotations.proto\x1a\x39google/cloud/proto/conversation/v1alpha/entity_type.proto\"\xd5\x02\n\x11SessionEntityType\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x65\n\x14\x65ntity_override_mode\x18\x02 \x01(\x0e\x32G.google.cloud.conversation.v1alpha.SessionEntityType.EntityOverrideMode\x12\x46\n\x08\x65ntities\x18\x03 \x03(\x0b\x32\x34.google.cloud.conversation.v1alpha.EntityType.Entity\"\x82\x01\n\x12\x45ntityOverrideMode\x12$\n ENTITY_OVERRIDE_MODE_UNSPECIFIED\x10\x00\x12!\n\x1d\x45NTITY_OVERRIDE_MODE_OVERRIDE\x10\x01\x12#\n\x1f\x45NTITY_OVERRIDE_MODE_SUPPLEMENT\x10\x02\"+\n\x1bGetSessionEntityTypeRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"\x83\x01\n\x1e\x43reateSessionEntityTypeRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12Q\n\x13session_entity_type\x18\x02 \x01(\x0b\x32\x34.google.cloud.conversation.v1alpha.SessionEntityType\"s\n\x1eUpdateSessionEntityTypeRequest\x12Q\n\x13session_entity_type\x18\x01 \x01(\x0b\x32\x34.google.cloud.conversation.v1alpha.SessionEntityType\".\n\x1e\x44\x65leteSessionEntityTypeRequest\x12\x0c\n\x04name\x18\x01 \x01(\tB\x90\x01\n%com.google.cloud.conversation.v1alphaB\x13UserUserEntityProtoP\x01ZMgoogle.golang.org/genproto/googleapis/cloud/conversation/v1alpha;conversation\xf8\x01\x01\x62\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_cloud_dot_proto_dot_conversation_dot_v1alpha_dot_entity__type__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_SESSIONENTITYTYPE_ENTITYOVERRIDEMODE = _descriptor.EnumDescriptor(
  name='EntityOverrideMode',
  full_name='google.cloud.conversation.v1alpha.SessionEntityType.EntityOverrideMode',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ENTITY_OVERRIDE_MODE_UNSPECIFIED', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ENTITY_OVERRIDE_MODE_OVERRIDE', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ENTITY_OVERRIDE_MODE_SUPPLEMENT', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=405,
  serialized_end=535,
)
_sym_db.RegisterEnumDescriptor(_SESSIONENTITYTYPE_ENTITYOVERRIDEMODE)


_SESSIONENTITYTYPE = _descriptor.Descriptor(
  name='SessionEntityType',
  full_name='google.cloud.conversation.v1alpha.SessionEntityType',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.cloud.conversation.v1alpha.SessionEntityType.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='entity_override_mode', full_name='google.cloud.conversation.v1alpha.SessionEntityType.entity_override_mode', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='entities', full_name='google.cloud.conversation.v1alpha.SessionEntityType.entities', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _SESSIONENTITYTYPE_ENTITYOVERRIDEMODE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=194,
  serialized_end=535,
)


_GETSESSIONENTITYTYPEREQUEST = _descriptor.Descriptor(
  name='GetSessionEntityTypeRequest',
  full_name='google.cloud.conversation.v1alpha.GetSessionEntityTypeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.cloud.conversation.v1alpha.GetSessionEntityTypeRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=537,
  serialized_end=580,
)


_CREATESESSIONENTITYTYPEREQUEST = _descriptor.Descriptor(
  name='CreateSessionEntityTypeRequest',
  full_name='google.cloud.conversation.v1alpha.CreateSessionEntityTypeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='parent', full_name='google.cloud.conversation.v1alpha.CreateSessionEntityTypeRequest.parent', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='session_entity_type', full_name='google.cloud.conversation.v1alpha.CreateSessionEntityTypeRequest.session_entity_type', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=583,
  serialized_end=714,
)


_UPDATESESSIONENTITYTYPEREQUEST = _descriptor.Descriptor(
  name='UpdateSessionEntityTypeRequest',
  full_name='google.cloud.conversation.v1alpha.UpdateSessionEntityTypeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='session_entity_type', full_name='google.cloud.conversation.v1alpha.UpdateSessionEntityTypeRequest.session_entity_type', index=0,
      number=1, type=11, cpp_type=10, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=716,
  serialized_end=831,
)


_DELETESESSIONENTITYTYPEREQUEST = _descriptor.Descriptor(
  name='DeleteSessionEntityTypeRequest',
  full_name='google.cloud.conversation.v1alpha.DeleteSessionEntityTypeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.cloud.conversation.v1alpha.DeleteSessionEntityTypeRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=833,
  serialized_end=879,
)

_SESSIONENTITYTYPE.fields_by_name['entity_override_mode'].enum_type = _SESSIONENTITYTYPE_ENTITYOVERRIDEMODE
_SESSIONENTITYTYPE.fields_by_name['entities'].message_type = google_dot_cloud_dot_proto_dot_conversation_dot_v1alpha_dot_entity__type__pb2._ENTITYTYPE_ENTITY
_SESSIONENTITYTYPE_ENTITYOVERRIDEMODE.containing_type = _SESSIONENTITYTYPE
_CREATESESSIONENTITYTYPEREQUEST.fields_by_name['session_entity_type'].message_type = _SESSIONENTITYTYPE
_UPDATESESSIONENTITYTYPEREQUEST.fields_by_name['session_entity_type'].message_type = _SESSIONENTITYTYPE
DESCRIPTOR.message_types_by_name['SessionEntityType'] = _SESSIONENTITYTYPE
DESCRIPTOR.message_types_by_name['GetSessionEntityTypeRequest'] = _GETSESSIONENTITYTYPEREQUEST
DESCRIPTOR.message_types_by_name['CreateSessionEntityTypeRequest'] = _CREATESESSIONENTITYTYPEREQUEST
DESCRIPTOR.message_types_by_name['UpdateSessionEntityTypeRequest'] = _UPDATESESSIONENTITYTYPEREQUEST
DESCRIPTOR.message_types_by_name['DeleteSessionEntityTypeRequest'] = _DELETESESSIONENTITYTYPEREQUEST

SessionEntityType = _reflection.GeneratedProtocolMessageType('SessionEntityType', (_message.Message,), dict(
  DESCRIPTOR = _SESSIONENTITYTYPE,
  __module__ = 'google.cloud.proto.conversation.v1alpha.session_entity_type_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.conversation.v1alpha.SessionEntityType)
  ))
_sym_db.RegisterMessage(SessionEntityType)

GetSessionEntityTypeRequest = _reflection.GeneratedProtocolMessageType('GetSessionEntityTypeRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETSESSIONENTITYTYPEREQUEST,
  __module__ = 'google.cloud.proto.conversation.v1alpha.session_entity_type_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.conversation.v1alpha.GetSessionEntityTypeRequest)
  ))
_sym_db.RegisterMessage(GetSessionEntityTypeRequest)

CreateSessionEntityTypeRequest = _reflection.GeneratedProtocolMessageType('CreateSessionEntityTypeRequest', (_message.Message,), dict(
  DESCRIPTOR = _CREATESESSIONENTITYTYPEREQUEST,
  __module__ = 'google.cloud.proto.conversation.v1alpha.session_entity_type_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.conversation.v1alpha.CreateSessionEntityTypeRequest)
  ))
_sym_db.RegisterMessage(CreateSessionEntityTypeRequest)

UpdateSessionEntityTypeRequest = _reflection.GeneratedProtocolMessageType('UpdateSessionEntityTypeRequest', (_message.Message,), dict(
  DESCRIPTOR = _UPDATESESSIONENTITYTYPEREQUEST,
  __module__ = 'google.cloud.proto.conversation.v1alpha.session_entity_type_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.conversation.v1alpha.UpdateSessionEntityTypeRequest)
  ))
_sym_db.RegisterMessage(UpdateSessionEntityTypeRequest)

DeleteSessionEntityTypeRequest = _reflection.GeneratedProtocolMessageType('DeleteSessionEntityTypeRequest', (_message.Message,), dict(
  DESCRIPTOR = _DELETESESSIONENTITYTYPEREQUEST,
  __module__ = 'google.cloud.proto.conversation.v1alpha.session_entity_type_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.conversation.v1alpha.DeleteSessionEntityTypeRequest)
  ))
_sym_db.RegisterMessage(DeleteSessionEntityTypeRequest)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n%com.google.cloud.conversation.v1alphaB\023UserUserEntityProtoP\001ZMgoogle.golang.org/genproto/googleapis/cloud/conversation/v1alpha;conversation\370\001\001'))
try:
  # THESE ELEMENTS WILL BE DEPRECATED.
  # Please use the generated *_pb2_grpc.py files instead.
  import grpc
  from grpc.beta import implementations as beta_implementations
  from grpc.beta import interfaces as beta_interfaces
  from grpc.framework.common import cardinality
  from grpc.framework.interfaces.face import utilities as face_utilities
except ImportError:
  pass
# @@protoc_insertion_point(module_scope)