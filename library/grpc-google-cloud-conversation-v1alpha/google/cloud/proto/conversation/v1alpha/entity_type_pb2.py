# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/proto/conversation/v1alpha/entity_type.proto

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


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/cloud/proto/conversation/v1alpha/entity_type.proto',
  package='google.cloud.conversation.v1alpha',
  syntax='proto3',
  serialized_pb=_b('\n9google/cloud/proto/conversation/v1alpha/entity_type.proto\x12!google.cloud.conversation.v1alpha\x1a\x1cgoogle/api/annotations.proto\"\xd9\x03\n\nEntityType\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x14\n\x0c\x64isplay_name\x18\x02 \x01(\t\x12@\n\x04kind\x18\x03 \x01(\x0e\x32\x32.google.cloud.conversation.v1alpha.EntityType.Kind\x12\\\n\x13\x61uto_expansion_mode\x18\x04 \x01(\x0e\x32?.google.cloud.conversation.v1alpha.EntityType.AutoExpansionMode\x12\x46\n\x08\x65ntities\x18\x06 \x03(\x0b\x32\x34.google.cloud.conversation.v1alpha.EntityType.Entity\x1a)\n\x06\x45ntity\x12\r\n\x05value\x18\x01 \x01(\t\x12\x10\n\x08synonyms\x18\x02 \x03(\t\"9\n\x04Kind\x12\x14\n\x10KIND_UNSPECIFIED\x10\x00\x12\x0c\n\x08KIND_MAP\x10\x01\x12\r\n\tKIND_LIST\x10\x02\"Y\n\x11\x41utoExpansionMode\x12#\n\x1f\x41UTO_EXPANSION_MODE_UNSPECIFIED\x10\x00\x12\x1f\n\x1b\x41UTO_EXPANSION_MODE_DEFAULT\x10\x01\"?\n\x16ListEntityTypesRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\x15\n\rlanguage_code\x18\x02 \x01(\t\"^\n\x17ListEntityTypesResponse\x12\x43\n\x0c\x65ntity_types\x18\x01 \x03(\x0b\x32-.google.cloud.conversation.v1alpha.EntityType\";\n\x14GetEntityTypeRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x15\n\rlanguage_code\x18\x02 \x01(\t\"\x84\x01\n\x17\x43reateEntityTypeRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\x42\n\x0b\x65ntity_type\x18\x02 \x01(\x0b\x32-.google.cloud.conversation.v1alpha.EntityType\x12\x15\n\rlanguage_code\x18\x03 \x01(\t\"t\n\x17UpdateEntityTypeRequest\x12\x42\n\x0b\x65ntity_type\x18\x01 \x01(\x0b\x32-.google.cloud.conversation.v1alpha.EntityType\x12\x15\n\rlanguage_code\x18\x02 \x01(\t\"\'\n\x17\x44\x65leteEntityTypeRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"\x8b\x01\n\x1d\x42\x61tchUpdateEntityTypesRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\x43\n\x0c\x65ntity_types\x18\x02 \x03(\x0b\x32-.google.cloud.conversation.v1alpha.EntityType\x12\x15\n\rlanguage_code\x18\x03 \x01(\t\"e\n\x1e\x42\x61tchUpdateEntityTypesResponse\x12\x43\n\x0c\x65ntity_types\x18\x01 \x03(\x0b\x32-.google.cloud.conversation.v1alpha.EntityType\"\x8b\x01\n\x1a\x42\x61tchCreateEntitiesRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\x46\n\x08\x65ntities\x18\x02 \x03(\x0b\x32\x34.google.cloud.conversation.v1alpha.EntityType.Entity\x12\x15\n\rlanguage_code\x18\x03 \x01(\t\"\x8b\x01\n\x1a\x42\x61tchUpdateEntitiesRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\x46\n\x08\x65ntities\x18\x02 \x03(\x0b\x32\x34.google.cloud.conversation.v1alpha.EntityType.Entity\x12\x15\n\rlanguage_code\x18\x03 \x01(\t\"t\n\x1a\x42\x61tchDeleteEntitiesRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\x46\n\x08\x65ntities\x18\x02 \x03(\x0b\x32\x34.google.cloud.conversation.v1alpha.EntityType.EntityB\x88\x01\n%com.google.cloud.conversation.v1alphaB\x0b\x45ntityProtoP\x01ZMgoogle.golang.org/genproto/googleapis/cloud/conversation/v1alpha;conversation\xf8\x01\x01\x62\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_ENTITYTYPE_KIND = _descriptor.EnumDescriptor(
  name='Kind',
  full_name='google.cloud.conversation.v1alpha.EntityType.Kind',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='KIND_UNSPECIFIED', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='KIND_MAP', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='KIND_LIST', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=452,
  serialized_end=509,
)
_sym_db.RegisterEnumDescriptor(_ENTITYTYPE_KIND)

_ENTITYTYPE_AUTOEXPANSIONMODE = _descriptor.EnumDescriptor(
  name='AutoExpansionMode',
  full_name='google.cloud.conversation.v1alpha.EntityType.AutoExpansionMode',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='AUTO_EXPANSION_MODE_UNSPECIFIED', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AUTO_EXPANSION_MODE_DEFAULT', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=511,
  serialized_end=600,
)
_sym_db.RegisterEnumDescriptor(_ENTITYTYPE_AUTOEXPANSIONMODE)


_ENTITYTYPE_ENTITY = _descriptor.Descriptor(
  name='Entity',
  full_name='google.cloud.conversation.v1alpha.EntityType.Entity',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='google.cloud.conversation.v1alpha.EntityType.Entity.value', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='synonyms', full_name='google.cloud.conversation.v1alpha.EntityType.Entity.synonyms', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=409,
  serialized_end=450,
)

_ENTITYTYPE = _descriptor.Descriptor(
  name='EntityType',
  full_name='google.cloud.conversation.v1alpha.EntityType',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.cloud.conversation.v1alpha.EntityType.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='display_name', full_name='google.cloud.conversation.v1alpha.EntityType.display_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='kind', full_name='google.cloud.conversation.v1alpha.EntityType.kind', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='auto_expansion_mode', full_name='google.cloud.conversation.v1alpha.EntityType.auto_expansion_mode', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='entities', full_name='google.cloud.conversation.v1alpha.EntityType.entities', index=4,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_ENTITYTYPE_ENTITY, ],
  enum_types=[
    _ENTITYTYPE_KIND,
    _ENTITYTYPE_AUTOEXPANSIONMODE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=127,
  serialized_end=600,
)


_LISTENTITYTYPESREQUEST = _descriptor.Descriptor(
  name='ListEntityTypesRequest',
  full_name='google.cloud.conversation.v1alpha.ListEntityTypesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='parent', full_name='google.cloud.conversation.v1alpha.ListEntityTypesRequest.parent', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='language_code', full_name='google.cloud.conversation.v1alpha.ListEntityTypesRequest.language_code', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=602,
  serialized_end=665,
)


_LISTENTITYTYPESRESPONSE = _descriptor.Descriptor(
  name='ListEntityTypesResponse',
  full_name='google.cloud.conversation.v1alpha.ListEntityTypesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='entity_types', full_name='google.cloud.conversation.v1alpha.ListEntityTypesResponse.entity_types', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=667,
  serialized_end=761,
)


_GETENTITYTYPEREQUEST = _descriptor.Descriptor(
  name='GetEntityTypeRequest',
  full_name='google.cloud.conversation.v1alpha.GetEntityTypeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.cloud.conversation.v1alpha.GetEntityTypeRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='language_code', full_name='google.cloud.conversation.v1alpha.GetEntityTypeRequest.language_code', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=763,
  serialized_end=822,
)


_CREATEENTITYTYPEREQUEST = _descriptor.Descriptor(
  name='CreateEntityTypeRequest',
  full_name='google.cloud.conversation.v1alpha.CreateEntityTypeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='parent', full_name='google.cloud.conversation.v1alpha.CreateEntityTypeRequest.parent', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='entity_type', full_name='google.cloud.conversation.v1alpha.CreateEntityTypeRequest.entity_type', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='language_code', full_name='google.cloud.conversation.v1alpha.CreateEntityTypeRequest.language_code', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=825,
  serialized_end=957,
)


_UPDATEENTITYTYPEREQUEST = _descriptor.Descriptor(
  name='UpdateEntityTypeRequest',
  full_name='google.cloud.conversation.v1alpha.UpdateEntityTypeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='entity_type', full_name='google.cloud.conversation.v1alpha.UpdateEntityTypeRequest.entity_type', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='language_code', full_name='google.cloud.conversation.v1alpha.UpdateEntityTypeRequest.language_code', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=959,
  serialized_end=1075,
)


_DELETEENTITYTYPEREQUEST = _descriptor.Descriptor(
  name='DeleteEntityTypeRequest',
  full_name='google.cloud.conversation.v1alpha.DeleteEntityTypeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.cloud.conversation.v1alpha.DeleteEntityTypeRequest.name', index=0,
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
  serialized_start=1077,
  serialized_end=1116,
)


_BATCHUPDATEENTITYTYPESREQUEST = _descriptor.Descriptor(
  name='BatchUpdateEntityTypesRequest',
  full_name='google.cloud.conversation.v1alpha.BatchUpdateEntityTypesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='parent', full_name='google.cloud.conversation.v1alpha.BatchUpdateEntityTypesRequest.parent', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='entity_types', full_name='google.cloud.conversation.v1alpha.BatchUpdateEntityTypesRequest.entity_types', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='language_code', full_name='google.cloud.conversation.v1alpha.BatchUpdateEntityTypesRequest.language_code', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=1119,
  serialized_end=1258,
)


_BATCHUPDATEENTITYTYPESRESPONSE = _descriptor.Descriptor(
  name='BatchUpdateEntityTypesResponse',
  full_name='google.cloud.conversation.v1alpha.BatchUpdateEntityTypesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='entity_types', full_name='google.cloud.conversation.v1alpha.BatchUpdateEntityTypesResponse.entity_types', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=1260,
  serialized_end=1361,
)


_BATCHCREATEENTITIESREQUEST = _descriptor.Descriptor(
  name='BatchCreateEntitiesRequest',
  full_name='google.cloud.conversation.v1alpha.BatchCreateEntitiesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='parent', full_name='google.cloud.conversation.v1alpha.BatchCreateEntitiesRequest.parent', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='entities', full_name='google.cloud.conversation.v1alpha.BatchCreateEntitiesRequest.entities', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='language_code', full_name='google.cloud.conversation.v1alpha.BatchCreateEntitiesRequest.language_code', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=1364,
  serialized_end=1503,
)


_BATCHUPDATEENTITIESREQUEST = _descriptor.Descriptor(
  name='BatchUpdateEntitiesRequest',
  full_name='google.cloud.conversation.v1alpha.BatchUpdateEntitiesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='parent', full_name='google.cloud.conversation.v1alpha.BatchUpdateEntitiesRequest.parent', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='entities', full_name='google.cloud.conversation.v1alpha.BatchUpdateEntitiesRequest.entities', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='language_code', full_name='google.cloud.conversation.v1alpha.BatchUpdateEntitiesRequest.language_code', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=1506,
  serialized_end=1645,
)


_BATCHDELETEENTITIESREQUEST = _descriptor.Descriptor(
  name='BatchDeleteEntitiesRequest',
  full_name='google.cloud.conversation.v1alpha.BatchDeleteEntitiesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='parent', full_name='google.cloud.conversation.v1alpha.BatchDeleteEntitiesRequest.parent', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='entities', full_name='google.cloud.conversation.v1alpha.BatchDeleteEntitiesRequest.entities', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=1647,
  serialized_end=1763,
)

_ENTITYTYPE_ENTITY.containing_type = _ENTITYTYPE
_ENTITYTYPE.fields_by_name['kind'].enum_type = _ENTITYTYPE_KIND
_ENTITYTYPE.fields_by_name['auto_expansion_mode'].enum_type = _ENTITYTYPE_AUTOEXPANSIONMODE
_ENTITYTYPE.fields_by_name['entities'].message_type = _ENTITYTYPE_ENTITY
_ENTITYTYPE_KIND.containing_type = _ENTITYTYPE
_ENTITYTYPE_AUTOEXPANSIONMODE.containing_type = _ENTITYTYPE
_LISTENTITYTYPESRESPONSE.fields_by_name['entity_types'].message_type = _ENTITYTYPE
_CREATEENTITYTYPEREQUEST.fields_by_name['entity_type'].message_type = _ENTITYTYPE
_UPDATEENTITYTYPEREQUEST.fields_by_name['entity_type'].message_type = _ENTITYTYPE
_BATCHUPDATEENTITYTYPESREQUEST.fields_by_name['entity_types'].message_type = _ENTITYTYPE
_BATCHUPDATEENTITYTYPESRESPONSE.fields_by_name['entity_types'].message_type = _ENTITYTYPE
_BATCHCREATEENTITIESREQUEST.fields_by_name['entities'].message_type = _ENTITYTYPE_ENTITY
_BATCHUPDATEENTITIESREQUEST.fields_by_name['entities'].message_type = _ENTITYTYPE_ENTITY
_BATCHDELETEENTITIESREQUEST.fields_by_name['entities'].message_type = _ENTITYTYPE_ENTITY
DESCRIPTOR.message_types_by_name['EntityType'] = _ENTITYTYPE
DESCRIPTOR.message_types_by_name['ListEntityTypesRequest'] = _LISTENTITYTYPESREQUEST
DESCRIPTOR.message_types_by_name['ListEntityTypesResponse'] = _LISTENTITYTYPESRESPONSE
DESCRIPTOR.message_types_by_name['GetEntityTypeRequest'] = _GETENTITYTYPEREQUEST
DESCRIPTOR.message_types_by_name['CreateEntityTypeRequest'] = _CREATEENTITYTYPEREQUEST
DESCRIPTOR.message_types_by_name['UpdateEntityTypeRequest'] = _UPDATEENTITYTYPEREQUEST
DESCRIPTOR.message_types_by_name['DeleteEntityTypeRequest'] = _DELETEENTITYTYPEREQUEST
DESCRIPTOR.message_types_by_name['BatchUpdateEntityTypesRequest'] = _BATCHUPDATEENTITYTYPESREQUEST
DESCRIPTOR.message_types_by_name['BatchUpdateEntityTypesResponse'] = _BATCHUPDATEENTITYTYPESRESPONSE
DESCRIPTOR.message_types_by_name['BatchCreateEntitiesRequest'] = _BATCHCREATEENTITIESREQUEST
DESCRIPTOR.message_types_by_name['BatchUpdateEntitiesRequest'] = _BATCHUPDATEENTITIESREQUEST
DESCRIPTOR.message_types_by_name['BatchDeleteEntitiesRequest'] = _BATCHDELETEENTITIESREQUEST

EntityType = _reflection.GeneratedProtocolMessageType('EntityType', (_message.Message,), dict(

  Entity = _reflection.GeneratedProtocolMessageType('Entity', (_message.Message,), dict(
    DESCRIPTOR = _ENTITYTYPE_ENTITY,
    __module__ = 'google.cloud.proto.conversation.v1alpha.entity_type_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.conversation.v1alpha.EntityType.Entity)
    ))
  ,
  DESCRIPTOR = _ENTITYTYPE,
  __module__ = 'google.cloud.proto.conversation.v1alpha.entity_type_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.conversation.v1alpha.EntityType)
  ))
_sym_db.RegisterMessage(EntityType)
_sym_db.RegisterMessage(EntityType.Entity)

ListEntityTypesRequest = _reflection.GeneratedProtocolMessageType('ListEntityTypesRequest', (_message.Message,), dict(
  DESCRIPTOR = _LISTENTITYTYPESREQUEST,
  __module__ = 'google.cloud.proto.conversation.v1alpha.entity_type_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.conversation.v1alpha.ListEntityTypesRequest)
  ))
_sym_db.RegisterMessage(ListEntityTypesRequest)

ListEntityTypesResponse = _reflection.GeneratedProtocolMessageType('ListEntityTypesResponse', (_message.Message,), dict(
  DESCRIPTOR = _LISTENTITYTYPESRESPONSE,
  __module__ = 'google.cloud.proto.conversation.v1alpha.entity_type_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.conversation.v1alpha.ListEntityTypesResponse)
  ))
_sym_db.RegisterMessage(ListEntityTypesResponse)

GetEntityTypeRequest = _reflection.GeneratedProtocolMessageType('GetEntityTypeRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETENTITYTYPEREQUEST,
  __module__ = 'google.cloud.proto.conversation.v1alpha.entity_type_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.conversation.v1alpha.GetEntityTypeRequest)
  ))
_sym_db.RegisterMessage(GetEntityTypeRequest)

CreateEntityTypeRequest = _reflection.GeneratedProtocolMessageType('CreateEntityTypeRequest', (_message.Message,), dict(
  DESCRIPTOR = _CREATEENTITYTYPEREQUEST,
  __module__ = 'google.cloud.proto.conversation.v1alpha.entity_type_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.conversation.v1alpha.CreateEntityTypeRequest)
  ))
_sym_db.RegisterMessage(CreateEntityTypeRequest)

UpdateEntityTypeRequest = _reflection.GeneratedProtocolMessageType('UpdateEntityTypeRequest', (_message.Message,), dict(
  DESCRIPTOR = _UPDATEENTITYTYPEREQUEST,
  __module__ = 'google.cloud.proto.conversation.v1alpha.entity_type_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.conversation.v1alpha.UpdateEntityTypeRequest)
  ))
_sym_db.RegisterMessage(UpdateEntityTypeRequest)

DeleteEntityTypeRequest = _reflection.GeneratedProtocolMessageType('DeleteEntityTypeRequest', (_message.Message,), dict(
  DESCRIPTOR = _DELETEENTITYTYPEREQUEST,
  __module__ = 'google.cloud.proto.conversation.v1alpha.entity_type_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.conversation.v1alpha.DeleteEntityTypeRequest)
  ))
_sym_db.RegisterMessage(DeleteEntityTypeRequest)

BatchUpdateEntityTypesRequest = _reflection.GeneratedProtocolMessageType('BatchUpdateEntityTypesRequest', (_message.Message,), dict(
  DESCRIPTOR = _BATCHUPDATEENTITYTYPESREQUEST,
  __module__ = 'google.cloud.proto.conversation.v1alpha.entity_type_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.conversation.v1alpha.BatchUpdateEntityTypesRequest)
  ))
_sym_db.RegisterMessage(BatchUpdateEntityTypesRequest)

BatchUpdateEntityTypesResponse = _reflection.GeneratedProtocolMessageType('BatchUpdateEntityTypesResponse', (_message.Message,), dict(
  DESCRIPTOR = _BATCHUPDATEENTITYTYPESRESPONSE,
  __module__ = 'google.cloud.proto.conversation.v1alpha.entity_type_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.conversation.v1alpha.BatchUpdateEntityTypesResponse)
  ))
_sym_db.RegisterMessage(BatchUpdateEntityTypesResponse)

BatchCreateEntitiesRequest = _reflection.GeneratedProtocolMessageType('BatchCreateEntitiesRequest', (_message.Message,), dict(
  DESCRIPTOR = _BATCHCREATEENTITIESREQUEST,
  __module__ = 'google.cloud.proto.conversation.v1alpha.entity_type_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.conversation.v1alpha.BatchCreateEntitiesRequest)
  ))
_sym_db.RegisterMessage(BatchCreateEntitiesRequest)

BatchUpdateEntitiesRequest = _reflection.GeneratedProtocolMessageType('BatchUpdateEntitiesRequest', (_message.Message,), dict(
  DESCRIPTOR = _BATCHUPDATEENTITIESREQUEST,
  __module__ = 'google.cloud.proto.conversation.v1alpha.entity_type_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.conversation.v1alpha.BatchUpdateEntitiesRequest)
  ))
_sym_db.RegisterMessage(BatchUpdateEntitiesRequest)

BatchDeleteEntitiesRequest = _reflection.GeneratedProtocolMessageType('BatchDeleteEntitiesRequest', (_message.Message,), dict(
  DESCRIPTOR = _BATCHDELETEENTITIESREQUEST,
  __module__ = 'google.cloud.proto.conversation.v1alpha.entity_type_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.conversation.v1alpha.BatchDeleteEntitiesRequest)
  ))
_sym_db.RegisterMessage(BatchDeleteEntitiesRequest)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n%com.google.cloud.conversation.v1alphaB\013EntityProtoP\001ZMgoogle.golang.org/genproto/googleapis/cloud/conversation/v1alpha;conversation\370\001\001'))
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
