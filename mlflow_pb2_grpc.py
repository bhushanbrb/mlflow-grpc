# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import mlflow_pb2 as mlflow__pb2


class MLflowStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.predict = channel.unary_unary(
        '/MLflow/predict',
        request_serializer=mlflow__pb2.Input.SerializeToString,
        response_deserializer=mlflow__pb2.Output.FromString,
        )


class MLflowServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def predict(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_MLflowServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'predict': grpc.unary_unary_rpc_method_handler(
          servicer.predict,
          request_deserializer=mlflow__pb2.Input.FromString,
          response_serializer=mlflow__pb2.Output.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'MLflow', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
