# TODO: Error/Exception Handling

def Sila_client(Cls):
    import is_sila_pb2
    import stdlib_pb2
    import grpc

    class NewCls():

        def __init__(self,*args, **kwargs):
            self.oInstance = Cls(*args,**kwargs)
            self.channel = grpc.insecure_channel('localhost:50051')


        def wsdl(self):
            # Create stub to servie
            stub = is_sila_pb2.is_silaStub(self.channel)

            # Get response
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

    return NewCls
