# TODO: Commenting and parameterize

def Sila_device(Cls):
    from concept.Python.playground.decorator.features import is_sila_pb2
    import stdlib_pb2
    import grpc
    import time
    import json
    import random
    import logging
    from concurrent import futures

    class NewCls(is_sila_pb2.is_silaServicer):
        """
        Class that provides the commands and properties for the standard sila feature
        """

        def __init__(self,*args,**kwargs):
            # Initial base class
            self.oInstance = Cls()

            # Set up Logger
            logging.basicConfig(level=logging.INFO)
            self.logger = logging.getLogger('is_sila')

            # Initilize
            self._initialized = False

            # Initialize Information
            if len(args) >= 1:
                try:
                    with open(args[0], 'r') as file:
                        self._information = json.loads(file.read())['is_sila']
                        self._initialized = True
                except:
                    logging.error("Could not initialize device information")
            else:
                logging.info("Device not initilized yet")


            # Set up Server
            self.server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

            is_sila_pb2.add_is_silaServicer_to_server(self, self.server)

        def inititialize_information(self, info_file):

            # Initialize Information
            try:
                with open(info_file, 'r') as file:
                    self._information = json.loads(file)
            except:
                logging.error("Could not initilaize device information")

        def wsdl(self, request, context):

            slp = random.randint(0,10)
            self.logger.info("Waiting for %d seconds", slp)
            self.logger.info('WSDL request')
            #time.sleep(7)

            try:
                msg = stdlib_pb2.String()
                msg.data = self._information['wsdl']
                return msg
            except KeyError as e:
                logging.exception("An exception has occured: " + e.message)
                context.set_details('SiLA Device: Information not found')
                context.set_code(grpc.StatusCode.INTERNAL)
                return stdlib_pb2.String()


        def sila_interface_version(self, request, context):

            self.logger.info('SiLA Interface Version request')

            try:
                msg = stdlib_pb2.String()
                msg.data = self._information['sila_interface_version']
                return msg
            except KeyError as e:
                logging.exception("An exception has occured: " + e.message)
                context.set_details('SiLA Device: Information not found')
                context.set_code(grpc.StatusCode.INTERNAL)
                return stdlib_pb2.String()

        def run_server(self):
            if self._initialized:
                self.server.add_insecure_port('[::]:50051')
                self.server.start()
                self.logger.info('Server running')
                try:
                    while True:
                        time.sleep(60 * 60 * 24)
                except KeyboardInterrupt:
                    self.server.stop(0)
            else:
                logging.error("Could not start server. Device information has not been initialized.")
    return NewCls
