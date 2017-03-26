import os, sys
sys.path.insert(0, "../lib")
sys.path.insert(0, "../lib/x64")

import Leap, thread, time
from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture

PRINT = 0

class LeapListener(Leap.Listener):
    finger_names = ['Thumb', 'Index', 'Middle', 'Ring', 'Pinky']
    bone_names = ['Metacarpal', 'Proximal', 'Intermediate', 'Distal']
    state_names = ['STATE_INVALID', 'STATE_START', 'STATE_UPDATE', 'STATE_END'] 
    def on_init(self, controller):
        print "Initialized"

    def on_connect(self, controller):
        print "Connected"
        # Enable gestures
        controller.enable_gesture(Leap.Gesture.TYPE_CIRCLE);
        controller.enable_gesture(Leap.Gesture.TYPE_KEY_TAP);
        controller.enable_gesture(Leap.Gesture.TYPE_SCREEN_TAP);
        controller.enable_gesture(Leap.Gesture.TYPE_SWIPE);

    def on_disconnect(self, controller):
        # Note: not dispatched when running in a debugger.
        print "Disconnected"

    def on_exit(self, controller):
        print "Exited"

    # For some reason the axis are reversed?
    
    def is_fist(self, hand):
        for finger in hand.fingers: # skip the thumb
            if self.finger_names[finger.type] == "Thumb": # skip thumb
                thumb_distal = finger.bone(3)
                if thumb_distal.direction.x < 0:
                    #print("Right thumb is pointing right")
                    print("");
                else:
                    #print("Right thumb is pointing left")
                    return False
            else:
                distal = finger.bone(3) # distal is the tip bone
                #print(distal.direction)
                if distal.direction.z < 0:
                    #print("finger is pointing towards user")
                    print("");
                else:
                    #print("finger is pointing away from user")
                    return False
        print("Fist detected")
        return True # Hand is making a fist


    def on_frame(self, controller):
        # Get the most recent frame and report some basic information
        frame = controller.frame()

        if 0:
            print "Frame id: %d, timestamp: %d, hands: %d, fingers: %d, tools: %d, gestures: %d" % (frame.id, frame.timestamp, len(frame.hands), len(frame.fingers), len(frame.tools), len(frame.gestures()))

        # Get hands
        for hand in frame.hands:

            if hand.is_left:
                break

            #print "Right palm position: %s" % (hand.palm_position)

            # Get the hand's normal vector and direction
            normal = hand.palm_normal
            direction = hand.direction

            self.is_fist(hand)

            # Send the pitch of the hand to the arduino
            if 0:
            # Calculate the hand's pitch, roll, and yaw angles
                print "  pitch: %f degrees, roll: %f degrees, yaw: %f degrees" % (direction.pitch * Leap.RAD_TO_DEG, normal.roll * Leap.RAD_TO_DEG, direction.yaw * Leap.RAD_TO_DEG)

            # Send the direction of the arm to the arduino
            # Get arm bone
            arm = hand.arm
            if 0:
                print "  Arm direction: %s, wrist position: %s, elbow position: %s" % (
                    arm.direction,
                    arm.wrist_position,
                    arm.elbow_position)

            # Get fingers
            for finger in hand.fingers:
                if 0:
                    print "    %s finger, id: %d, length: %fmm, width: %fmm" % (
                        self.finger_names[finger.type],
                        finger.id,
                        finger.length,
                        finger.width)

                # Get bones
                
                for b in range(0, 4):
                    bone = finger.bone(b)
                    if 0:
                        print "      Bone: %s, start: %s, end: %s, direction: %s" % (
                            self.bone_names[bone.type],
                            bone.prev_joint,
                            bone.next_joint,
                            bone.direction)
		# Check the distal bone for each finger
		# If the direction of the bone is towards the user (in the positive z direction)
		# Then it's likely that it's a closed fist

        # Get tools
        #for tool in frame.tools:
        #    print "  Tool id: %d, position: %s, direction: %s" % (
        #        tool.id, tool.tip_position, tool.direction)

        # Get gestures
        for gesture in frame.gestures():
            if gesture.type == Leap.Gesture.TYPE_CIRCLE:
                circle = CircleGesture(gesture)

                # Determine clock direction using the angle between the pointable and the circle normal
                if circle.pointable.direction.angle_to(circle.normal) <= Leap.PI/2:
                    clockwiseness = "clockwise"
                else:
                    clockwiseness = "counterclockwise"

                # Calculate the angle swept since the last frame
                swept_angle = 0
                if circle.state != Leap.Gesture.STATE_START:
                    previous_update = CircleGesture(controller.frame(1).gesture(circle.id))
                    swept_angle =  (circle.progress - previous_update.progress) * 2 * Leap.PI

                print "  Circle id: %d, %s, progress: %f, radius: %f, angle: %f degrees, %s" % (
                        gesture.id, self.state_names[gesture.state],
                        circle.progress, circle.radius, swept_angle * Leap.RAD_TO_DEG, clockwiseness)

            if gesture.type == Leap.Gesture.TYPE_SWIPE:
                swipe = SwipeGesture(gesture)
                print "  Swipe id: %d, state: %s, position: %s, direction: %s, speed: %f" % (
                        gesture.id, self.state_names[gesture.state],
                        swipe.position, swipe.direction, swipe.speed)

            if gesture.type == Leap.Gesture.TYPE_KEY_TAP:
                keytap = KeyTapGesture(gesture)
                print "  Key Tap id: %d, %s, position: %s, direction: %s" % (
                        gesture.id, self.state_names[gesture.state],
                        keytap.position, keytap.direction )

            if gesture.type == Leap.Gesture.TYPE_SCREEN_TAP:
                screentap = ScreenTapGesture(gesture)
                print "  Screen Tap id: %d, %s, position: %s, direction: %s" % (
                        gesture.id, self.state_names[gesture.state],
                        screentap.position, screentap.direction )

        if not (frame.hands.is_empty and frame.gestures().is_empty):
            print ""

    def state_string(self, state):
        if state == Leap.Gesture.STATE_START:
            return "STATE_START"

        if state == Leap.Gesture.STATE_UPDATE:
            return "STATE_UPDATE"

        if state == Leap.Gesture.STATE_STOP:
            return "STATE_STOP"

        if state == Leap.Gesture.STATE_INVALID:
            return "STATE_INVALID"

