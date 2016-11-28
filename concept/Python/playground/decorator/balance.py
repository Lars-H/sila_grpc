from sila_device import Sila_device

@Sila_device
class Balance():


    def name(self):
        return self.__wsdl



balance = Balance()
balance.run_server()