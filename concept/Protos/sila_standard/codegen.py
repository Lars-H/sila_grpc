from grpc.tools import protoc

protofile = "stdlib"
cmd = (
    '',
    '-I.',
    '--python_out=.',
    '--grpc_python_out=.',
    str(protofile) + ".proto",
)

protoc.main(cmd)
