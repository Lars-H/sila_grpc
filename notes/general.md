# General Notes

## Issues:

- Naming of RPCs: "-" not allowed in .proto configuration, however used to describe features & commands (e.g. "get-temperature")
- Not having required fiedls in protocol buffers may be an issues, since a device cannot be "force" to provide the necessary information
- How to self-describe a device? Idea: If there is a consistent mapping, the .proto-File for a client could be generate from the IsSiLA-Response

## Ideas:

- For large data sets, use a grpc stream to send data step by step
- Additional to the SiLA Service specification (IsSiLA Command), add standard message such as enums for units (potentially split into a sepereate files)


## Questions:

- Definition of types and units as strings or enums?


## Further Task:

- A GUI to specifiy the properties of a device according to the standard would be helpful
	* Automatic generation of the mandatory "IsSiiLA" command according to the specs
	* Potentially, auto-generated .proto files for the device
