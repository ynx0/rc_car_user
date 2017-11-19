from procbridge.procbridge import *
from rc_car import motor_controller as mc
from RC_Commands import Commands
import sys


localhost = '127.0.0.1'
port = 2323


def movement_handler(command, args):
    print("Command is: %s" % str(command))
    print("Args are: %s" % str(args))

    if command == Commands.FORWARD:
        mc.forward(args['speed'])
    elif command == Commands.BACKWARD:
        mc.backward(args['speed'])
    elif command == Commands.LEFT:
        mc.turnLeft()
    elif command == Commands.RIGHT:
        mc.turnRight()
    elif command == Commands.STOP:
        mc.stopAll()
    elif command == Commands.SHUTDOWN:
        mc.stopAll()
        mc.cleanup()
        server.stop()
        sys.exit(0)
    else:
        print("Error: Unknown command: " + command)

server = ProcBridgeServer(localhost, port, movement_handler)

def start():
    mc.setup()
    server.start()
    # the only way to indefinitely keep open the server.
    while True:
        pass


if __name__ == '__main__':
    try:
        start()
    except KeyboardInterrupt:
        server.stop()
        print("Stopping server...")
