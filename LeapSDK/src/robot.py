import sys
from importLeap import pyLeap
from listener import Listener

def controller():
    listener = Listener()
    controller = pyLeap.Controller()

    controller.add_listener(listener)

    print "Press any key to quit"
    try:
        sys.stdin.readline()
    except KeyboardInterrupt:
        pass
    finally:
        controller.remove_listener(listener)

if __name__ == '__main__':
    controller()
