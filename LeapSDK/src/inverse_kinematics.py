# inverse kinematics

# from leap motion we will gather three data points

# position of hand

# angle of arms

import math
import matplotlib.pyplot as plt
import os, sys
sys.path.insert(0, "../lib")
sys.path.insert(0, "../lib/x64")

import Leap, thread


BASE = 121 # mm
MIDDLE = 122 # mm
WRIST = 9.52 # mm

#equations
#https://ocw.mit.edu/courses/mechanical-engineering/2-12-introduction-to-robotics-fall-2005/lecture-notes/chapter4.pdf

def end_effector_position(wrist_position, hand_direction): # z, y are the coordinates of the end effector
									# phi is the angle (in radians) of the end effector with respect to x
	
	phi = math.tan(hand_direction.y/hand_direction.z)

	z = wrist_position.z
	y = wrist_position.y
	
	z_prime = z - WRIST*math.cos(phi)
	y_prime = y - WRIST*math.sin(phi)

	alpha = math.atan2(y_prime,z_prime) # atan2 returns angle between pi and negative pi

	r_squared = z_prime**2 + y_prime**2

	beta = (BASE**2 + MIDDLE**2 - r_squared)/(2*BASE*MIDDLE)

	theta_2 = math.pi - beta

	gamma = math.acos((r_squared + BASE**2 - MIDDLE**2)/(2*math.sqrt(r_squared)*BASE))

	theta_1 = alpha - gamma

	theta_3 = phi - theta_1 - theta_2

	#return str(int(math.degrees(theta_1))) + " " + str(int(math.degrees(theta_2))) + " " + str(int(math.degrees(theta_3)))
	return [int(math.degrees(theta_1)), int(math.degrees(theta_2)), int(math.degrees(theta_3))]

angles_str = end_effector_position(30, 30, math.pi/2)

#theta_1, theta_2, theta_3 = angles_str.split(' ')

print angles_str


