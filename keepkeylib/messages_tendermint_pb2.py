# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: messages-tendermint.proto
# Protobuf Python Version: 5.27.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    3,
    '',
    'messages-tendermint.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import types_pb2 as types__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19messages-tendermint.proto\x1a\x0btypes.proto\"|\n\x14TendermintGetAddress\x12\x11\n\taddress_n\x18\x01 \x03(\r\x12\x14\n\x0cshow_display\x18\x02 \x01(\x08\x12\x0f\n\x07testnet\x18\x03 \x01(\x08\x12\x16\n\x0e\x61\x64\x64ress_prefix\x18\x04 \x01(\t\x12\x12\n\nchain_name\x18\x05 \x01(\t\"$\n\x11TendermintAddress\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\"\x8e\x02\n\x10TendermintSignTx\x12\x11\n\taddress_n\x18\x01 \x03(\r\x12\x1a\n\x0e\x61\x63\x63ount_number\x18\x02 \x01(\x04\x42\x02\x30\x01\x12\x10\n\x08\x63hain_id\x18\x03 \x01(\t\x12\x12\n\nfee_amount\x18\x04 \x01(\r\x12\x0b\n\x03gas\x18\x05 \x01(\r\x12\x0c\n\x04memo\x18\x06 \x01(\t\x12\x14\n\x08sequence\x18\x07 \x01(\x04\x42\x02\x30\x01\x12\x11\n\tmsg_count\x18\x08 \x01(\r\x12\x0f\n\x07testnet\x18\t \x01(\x08\x12\r\n\x05\x64\x65nom\x18\n \x01(\t\x12\x10\n\x08\x64\x65\x63imals\x18\x0b \x01(\x04\x12\x12\n\nchain_name\x18\x0c \x01(\t\x12\x1b\n\x13message_type_prefix\x18\r \x01(\t\"\x16\n\x14TendermintMsgRequest\"\xd3\x02\n\x10TendermintMsgAck\x12 \n\x04send\x18\x01 \x01(\x0b\x32\x12.TendermintMsgSend\x12(\n\x08\x64\x65legate\x18\x02 \x01(\x0b\x32\x16.TendermintMsgDelegate\x12,\n\nundelegate\x18\x03 \x01(\x0b\x32\x18.TendermintMsgUndelegate\x12,\n\nredelegate\x18\x04 \x01(\x0b\x32\x18.TendermintMsgRedelegate\x12&\n\x07rewards\x18\x05 \x01(\x0b\x32\x15.TendermintMsgRewards\x12/\n\x0cibc_transfer\x18\x06 \x01(\x0b\x32\x19.TendermintMsgIBCTransfer\x12\r\n\x05\x64\x65nom\x18\x07 \x01(\t\x12\x12\n\nchain_name\x18\x08 \x01(\t\x12\x1b\n\x13message_type_prefix\x18\t \x01(\t\"\x81\x01\n\x11TendermintMsgSend\x12\x14\n\x0c\x66rom_address\x18\x06 \x01(\t\x12\x12\n\nto_address\x18\x07 \x01(\t\x12\x12\n\x06\x61mount\x18\x08 \x01(\x04\x42\x02\x30\x01\x12(\n\x0c\x61\x64\x64ress_type\x18\t \x01(\x0e\x32\x12.OutputAddressTypeJ\x04\x08\n\x10\x0b\"a\n\x15TendermintMsgDelegate\x12\x19\n\x11\x64\x65legator_address\x18\x01 \x01(\t\x12\x19\n\x11validator_address\x18\x02 \x01(\t\x12\x12\n\x06\x61mount\x18\x03 \x01(\x04\x42\x02\x30\x01\"c\n\x17TendermintMsgUndelegate\x12\x19\n\x11\x64\x65legator_address\x18\x01 \x01(\t\x12\x19\n\x11validator_address\x18\x02 \x01(\t\x12\x12\n\x06\x61mount\x18\x03 \x01(\x04\x42\x02\x30\x01\"\x86\x01\n\x17TendermintMsgRedelegate\x12\x19\n\x11\x64\x65legator_address\x18\x01 \x01(\t\x12\x1d\n\x15validator_src_address\x18\x02 \x01(\t\x12\x1d\n\x15validator_dst_address\x18\x03 \x01(\t\x12\x12\n\x06\x61mount\x18\x04 \x01(\x04\x42\x02\x30\x01\"`\n\x14TendermintMsgRewards\x12\x19\n\x11\x64\x65legator_address\x18\x01 \x01(\t\x12\x19\n\x11validator_address\x18\x02 \x01(\t\x12\x12\n\x06\x61mount\x18\x03 \x01(\x04\x42\x02\x30\x01\"\xaa\x01\n\x18TendermintMsgIBCTransfer\x12\x10\n\x08receiver\x18\x01 \x01(\t\x12\x0e\n\x06sender\x18\x02 \x01(\t\x12\x16\n\x0esource_channel\x18\x03 \x01(\t\x12\x13\n\x0bsource_port\x18\x04 \x01(\t\x12\x17\n\x0frevision_height\x18\x05 \x01(\t\x12\x17\n\x0frevision_number\x18\x06 \x01(\t\x12\r\n\x05\x64\x65nom\x18\x07 \x01(\t\";\n\x12TendermintSignedTx\x12\x12\n\npublic_key\x18\x01 \x01(\x0c\x12\x11\n\tsignature\x18\x02 \x01(\x0c\x42?\n#com.shapeshift.keepkey.lib.protobufB\x18KeepKeyMessageTendermint')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'messages_tendermint_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n#com.shapeshift.keepkey.lib.protobufB\030KeepKeyMessageTendermint'
  _globals['_TENDERMINTSIGNTX'].fields_by_name['account_number']._loaded_options = None
  _globals['_TENDERMINTSIGNTX'].fields_by_name['account_number']._serialized_options = b'0\001'
  _globals['_TENDERMINTSIGNTX'].fields_by_name['sequence']._loaded_options = None
  _globals['_TENDERMINTSIGNTX'].fields_by_name['sequence']._serialized_options = b'0\001'
  _globals['_TENDERMINTMSGSEND'].fields_by_name['amount']._loaded_options = None
  _globals['_TENDERMINTMSGSEND'].fields_by_name['amount']._serialized_options = b'0\001'
  _globals['_TENDERMINTMSGDELEGATE'].fields_by_name['amount']._loaded_options = None
  _globals['_TENDERMINTMSGDELEGATE'].fields_by_name['amount']._serialized_options = b'0\001'
  _globals['_TENDERMINTMSGUNDELEGATE'].fields_by_name['amount']._loaded_options = None
  _globals['_TENDERMINTMSGUNDELEGATE'].fields_by_name['amount']._serialized_options = b'0\001'
  _globals['_TENDERMINTMSGREDELEGATE'].fields_by_name['amount']._loaded_options = None
  _globals['_TENDERMINTMSGREDELEGATE'].fields_by_name['amount']._serialized_options = b'0\001'
  _globals['_TENDERMINTMSGREWARDS'].fields_by_name['amount']._loaded_options = None
  _globals['_TENDERMINTMSGREWARDS'].fields_by_name['amount']._serialized_options = b'0\001'
  _globals['_TENDERMINTGETADDRESS']._serialized_start=42
  _globals['_TENDERMINTGETADDRESS']._serialized_end=166
  _globals['_TENDERMINTADDRESS']._serialized_start=168
  _globals['_TENDERMINTADDRESS']._serialized_end=204
  _globals['_TENDERMINTSIGNTX']._serialized_start=207
  _globals['_TENDERMINTSIGNTX']._serialized_end=477
  _globals['_TENDERMINTMSGREQUEST']._serialized_start=479
  _globals['_TENDERMINTMSGREQUEST']._serialized_end=501
  _globals['_TENDERMINTMSGACK']._serialized_start=504
  _globals['_TENDERMINTMSGACK']._serialized_end=843
  _globals['_TENDERMINTMSGSEND']._serialized_start=846
  _globals['_TENDERMINTMSGSEND']._serialized_end=975
  _globals['_TENDERMINTMSGDELEGATE']._serialized_start=977
  _globals['_TENDERMINTMSGDELEGATE']._serialized_end=1074
  _globals['_TENDERMINTMSGUNDELEGATE']._serialized_start=1076
  _globals['_TENDERMINTMSGUNDELEGATE']._serialized_end=1175
  _globals['_TENDERMINTMSGREDELEGATE']._serialized_start=1178
  _globals['_TENDERMINTMSGREDELEGATE']._serialized_end=1312
  _globals['_TENDERMINTMSGREWARDS']._serialized_start=1314
  _globals['_TENDERMINTMSGREWARDS']._serialized_end=1410
  _globals['_TENDERMINTMSGIBCTRANSFER']._serialized_start=1413
  _globals['_TENDERMINTMSGIBCTRANSFER']._serialized_end=1583
  _globals['_TENDERMINTSIGNEDTX']._serialized_start=1585
  _globals['_TENDERMINTSIGNEDTX']._serialized_end=1644
# @@protoc_insertion_point(module_scope)
