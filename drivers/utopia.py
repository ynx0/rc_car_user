from bluepy import btle
import time

class SnifferDelegate(btle.DefaultDelegate):
    def __init__(self, params):
        btle.DefaultDelegate.__init__(self)
        # init code?

    def handleNotif(self, cHandle, data):
        print("cHandle (characteristic's handle): " + str(cHandle))
        print("notif data" + str(data))


utopia_mac = "ff:ff:40:04:35:2d"

print("Connecting")
dev = btle.Peripheral(utopia_mac)
#characteristics = dev.getCharacteristics()
dev.setDelegate(SnifferDelegate(None))

while True:
    if dev.waitForNotifications(1.0):
        print("Notif recieved")
        continue

    print("Waiting for notification")





#battery = int.from_bytes(charac[-1], 'little') # is the last one

#
# def ls(char):
#     for c in char:
#         print(c)
#         print(c.read())
#
# while True:
#     ls(charac)
#     time.sleep(0.5)