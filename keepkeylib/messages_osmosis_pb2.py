# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: messages-osmosis.proto
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
    'messages-osmosis.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import types_pb2 as types__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16messages-osmosis.proto\x1a\x0btypes.proto\"M\n\x11OsmosisGetAddress\x12\x11\n\taddress_n\x18\x01 \x03(\r\x12\x14\n\x0cshow_display\x18\x02 \x01(\x08\x12\x0f\n\x07testnet\x18\x03 \x01(\x08\"!\n\x0eOsmosisAddress\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\"\xb9\x01\n\rOsmosisSignTx\x12\x11\n\taddress_n\x18\x01 \x03(\r\x12\x1a\n\x0e\x61\x63\x63ount_number\x18\x02 \x01(\x04\x42\x02\x30\x01\x12\x10\n\x08\x63hain_id\x18\x03 \x01(\t\x12\x12\n\nfee_amount\x18\x04 \x01(\r\x12\x0b\n\x03gas\x18\x05 \x01(\r\x12\x0c\n\x04memo\x18\x06 \x01(\t\x12\x14\n\x08sequence\x18\x07 \x01(\x04\x42\x02\x30\x01\x12\x11\n\tmsg_count\x18\x08 \x01(\r\x12\x0f\n\x07testnet\x18\t \x01(\x08\"\x13\n\x11OsmosisMsgRequest\"\xb7\x03\n\rOsmosisMsgAck\x12\x1d\n\x04send\x18\x01 \x01(\x0b\x32\x0f.OsmosisMsgSend\x12%\n\x08\x64\x65legate\x18\x02 \x01(\x0b\x32\x13.OsmosisMsgDelegate\x12)\n\nundelegate\x18\x03 \x01(\x0b\x32\x15.OsmosisMsgUndelegate\x12)\n\nredelegate\x18\x04 \x01(\x0b\x32\x15.OsmosisMsgRedelegate\x12#\n\x07rewards\x18\x05 \x01(\x0b\x32\x12.OsmosisMsgRewards\x12 \n\x06lp_add\x18\x06 \x01(\x0b\x32\x10.OsmosisMsgLPAdd\x12&\n\tlp_remove\x18\x07 \x01(\x0b\x32\x13.OsmosisMsgLPRemove\x12$\n\x08lp_stake\x18\x08 \x01(\x0b\x32\x12.OsmosisMsgLPStake\x12(\n\nlp_unstake\x18\t \x01(\x0b\x32\x14.OsmosisMsgLPUnstake\x12,\n\x0cibc_transfer\x18\n \x01(\x0b\x32\x16.OsmosisMsgIBCTransfer\x12\x1d\n\x04swap\x18\x0b \x01(\x0b\x32\x0f.OsmosisMsgSwap\"\x83\x01\n\x0eOsmosisMsgSend\x12\x14\n\x0c\x66rom_address\x18\x01 \x01(\t\x12\x12\n\nto_address\x18\x02 \x01(\t\x12\r\n\x05\x64\x65nom\x18\x03 \x01(\t\x12\x0e\n\x06\x61mount\x18\x04 \x01(\t\x12(\n\x0c\x61\x64\x64ress_type\x18\x05 \x01(\x0e\x32\x12.OutputAddressType\"i\n\x12OsmosisMsgDelegate\x12\x19\n\x11\x64\x65legator_address\x18\x01 \x01(\t\x12\x19\n\x11validator_address\x18\x02 \x01(\t\x12\r\n\x05\x64\x65nom\x18\x03 \x01(\t\x12\x0e\n\x06\x61mount\x18\x04 \x01(\t\"k\n\x14OsmosisMsgUndelegate\x12\x19\n\x11\x64\x65legator_address\x18\x01 \x01(\t\x12\x19\n\x11validator_address\x18\x02 \x01(\t\x12\r\n\x05\x64\x65nom\x18\x03 \x01(\t\x12\x0e\n\x06\x61mount\x18\x04 \x01(\t\"\x8e\x01\n\x14OsmosisMsgRedelegate\x12\x19\n\x11\x64\x65legator_address\x18\x01 \x01(\t\x12\x1d\n\x15validator_src_address\x18\x02 \x01(\t\x12\x1d\n\x15validator_dst_address\x18\x03 \x01(\t\x12\r\n\x05\x64\x65nom\x18\x04 \x01(\t\x12\x0e\n\x06\x61mount\x18\x05 \x01(\t\"\xb2\x01\n\x0fOsmosisMsgLPAdd\x12\x0e\n\x06sender\x18\x01 \x01(\t\x12\x13\n\x07pool_id\x18\x02 \x01(\x04\x42\x02\x30\x01\x12\x18\n\x10share_out_amount\x18\x03 \x01(\t\x12\x16\n\x0e\x64\x65nom_in_max_a\x18\x04 \x01(\t\x12\x17\n\x0f\x61mount_in_max_a\x18\x05 \x01(\t\x12\x16\n\x0e\x64\x65nom_in_max_b\x18\x06 \x01(\t\x12\x17\n\x0f\x61mount_in_max_b\x18\x07 \x01(\t\"\xb8\x01\n\x12OsmosisMsgLPRemove\x12\x0e\n\x06sender\x18\x01 \x01(\t\x12\x13\n\x07pool_id\x18\x02 \x01(\x04\x42\x02\x30\x01\x12\x17\n\x0fshare_in_amount\x18\x03 \x01(\t\x12\x17\n\x0f\x64\x65nom_out_min_a\x18\x04 \x01(\t\x12\x18\n\x10\x61mount_out_min_a\x18\x05 \x01(\t\x12\x17\n\x0f\x64\x65nom_out_min_b\x18\x06 \x01(\t\x12\x18\n\x10\x61mount_out_min_b\x18\x07 \x01(\t\"W\n\x11OsmosisMsgLPStake\x12\r\n\x05owner\x18\x01 \x01(\t\x12\x14\n\x08\x64uration\x18\x02 \x01(\x04\x42\x02\x30\x01\x12\r\n\x05\x64\x65nom\x18\x04 \x01(\t\x12\x0e\n\x06\x61mount\x18\x05 \x01(\t\"0\n\x13OsmosisMsgLPUnstake\x12\r\n\x05owner\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\"I\n\x11OsmosisMsgRewards\x12\x19\n\x11\x64\x65legator_address\x18\x01 \x01(\t\x12\x19\n\x11validator_address\x18\x02 \x01(\t\"\xb7\x01\n\x15OsmosisMsgIBCTransfer\x12\x13\n\x0bsource_port\x18\x01 \x01(\t\x12\x16\n\x0esource_channel\x18\x02 \x01(\t\x12\r\n\x05\x64\x65nom\x18\x03 \x01(\t\x12\x0e\n\x06\x61mount\x18\x04 \x01(\t\x12\x0e\n\x06sender\x18\x05 \x01(\t\x12\x10\n\x08receiver\x18\x06 \x01(\t\x12\x17\n\x0frevision_number\x18\x07 \x01(\t\x12\x17\n\x0frevision_height\x18\x08 \x01(\t\"\x9d\x01\n\x0eOsmosisMsgSwap\x12\x0e\n\x06sender\x18\x01 \x01(\t\x12\x13\n\x07pool_id\x18\x02 \x01(\x04\x42\x02\x30\x01\x12\x17\n\x0ftoken_out_denom\x18\x03 \x01(\t\x12\x16\n\x0etoken_in_denom\x18\x04 \x01(\t\x12\x17\n\x0ftoken_in_amount\x18\x05 \x01(\t\x12\x1c\n\x14token_out_min_amount\x18\x06 \x01(\t\"8\n\x0fOsmosisSignedTx\x12\x12\n\npublic_key\x18\x01 \x01(\x0c\x12\x11\n\tsignature\x18\x02 \x01(\x0c\x42\x33\n\x1a\x63om.keepkey.deviceprotocolB\x15KeepKeyMessageOsmosis')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'messages_osmosis_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\032com.keepkey.deviceprotocolB\025KeepKeyMessageOsmosis'
  _globals['_OSMOSISSIGNTX'].fields_by_name['account_number']._loaded_options = None
  _globals['_OSMOSISSIGNTX'].fields_by_name['account_number']._serialized_options = b'0\001'
  _globals['_OSMOSISSIGNTX'].fields_by_name['sequence']._loaded_options = None
  _globals['_OSMOSISSIGNTX'].fields_by_name['sequence']._serialized_options = b'0\001'
  _globals['_OSMOSISMSGLPADD'].fields_by_name['pool_id']._loaded_options = None
  _globals['_OSMOSISMSGLPADD'].fields_by_name['pool_id']._serialized_options = b'0\001'
  _globals['_OSMOSISMSGLPREMOVE'].fields_by_name['pool_id']._loaded_options = None
  _globals['_OSMOSISMSGLPREMOVE'].fields_by_name['pool_id']._serialized_options = b'0\001'
  _globals['_OSMOSISMSGLPSTAKE'].fields_by_name['duration']._loaded_options = None
  _globals['_OSMOSISMSGLPSTAKE'].fields_by_name['duration']._serialized_options = b'0\001'
  _globals['_OSMOSISMSGSWAP'].fields_by_name['pool_id']._loaded_options = None
  _globals['_OSMOSISMSGSWAP'].fields_by_name['pool_id']._serialized_options = b'0\001'
  _globals['_OSMOSISGETADDRESS']._serialized_start=39
  _globals['_OSMOSISGETADDRESS']._serialized_end=116
  _globals['_OSMOSISADDRESS']._serialized_start=118
  _globals['_OSMOSISADDRESS']._serialized_end=151
  _globals['_OSMOSISSIGNTX']._serialized_start=154
  _globals['_OSMOSISSIGNTX']._serialized_end=339
  _globals['_OSMOSISMSGREQUEST']._serialized_start=341
  _globals['_OSMOSISMSGREQUEST']._serialized_end=360
  _globals['_OSMOSISMSGACK']._serialized_start=363
  _globals['_OSMOSISMSGACK']._serialized_end=802
  _globals['_OSMOSISMSGSEND']._serialized_start=805
  _globals['_OSMOSISMSGSEND']._serialized_end=936
  _globals['_OSMOSISMSGDELEGATE']._serialized_start=938
  _globals['_OSMOSISMSGDELEGATE']._serialized_end=1043
  _globals['_OSMOSISMSGUNDELEGATE']._serialized_start=1045
  _globals['_OSMOSISMSGUNDELEGATE']._serialized_end=1152
  _globals['_OSMOSISMSGREDELEGATE']._serialized_start=1155
  _globals['_OSMOSISMSGREDELEGATE']._serialized_end=1297
  _globals['_OSMOSISMSGLPADD']._serialized_start=1300
  _globals['_OSMOSISMSGLPADD']._serialized_end=1478
  _globals['_OSMOSISMSGLPREMOVE']._serialized_start=1481
  _globals['_OSMOSISMSGLPREMOVE']._serialized_end=1665
  _globals['_OSMOSISMSGLPSTAKE']._serialized_start=1667
  _globals['_OSMOSISMSGLPSTAKE']._serialized_end=1754
  _globals['_OSMOSISMSGLPUNSTAKE']._serialized_start=1756
  _globals['_OSMOSISMSGLPUNSTAKE']._serialized_end=1804
  _globals['_OSMOSISMSGREWARDS']._serialized_start=1806
  _globals['_OSMOSISMSGREWARDS']._serialized_end=1879
  _globals['_OSMOSISMSGIBCTRANSFER']._serialized_start=1882
  _globals['_OSMOSISMSGIBCTRANSFER']._serialized_end=2065
  _globals['_OSMOSISMSGSWAP']._serialized_start=2068
  _globals['_OSMOSISMSGSWAP']._serialized_end=2225
  _globals['_OSMOSISSIGNEDTX']._serialized_start=2227
  _globals['_OSMOSISSIGNEDTX']._serialized_end=2283
# @@protoc_insertion_point(module_scope)
