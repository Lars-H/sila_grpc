import sys
import re
from grpc.tools import protoc

buildSiLA = False
buildDevice = False

def build():

    print ("Status: Build started")
    try:
        if buildDevice:
            protoc.main(
                (
                    '',
                    '-I.',
                    '--python_out=.',
                    '--grpc_python_out=.',
                    'device.proto',
                )
            )
            print ("Status: Device built")

        if buildSiLA:
            protoc.main(
                (
                    '',
                    '-I.',
                    '--python_out=.',
                    '--grpc_python_out=.',
                    'SiLAService.proto',
                )
            )
            print ("Status: SiLA built")
    except Exception as e:
        print ("Status: Build Exception occured")
        print (str(e.message))

if __name__ == "__main__":
    print (sys.argv)
    if len(sys.argv) == 1:
        # Build both
        buildSiLA =True
        buildDevice = True

    elif len(sys.argv) == 2:
        protoname = sys.argv[1]
        if re.match("sila", protoname, re.IGNORECASE):
            buildSiLA = True

        elif re.match("device", protoname, re.IGNORECASE):
            buildDevice = True
    else:
        print ("Invalid Arguments")

    build()

