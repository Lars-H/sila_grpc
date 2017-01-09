import logging
logging.basicConfig(level=logging.INFO)
from grpc import StatusCode, RpcError
from concept.Python.playground.decorator.features.sila_client import Sila_client
from concept.Python.playground.decorator.features.sila_error_pb2 import SiLA_Error_Message
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

    # Example for SiLA Specific Data
    elif e.code() == StatusCode.ABORTED:
        # Deserialize Message
        error_msg = SiLA_Error_Message().FromString(e.details())

        # Log: Type, Description and Redirect (if available)
        logging.error("Error Type: " + error_msg.type)
        logging.error("Error Description: " + error_msg.description)
        if error_msg.redirect == "":
            logging.info("No error handling mechanism provided")
        else:
            logging.info("Redirection to " + error_msg.redirect)

    else:
        logging.error((e.code().value))
        logging.error(str(e.code()) + ": " + e.details())
