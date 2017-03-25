import bluetooth

target_name = "HC-05"
target_address = None

def connect():
    print("Discovering nearby devices")
    nearby_devices = bluetooth.discover_devices()
    for device in nearby_devices:
        if target_name == bluetooth.lookup_name(device)
            target_address = device
            break
    if target_address is not None:
        print("Found target bluetooth device with address ")
        print(target_address)

def send_arduino(string):
	print("Sending signals to the Arduino")


