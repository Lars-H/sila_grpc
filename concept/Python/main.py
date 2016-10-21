import re

# Import the DeviceCLient that provides interface to the grpc service
from clients import DeviceClient

client = DeviceClient()


def command(commandStr, *args):
    """
    Executes command given by a command string
    Args:
        commandStr: String representing the command
        args: additional arguments, if necessary

    Returns:
    """

    # IsSiLA Command
    if re.match(commandStr, "IsSiLA", re.IGNORECASE):
        print (client.is_sila())

    # Device specific command
    elif re.match(commandStr, "temperature", re.IGNORECASE):
        if len(args) == 1:
            client.get_datastream(int(args[0]))
        else:
            print (client.get_datapoint())

    else:
        print ("Command not found.")


try:
    while True:
        print ("Enter a command: ")
        inputStr =  raw_input()
        if re.match(inputStr, "exit", re.IGNORECASE) or re.match(inputStr, "q", re.IGNORECASE):
            break;
        inputStr = inputStr.split(" ")
        if len(inputStr) >= 2:
            command(inputStr[0], inputStr[1:][0])
        else:
            command(commandStr=inputStr[0])
except KeyboardInterrupt:
    print ("Client disconnected")
