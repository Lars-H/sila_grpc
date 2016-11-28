from __future__ import print_function

import utils
import grpc
import protos.device_pb2 as device_pb2
import protos.SiLAService_pb2 as SiLAService_pb2
import logging
logging.basicConfig(level=logging.INFO)
from pprint import pprint

class DeviceClient:

    def __init__(self, *args):
        '''
        Initialize Client device
        Args:
            *args: Parameters, such as the socket for the stub channel
        '''
        if len(args) == 1 and isinstance(args[0], str):
            self.__channel = grpc.insecure_channel(args[0])
        else:
            self.__channel = grpc.insecure_channel('localhost:50051')

    # TODO: Make abstract class "SiLA Device" which needs to be implemented by every device
    def is_sila(self):
        """
        Execute IsSiLA RPC call
        Returns: SiLA Device Response

        """
        # Create stub to servie
        stub = SiLAService_pb2.SiLAServiceStub(self.__channel)

        # Get response
        response = stub.IsSiLA(SiLAService_pb2.Empty())

        # Return response
        return response

    def get_datastream(self, length):
        """
        Gets the temperature datastream of the server
        Args:
            length: Number of response to be returned

        Returns: String representation for each temperature observation

        """
        # Create stub to servie
        stub = device_pb2.ThermometerStub(self.__channel)

        # Get response
        datagrams = stub.TemperatureStream(device_pb2.StreamRequest(length=length))
        logging.info(datagrams.initial_metadata())

        i = 0
        # Return response
        try:
            for data in datagrams:
                yield (utils.temperature_str(data))
                i += 1

                # Example: Cancel Stream after 5 Messages have been received
                if i == 5:
                    datagrams.cancel()
                    break
        except grpc.RpcError as e:
            print(str(e))
            logging.exception(e.message)

    def get_datapoint(self):
        """
        Get a single temperature observation of the device
        Returns: String representation for the temperature observation

        """
        # Create stub to servie
        stub = device_pb2.ThermometerStub(self.__channel).Temperature
        # Get response
        try:
            # Using future in order to be able to read the metadata

            future = stub.future(SiLAService_pb2.Empty(), timeout=5)
            logging.info("Metadata: " + str(future.initial_metadata()))

            # Data is equal to the future result
            datagram = future.result()

            # Return response
            return utils.temperature_str(datagram)
        except Exception as e:
            logging.exception("An Error has occured")
            logging.exception(str(e))
            #pprint(dir(datagram))



