from grpc.tools import protoc



build = "device"

if build == "device":
    protoc.main(
        (
        '',
        '-I.',
        '--python_out=.',
        '--grpc_python_out=.',
        'device.proto',
        )
    )

elif build == "sila":
    protoc.main(
        (
        '',
        '-I.',
        '--python_out=.',
        '--grpc_python_out=.',
        'SiLAService.proto',
        )
    )
