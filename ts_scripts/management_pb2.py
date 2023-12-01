# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: management.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10management.proto\x12!org.pytorch.serve.grpc.management\"!\n\x12ManagementResponse\x12\x0b\n\x03msg\x18\x01 \x01(\t\"U\n\x14\x44\x65scribeModelRequest\x12\x12\n\nmodel_name\x18\x01 \x01(\t\x12\x15\n\rmodel_version\x18\x02 \x01(\t\x12\x12\n\ncustomized\x18\x03 \x01(\x08\";\n\x11ListModelsRequest\x12\r\n\x05limit\x18\x01 \x01(\x05\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\x05\"\xe2\x01\n\x14RegisterModelRequest\x12\x12\n\nbatch_size\x18\x01 \x01(\x05\x12\x0f\n\x07handler\x18\x02 \x01(\t\x12\x17\n\x0finitial_workers\x18\x03 \x01(\x05\x12\x17\n\x0fmax_batch_delay\x18\x04 \x01(\x05\x12\x12\n\nmodel_name\x18\x05 \x01(\t\x12\x18\n\x10response_timeout\x18\x06 \x01(\x05\x12\x0f\n\x07runtime\x18\x07 \x01(\t\x12\x13\n\x0bsynchronous\x18\x08 \x01(\x08\x12\x0b\n\x03url\x18\t \x01(\t\x12\x12\n\ns3_sse_kms\x18\n \x01(\x08\"\xa1\x01\n\x12ScaleWorkerRequest\x12\x12\n\nmodel_name\x18\x01 \x01(\t\x12\x15\n\rmodel_version\x18\x02 \x01(\t\x12\x12\n\nmax_worker\x18\x03 \x01(\x05\x12\x12\n\nmin_worker\x18\x04 \x01(\x05\x12\x12\n\nnumber_gpu\x18\x05 \x01(\x05\x12\x13\n\x0bsynchronous\x18\x06 \x01(\x08\x12\x0f\n\x07timeout\x18\x07 \x01(\x05\">\n\x11SetDefaultRequest\x12\x12\n\nmodel_name\x18\x01 \x01(\t\x12\x15\n\rmodel_version\x18\x02 \x01(\t\"C\n\x16UnregisterModelRequest\x12\x12\n\nmodel_name\x18\x01 \x01(\t\x12\x15\n\rmodel_version\x18\x02 \x01(\t2\xa0\x06\n\x15ManagementAPIsService\x12\x81\x01\n\rDescribeModel\x12\x37.org.pytorch.serve.grpc.management.DescribeModelRequest\x1a\x35.org.pytorch.serve.grpc.management.ManagementResponse\"\x00\x12{\n\nListModels\x12\x34.org.pytorch.serve.grpc.management.ListModelsRequest\x1a\x35.org.pytorch.serve.grpc.management.ManagementResponse\"\x00\x12\x81\x01\n\rRegisterModel\x12\x37.org.pytorch.serve.grpc.management.RegisterModelRequest\x1a\x35.org.pytorch.serve.grpc.management.ManagementResponse\"\x00\x12}\n\x0bScaleWorker\x12\x35.org.pytorch.serve.grpc.management.ScaleWorkerRequest\x1a\x35.org.pytorch.serve.grpc.management.ManagementResponse\"\x00\x12{\n\nSetDefault\x12\x34.org.pytorch.serve.grpc.management.SetDefaultRequest\x1a\x35.org.pytorch.serve.grpc.management.ManagementResponse\"\x00\x12\x85\x01\n\x0fUnregisterModel\x12\x39.org.pytorch.serve.grpc.management.UnregisterModelRequest\x1a\x35.org.pytorch.serve.grpc.management.ManagementResponse\"\x00\x42\x02P\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'management_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'P\001'
  _globals['_MANAGEMENTRESPONSE']._serialized_start=55
  _globals['_MANAGEMENTRESPONSE']._serialized_end=88
  _globals['_DESCRIBEMODELREQUEST']._serialized_start=90
  _globals['_DESCRIBEMODELREQUEST']._serialized_end=175
  _globals['_LISTMODELSREQUEST']._serialized_start=177
  _globals['_LISTMODELSREQUEST']._serialized_end=236
  _globals['_REGISTERMODELREQUEST']._serialized_start=239
  _globals['_REGISTERMODELREQUEST']._serialized_end=465
  _globals['_SCALEWORKERREQUEST']._serialized_start=468
  _globals['_SCALEWORKERREQUEST']._serialized_end=629
  _globals['_SETDEFAULTREQUEST']._serialized_start=631
  _globals['_SETDEFAULTREQUEST']._serialized_end=693
  _globals['_UNREGISTERMODELREQUEST']._serialized_start=695
  _globals['_UNREGISTERMODELREQUEST']._serialized_end=762
  _globals['_MANAGEMENTAPISSERVICE']._serialized_start=765
  _globals['_MANAGEMENTAPISSERVICE']._serialized_end=1565
# @@protoc_insertion_point(module_scope)
