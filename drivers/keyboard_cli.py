from RC_Commands import Commands
import msvcrt
from procbridge.procbridge import *




# adapted from https://stackoverflow.com/a/34497639/3807967
class Arrows():
    LEFT = 75
    RIGHT = 77
    UP = 72
    DOWN = 80

DEFAULT_SPEED = 35

def start():
    print("Starting driver: " + __file__)
    print("Use the arrow keys to drive the car")
    print("'s' to stop")
    print("'e' to exit")

    host = '192.168.0.124'
    port = 9939
    client = ProcBridge(host, port)

    while True:
        key = msvcrt.getch()

        if key == b's':
            client.request(Commands.STOP, {})
        elif key == b'e':
            client.request(Commands.SHUTDOWN, {})
        elif key == b'\x0e':
            # this means arrow key
            arrow = int.from_bytes(msvcrt.getch())
            if arrow == Arrows.RIGHT:
                client.request(Commands.RIGHT)
            elif arrow == Arrows.LEFT:
                client.request(Commands.LEFT)
            elif arrow == Arrows.UP:
                client.request(Commands.FORWARD, {"speed": DEFAULT_SPEED})
            elif arrow == Arrows.DOWN:
                client.request(Commands.BACKWARD, {"speed" : DEFAULT_SPEED})
            else:
                print("Unknown arrow/keycode" + str(arrow))
        else:
            pass

if __name__ == '__main__':
    start()
