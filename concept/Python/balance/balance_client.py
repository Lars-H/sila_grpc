import grpc
import sila.features.can_weigh_pb2 as can_weigh
import sila.features.is_sila_pb2 as is_sila
import sila.features.stdlib_pb2 as stdlib
import logging
logging.basicConfig(level=logging.INFO)
from pint import UnitRegistry
ureg = UnitRegistry()
Q_ = ureg.Quantity

class BalanceClient():
    def __init__(self):
        host = "localhost"
        port = "50051"
        self.target = host + ":" + port
        self.channel = grpc.insecure_channel(self.target)
        self.calibrate()

    def current_weight(self, frequency=None, threshold=None):

        stub = can_weigh.can_weighStub(self.channel)
        request = stdlib.SiLA_Property_Request()

        if not frequency is None:
            request.frequency.value = frequency.to_base_units().magnitude
            request.frequency.unit.value = '{:~P}'.format(
                    frequency.to_base_units().units)
        if not threshold is None:
            request.threshold.value = threshold.to_base_units().magnitude
            request.threshold.unit.value = '{:~P}'.format(
                threshold.to_base_units().units)


        weight_stream = stub.current_weight(request)
        return weight_stream

    def calibrate(self):
        stub = can_weigh.can_weighStub(self.channel)
        stub.calibrate_balance(stdlib.Void())

    def stable_measurement(self):
        stub = can_weigh.can_weighStub(self.channel)
        return stub.measure_stable_weight(stdlib.Void())

    def device_identification(self):
        stub = is_sila.is_silaStub(self.channel)
        return stub.device_identification(stdlib.Void())

if __name__ == '__main__':
    client = BalanceClient()
    frequency = Q_(1, 's')
    threshold = Q_(10, 'g')


    # Single Property Request
    #datagrams = client.current_weight()

    # Frequency Request
    #datagrams = client.current_weight(frequency=frequency)

    # Threshold Request
    #datagrams = client.current_weight(threshold=threshold)

    # Frequnecy and Threshold Request
    #datagrams = client.current_weight(frequency=frequency, threshold=threshold)

    # Stable Measurement
    print (client.stable_measurement())

    # Device Identification
    print (client.device_identification())

    datagrams = []
    try:
        i = 0
        for value in datagrams:
            print value
            i += 1
            if i == 10:
                datagrams.cancel()

    except grpc.RpcError as grpc_error:
        if grpc_error.code() == grpc.StatusCode.CANCELLED:
            logging.info("The stream has been cancelled.")

