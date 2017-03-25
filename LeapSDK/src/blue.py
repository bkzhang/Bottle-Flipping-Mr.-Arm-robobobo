import bluetooth

target_name = "HC-05"
target_address = None
port = 1

def connect():
    print("Discovering nearby devices")
    nearby_devices = bluetooth.discover_devices()
    for device in nearby_devices:
        if target_name == bluetooth.lookup_name(device):
            target_address = device
            break
    if target_address is not None:
        print("Found target bluetooth device with address ")
        print(target_address)
    else:
        print("Could not find target device")
        return

    sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    sock.connect(target_address, port)


def send_arduino(string):
    print("Sending signals to the Arduino")
    sock.send(string)

def main():
    connect()
    send_arduino("Hello")

if __name__ == "__main__":
    main()

