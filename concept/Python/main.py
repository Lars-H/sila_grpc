from clients import DeviceClient

client = DeviceClient()
print (client.is_sila())


try:
    while True:
        print("Tets")
except KeyboardInterrupt:
    print ("Client disconnected")
