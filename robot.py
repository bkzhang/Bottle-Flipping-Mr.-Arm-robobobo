import os, sys
import Leap
from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture

src_dir = os.path.dirname(inspect.getfile(inspect.currentframe()))
sys.path.insert(0, os.path.abspath(os.path.join(src_dir, '../lib')))
sys.path.insert(0, os.path.abspath(os.path.join(src_dir, '../lib/x64')))

class Listener(Leap.Listener):
    def on_connect(self, controller):
        print "Connected"
    
    def on_frame(self, controller):
        print "Frame available"

def controller():
    listener = Listener()
    controller = Leap.Controller()

    controller.add_listener(listener)

    print "Press any key to quit"
    try:
        sys.stdin.readline()
    except KeyboardInterrupt:
        pass
    finally:
        contoller.remove_listener(listener)

if __name__ == '__main__':
    connect()
