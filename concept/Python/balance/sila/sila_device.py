from features import is_sila_pb2
import features.stdlib_pb2 as stdlib_pb2
import grpc
import time
import json
import random
import logging

from concurrent import futures

class Sila_device(is_sila_pb2.is_silaServicer):

    """
    Class that provides the commands and properties for the standard sila feature
    """

    def __init__(self,*args,**kwargs):

        # Set up Logger
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger('is_sila')

    def inititialize_information(self, info_file):

        # Initialize Information
        logging.info("Loading Information from: " + info_file)
        try:
            with open(info_file, 'r') as file:
                self.__device_identification = json.loads(file.read())['is_sila']
        except Exception as e:
            logging.error("Could not initilaize device information")
            logging.error(e.message)

    def device_identification(self, request, context):
        self.logger.info('Device Information request')

        try:
            msg = is_sila_pb2.DeviveIdentification()
            msg.wsdl = self.__device_identification['wsdl']
            msg.sila_interface_version = self.__device_identification['sila_interface_version']
            msg.device_manufacturer = self.__device_identification['device_manufacturer']
            msg.device_name = self.__device_identification['device_name']
            msg.device_serial_number = self.__device_identification['device_serial_number']
            msg.device_firmware_version = self.__device_identification['device_firmware_version']
            return msg
        except KeyError as e:
            logging.exception("An exception has occured: " + e.message)
            error_msg = stdlib_pb2.SiLA_Error_Message()
            error_msg.type = "Unknown Execution Error"
            error_msg.description = "No valid device Information Found."
            error_msg_str = error_msg.SerializeToString()
            context.set_details(error_msg_str)
            context.set_code(grpc.StatusCode.ABORTED)
            return is_sila_pb2.DeviveIdentification()

    def supported_features(self, request, context):
        pass


