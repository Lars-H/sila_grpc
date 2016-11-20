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

    """

    # IsSiLA Command
    if re.match(commandStr, "IsSiLA", re.IGNORECASE):
        print (client.is_sila())

    # Device specific command
    elif re.match(commandStr, "temperature", re.IGNORECASE):
        if len(args) == 1:
            responses = client.get_datastream(int(args[0]))
            for response in responses:
                print str(response)
        else:
            print (client.get_datapoint())

    else:
        print ("Command not found.")


# Start endless loop for client to interact with server
if __name__ == '__main__':

    try:
        while True:
            print ("Enter a command: ")

            # Read Input
            inputStr =  raw_input()

            # Check for exit command to end loop
            if re.match(inputStr, "exit", re.IGNORECASE) or re.match(inputStr, "q", re.IGNORECASE):
                break;

            # Split input string to retrieve command and parameters
            inputStr = inputStr.split(" ")

            # Execute command
            if len(inputStr) >= 2:
                command(inputStr[0], inputStr[1:][0])
            else:
                command(commandStr=inputStr[0])
    except KeyboardInterrupt:
        print ("Client disconnected")
