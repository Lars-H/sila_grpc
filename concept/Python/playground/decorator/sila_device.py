# TODO: Commenting and parameterize

def Sila_device(Cls):
    import is_sila_pb2
    import stdlib_pb2
    import grpc
    import time
    from concurrent import futures

    class NewCls(is_sila_pb2.is_silaServicer):
        def __init__(self,*args,**kwargs):
            self.oInstance = Cls(*args,**kwargs)
            self.__wsdl = 'Test'
            self.__int_vers = '0.1'
            self.server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

        def wsdl(self, request, context):
            msg = stdlib_pb2.String()
            msg.data = self.__wsdl
            return msg

        def sila_interface_version(self, request, context):
            msg = stdlib_pb2.String()
            msg.data = self.__int_vers
            return msg

        def run_server(self):
            self.server.add_insecure_port('[::]:50051')
            self.server.start()
            print('Server running.')
            try:
                while True:
                    time.sleep(60 * 60 * 24)
            except KeyboardInterrupt:
                self.server.stop(0)

    return NewCls
