import os, sys, inspect

src_dir = os.path.dirname(inspect.getfile(inspect.currentframe()))
sys.path.insert(0, os.path.abspath(os.path.join(src_dir, '../lib')))
sys.path.insert(0, os.path.abspath(os.path.join(src_dir, '../lib/x64')))

import Leap
from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture

pyLeap = Leap
