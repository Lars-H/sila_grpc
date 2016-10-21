from __future__ import print_function

import utils
import grpc
import protos.device_pb2 as device_pb2
import protos.SiLAService_pb2 as SiLAService_pb2

class DeviceClient:

    def __init__(self, *args):
        if len(args) == 1 and isinstance(args[0], str):
            self.__channel = grpc.insecure_channel(args[0])
        else:
            self.__channel = grpc.insecure_channel('localhost:50051')

    def is_sila(self):
        # Create stub to servie
        stub = SiLAService_pb2.SiLAServiceStub(self.__channel)

        # Get response
        response = stub.IsSiLA(SiLAService_pb2.Empty())

        # Return response
        return response

    def get_datastream(self, length):
        # Create stub to servie
        stub = device_pb2.ThermometerStub(self.__channel)

        # Get response
        datagrams = stub.TemperatureStream(device_pb2.StreamRequest(length=length))

        # Return response
        for data in datagrams:
            print (utils.temperature_str(data))

    def get_datapoint(self):
        # Create stub to servie
        stub= device_pb2.ThermometerStub(self.__channel)

        # Get response
        datagram = stub.Temperature(SiLAService_pb2.Empty())

        # Return response
        return utils.temperature_str(datagram)
