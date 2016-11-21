from sila_client import Sila_client


@Sila_client
class Balance_client():

    def name(self):
        return 'Balance'


bc = Balance_client()
result = bc.wsdl()

print (str(result))