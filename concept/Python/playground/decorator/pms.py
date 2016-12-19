import logging
logging.basicConfig(level=logging.INFO)
from grpc import StatusCode, RpcError
from concept.Python.playground.decorator.features.sila_client import Sila_client
from requests.auth import HTTPBasicAuth

@Sila_client
class Balance_client():

    def name(self):
        return 'PMS System'


bc = Balance_client()


try:
    result = bc.wsdl(timeout=5)
    #result = bc.sila_interface_version()
    #result = bc.manufacturer()

    print(result)

except RpcError as e:
    if e.code() == StatusCode.DEADLINE_EXCEEDED:
        logging.error(str(e.code()) + ": " + e.details())

    elif e.code() == StatusCode.UNAVAILABLE:
        logging.error(str(e.code()) + " @" + bc.target)

    elif e.code() == StatusCode.UNIMPLEMENTED:
        logging.error(str(e.code()) + ": Functionality not implemented")
    else:
        logging.error((e.code().value))
        logging.error(str(e.code()) + ": " + e.details())
