import sys
from leapMotion import importLeap, leapListener

def controller():
    listener = leapListener.Listener()
    controller = importLeap.pyLeap.Controller()

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
