# TODO: Error/Exception Handling


def Sila_client(Cls):
    from concept.Python.playground.decorator.features import is_sila_pb2
    import stdlib_pb2
    import grpc

    class NewCls():

        def __init__(self, *args, **kwargs):
            self.oInstance = Cls(*args, **kwargs)
            host = "localhost"
            port = "50051"
            self.target = host + ":" + port
            self.channel = grpc.insecure_channel(self.target)

        def wsdl(self, timeout=0):
            # Create stub to servie
            stub = is_sila_pb2.is_silaStub(self.channel)

            # Get response
            if timeout > 0:
                response = stub.wsdl(stdlib_pb2.Empty(), timeout=timeout)
            else:
                response = stub.wsdl(stdlib_pb2.Empty())

            # Return response
            return response

        def sila_interface_version(self):
            # Create stub to servie
            stub = is_sila_pb2.is_silaStub(self.channel)

            # Get response
            response = stub.sila_interface_version(stdlib_pb2.Empty())

            # Return response
            return response

        def manufacturer(self):
            # Create stub to servie
            stub = is_sila_pb2.is_silaStub(self.channel)

            # Get response
            response = stub.device_manufacturer(stdlib_pb2.Empty())

            # Return response
            return response

    return NewCls
