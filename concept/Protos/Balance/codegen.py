from grpc.tools import protoc

protofile = "balance"
cmd = (
    '' ,
    '-I../Protos/',
    '--python_out=.',
    '--grpc_python_out=.',
    str(protofile) + ".proto",
    )

protoc.main(cmd)