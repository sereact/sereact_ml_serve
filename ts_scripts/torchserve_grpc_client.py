import argparse
import queue
import threading
from functools import partial

import grpc
import inference_pb2
import inference_pb2_grpc
import management_pb2
import management_pb2_grpc
from pickgpt.sm.msgpack_utils import pack_msg, unpack_msg

def get_inference_stub():
    channel = grpc.insecure_channel("localhost:7070")
    stub = inference_pb2_grpc.InferenceAPIsServiceStub(channel)
    return stub


def get_management_stub():
    channel = grpc.insecure_channel("localhost:7071")
    stub = management_pb2_grpc.ManagementAPIsServiceStub(channel)
    return stub


def infer(stub, model_name):
    metadata = (("protocol", "gRPC"), ("session_id", "12345"))

    from PIL import Image
    import numpy as np

    img = np.asarray(Image.open('../cropped_rgb.png'))

    prompt = 'Can you segment the tape?'
    data = {'images': img, 'prompt' : prompt}
    data = pack_msg(data)
    input_data = {"data": data}
    response = stub.Predictions(
        inference_pb2.PredictionsRequest(model_name=model_name, input=input_data),
        metadata=metadata,
    )

    response = unpack_msg(response.prediction)
    print(response)

infer(get_inference_stub(), 'lisa')