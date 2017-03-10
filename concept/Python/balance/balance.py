from concurrent import futures
import time
import grpc
import logging
logging.basicConfig(level=logging.INFO)
from sila.sila_device import Sila_device
from sila.features import stdlib_pb2 as stdlib
import sila.features.is_sila_pb2 as is_sila
import sila.features.can_weigh_pb2 as can_weigh
from sila.simulator import Simulator
import datetime as dt
from pint import UnitRegistry
import copy
import threading
ureg = UnitRegistry()
Q_ = ureg.Quantity


class Balance(Sila_device, can_weigh.can_weighServicer):

    def __init__(self):
        self.logger = logging.getLogger('balance')

        self.__calibrated = False
        self.__precision = Q_(1, 'mg')
        self.__weight = Q_(0, 'g')
        self.__tara_weight = Q_(0, 'g')

        sim_process = Simulator(self)

    @property
    def calibrated(self):
        return self.__calibrated

    @calibrated.setter
    def calibrated(self, value):
        self.__calibrated = value

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, value):
        self.__weight = value

    def get_measurement(self, context):
        if self.calibrated:
            measurement = stdlib.PhysicalValue()
            measurement.value = self.__weight.to_base_units().magnitude - \
                self.__tara_weight.to_base_units().magnitude
            measurement.unit.value = '{:~P}'.format(
                self.weight.to_base_units().units)
            return measurement
        else:
            logging.exception(
                "Standard Execution Error: Balance not calibrated")
            error_msg = stdlib.SiLA_Error_Message()
            error_msg.type = "Standard Execution Error"
            error_msg.description = "Balance has not been calibrated yet."
            error_msg_str = error_msg.SerializeToString()
            context.set_details(error_msg_str)
            context.set_code(grpc.StatusCode.ABORTED)
            return stdlib.PhysicalValue()

    def measure_stable_weight(self, request, context):
        logging.info("measure_stable_weight reuqest")
        logging.info("Current weight: " + str(self.weight))
        logging.info("Tara weight: " + str(self.__tara_weight))
        return self.get_measurement(context)

    def calibrate_balance(self, request, context):
        logging.info("calibrate_balance request")
        self.calibrated = True
        return stdlib.Void()

    def set_tara(self, request, context):
        logging.info("set_tara reuqest")
        self.__tara_weight = self.weight
        logging.info("Seting tara weight to: " + str(self.__tara_weight))
        return stdlib.Void()

    def reset_tara(self, request, context):
        logging.info("reset_tara request")
        self.__tara_weight = Q_(0, 'g')
        return stdlib.Void()

    def precision(self, request, context):
        logging.info("precision requets")
        precision = stdlib.PhysicalValue()
        precision.value = self.__precision.to_base_units().magnitude
        precision.unit.value = '{:~P}'.format(
            self.__precision.to_base_units().units)

        return precision

    def current_weight(self, request, context):

        # Logging
        logging.info("current_weight request")

        # Add a callback for cancelled streams
        context.add_callback(self.cancel_stream)

        # Retrieve Parameter from request
        frequency = Q_(request.frequency.value,
                       str(request.frequency.unit.value))

        threshold = Q_(request.threshold.value,
                       str(request.threshold.unit.value))

        # Parameters for stream is given
        if (frequency.magnitude != 0) or (threshold.magnitude != 0):
            try:
                if frequency.magnitude > 0 and threshold.magnitude > 0:
                    current_weight = Q_(
                        self.weight.magnitude, self.weight.units)
                    t0 = dt.datetime.now()
                    while (True):
                        if abs(current_weight.to_base_units().magnitude -
                               self.weight.to_base_units().magnitude)\
                                >= threshold.to_base_units().magnitude:
                            current_weight = self.weight
                            yield self.get_measurement(context)
                        if (dt.datetime.now() -
                                t0).total_seconds() > frequency.to_base_units().magnitude:
                            t0 = dt.datetime.now()
                            yield self.get_measurement(context)

                elif frequency.magnitude > 0:
                    while (True):
                        yield self.get_measurement(context)
                        time.sleep(frequency.to_base_units().magnitude)

                elif threshold.magnitude > 0:
                    current_weight = Q_(
                        self.weight.magnitude, self.weight.units)

                    # Not a nice comparison, but there seem to be issues with
                    # the pint library
                    while (True):
                        if abs(current_weight.to_base_units().magnitude -
                               self.weight.to_base_units().magnitude)\
                                >= threshold.to_base_units().magnitude:
                            current_weight = self.weight
                            yield self.get_measurement(context)

            except Exception as e:
                logging.exception("Unknown Execution Error")
                error_msg = stdlib.SiLA_Error_Message()
                error_msg.type = "Unknown Execution Error"
                error_msg.description = e.message
                error_msg_str = error_msg.SerializeToString()
                context.set_details(error_msg_str)
                context.set_code(grpc.StatusCode.ABORTED)
                yield stdlib.PhysicalValue()

        # Otherwise, only a single response is sent
        else:
            logging.info("Basic Property Request")
            yield self.get_measurement(context)

    def cancel_stream(self):
        logging.info("The stream has been canelled.")

    def run(self):
        self.server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        is_sila.add_is_silaServicer_to_server(self, self.server)
        can_weigh.add_can_weighServicer_to_server(self, self.server)
        self.server.add_insecure_port('[::]:50051')
        self.server.start()
        self.logger.info('Server running')
        try:
            while True:
                time.sleep(60 * 60 * 24)
        except KeyboardInterrupt:
            self.server.stop(0)


if __name__ == '__main__':
    balance = Balance()
    balance.inititialize_information("device_identification.txt")
    balance.run()
