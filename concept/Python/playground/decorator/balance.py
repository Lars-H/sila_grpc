from concept.Python.playground.decorator.features.sila_device import Sila_device

@Sila_device
class Balance():


    def name(self):
        return self._information['device_name']



balance = Balance("mt_ml_info.txt")
balance.run_server()