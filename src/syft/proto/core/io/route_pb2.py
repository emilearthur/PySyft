# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/core/io/route.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from syft.proto.core.io import location_pb2 as proto_dot_core_dot_io_dot_location__pb2
from syft.proto.core.io import (
    connection_pb2 as proto_dot_core_dot_io_dot_connection__pb2,
)


DESCRIPTOR = _descriptor.FileDescriptor(
    name="proto/core/io/route.proto",
    package="syft.core.io",
    syntax="proto3",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n\x19proto/core/io/route.proto\x12\x0csyft.core.io\x1a\x1cproto/core/io/location.proto\x1a\x1eproto/core/io/connection.proto"{\n\tSoloRoute\x12\x33\n\x0b\x64\x65stination\x18\x01 \x01(\x0b\x32\x1e.syft.core.io.SpecificLocation\x12\x39\n\nconnection\x18\x02 \x01(\x0b\x32%.syft.core.io.VirtualClientConnectionb\x06proto3',
    dependencies=[
        proto_dot_core_dot_io_dot_location__pb2.DESCRIPTOR,
        proto_dot_core_dot_io_dot_connection__pb2.DESCRIPTOR,
    ],
)


_SOLOROUTE = _descriptor.Descriptor(
    name="SoloRoute",
    full_name="syft.core.io.SoloRoute",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="destination",
            full_name="syft.core.io.SoloRoute.destination",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="connection",
            full_name="syft.core.io.SoloRoute.connection",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=105,
    serialized_end=228,
)

_SOLOROUTE.fields_by_name[
    "destination"
].message_type = proto_dot_core_dot_io_dot_location__pb2._SPECIFICLOCATION
_SOLOROUTE.fields_by_name[
    "connection"
].message_type = proto_dot_core_dot_io_dot_connection__pb2._VIRTUALCLIENTCONNECTION
DESCRIPTOR.message_types_by_name["SoloRoute"] = _SOLOROUTE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SoloRoute = _reflection.GeneratedProtocolMessageType(
    "SoloRoute",
    (_message.Message,),
    {
        "DESCRIPTOR": _SOLOROUTE,
        "__module__": "proto.core.io.route_pb2"
        # @@protoc_insertion_point(class_scope:syft.core.io.SoloRoute)
    },
)
_sym_db.RegisterMessage(SoloRoute)


# @@protoc_insertion_point(module_scope)