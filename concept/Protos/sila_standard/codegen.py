from grpc.tools import protoc

protofile = "is_sila"
cmd = (
    '' ,
    '-I.',
    '--python_out=.',
    '--grpc_python_out=.',
    str(protofile) + ".proto",
    )

protoc.main(cmd)