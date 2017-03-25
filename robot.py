import os, sys

src_dir = os.path.dirname(inspect.getfile(inspect.currentframe()))
sys.path.insert(0, os.path.abspath(os.path.join(src_dir, '../lib')))
sys.path.insert(0, os.path.abspath(os.path.join(src_dir, '../lib/x64')))

import Leap

def controller():
    controller = Leap.Controller()

    print "Press any key to quit"
    try:
        sys.stdin.readline()
    except KeyboardInterrupt:
        pass

if __name__ == '__main__':
    connect()
