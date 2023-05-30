# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import protos_generated.webcontroller_pb2 as webcontroller__pb2


class AgentStub(object):
    """The greeting service definition.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.MoveInformation = channel.unary_unary(
                '/Agent/MoveInformation',
                request_serializer=webcontroller__pb2.MoveInformationRequest.SerializeToString,
                response_deserializer=webcontroller__pb2.MoveInformationReply.FromString,
                )


class AgentServicer(object):
    """The greeting service definition.
    """

    def MoveInformation(self, request, context):
        """Sends a greeting
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AgentServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'MoveInformation': grpc.unary_unary_rpc_method_handler(
                    servicer.MoveInformation,
                    request_deserializer=webcontroller__pb2.MoveInformationRequest.FromString,
                    response_serializer=webcontroller__pb2.MoveInformationReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Agent', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Agent(object):
    """The greeting service definition.
    """

    @staticmethod
    def MoveInformation(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Agent/MoveInformation',
            webcontroller__pb2.MoveInformationRequest.SerializeToString,
            webcontroller__pb2.MoveInformationReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
