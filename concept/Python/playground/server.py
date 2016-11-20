import random
import time

from concurrent import futures

import grpc
from protos import device_pb2, SiLAService_pb2

_ONE_DAY_IN_SECONDS = 60 * 60 * 24

class SiLAService(SiLAService_pb2.SiLAServiceServicer):
    """
    Class that implements the SiLA Service
    """

    def IsSiLA(self, request, context):
        """
        Returns the device information as definde by IsSiLA
        Args:
            request: Request message (Empty for IsSiLA)
            context: Request context

        Returns: Device information

        """

        msg = SiLAService_pb2.IsSiLAResponse()
        msg.serialNumber = 1 # Example data
        msg.manufacturer = "Merck" # Example data
        msg.model = "CER-B8" # Example data

        # Fake Information
        self.add_features(msg)
        return msg


    def add_features(self, msg):
        feature = msg.feature.add()
        feature.Identifier = "can-measure"
        feature.Version = "1.0"
        feature.DisplayName ="Measurement"
        feature.Description  = "Measures data"
        self.add_commands(feature)

    def add_commands(self, feature):
        command = feature.command.add()
        command.Identifier = "get-temperature"
        command.DisplayName = "Temperatur"
        command.Description = "Measures the current temperature"

        command = feature.command.add()
        command.Identifier = "get-temperatureStream"
        command.DisplayName = "TemperaturStream"
        command.Description = "Measures the temperature for a defined number of times and returns the stream"
        parameter = command.parameter.add()
        parameter.Identifier = "length"


class Device(device_pb2.ThermometerServicer):
    """
    Class that implements the Thermometer Service
    """

    def Temperature(self, request, context):
        """
        Temperature RPC Method
        Args:
            request: Request message
            context: Request Context

        Returns: Temperature Datapoint

        """
        print ("Temperature Request") # Log
        try:
            datapoint = device_pb2.Datapoint()
            metadata = [(b'device', b'Thermometer'), (b'version', b'0.1'), (b'precision', b'1 decimal')]
            context.send_initial_metadata(metadata)
            datapoint.value = 20  # Fake value
            datapoint.unit = 0
            return datapoint

        except Exception as e:
            print(e.message)
            context.set_code(grpc.StatusCode.UNKNOWN)
            context.set_details('An Error has occurred measuring the temperature value!')
            return device_pb2.Datapoint()

    def TemperatureStream(self, request, context):
        """
        Temperature Stream RPC Method
        Args:
            request: Request Method
            context: Request Context

        Returns: Datastream of temperature observations

        """
        print ("Temperature Stream Request")  # Log
        length = request.length
        metadata = [(b'device', b'Thermometer'), (b'version', b'0.1'), (b'precision', b'1 decimal')]
        context.send_initial_metadata(metadata)
        for i in range(0, length):
            time.sleep(1)
            datapoint = device_pb2.Datapoint()
            val = 20 + random.normalvariate(0, 2) # Fake values
            datapoint.value = val
            datapoint.unit = 0
            yield datapoint


def serve():
    """
    Main Server Loop
    Returns: None

    """
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    device_pb2.add_ThermometerServicer_to_server(Device(), server)
    SiLAService_pb2.add_SiLAServiceServicer_to_server(SiLAService(), server)

    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server running.")
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()
