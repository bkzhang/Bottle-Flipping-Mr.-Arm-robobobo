# inverse kinematics

# from leap motion we will gather three data points

# position of hand

# angle of arms
import csv
import math
import os, sys
sys.path.insert(0, "../lib")
sys.path.insert(0, "../lib/x64")

import Leap, thread


BASE = 121 # mm
MIDDLE = 122 # mm
WRIST = 9.52 # mm

#equations
#https://ocw.mit.edu/courses/mechanical-engineering/2-12-introduction-to-robotics-fall-2005/lecture-notes/chapter4.pdf

DEBUG = 1
def end_effector_position(wrist_position, hand_direction): # z, y are the coordinates of the end effector
									# phi is the angle (in radians) of the end effector with respect to x
	#if wrist_position == None or hand_direction == None:
	#	return None

	phi = math.tan(hand_direction.y/-hand_direction.z)

	z = -wrist_position.z
	y = wrist_position.y
	
	z_prime = z - WRIST*math.cos(phi)
	y_prime = y - WRIST*math.sin(phi)

	alpha = math.atan2(y_prime,z_prime) # atan2 returns angle between pi and negative pi

	r_squared = z_prime**2 + y_prime**2

	beta = math.acos((BASE**2 + MIDDLE**2 - r_squared)/(2*BASE*MIDDLE))

	theta_2 = math.pi - beta
	
	gamma = math.acos((r_squared + BASE**2 - MIDDLE**2)/(2*math.sqrt(r_squared)*BASE))

	theta_1 = alpha - gamma

	theta_3 = phi - theta_1 - theta_2

	theta_1 = int(math.degrees(theta_1))
	theta_2 = int(math.degrees(theta_2))
	theta_3 = int(math.degrees(theta_3))

	l = (MIDDLE*math.sin(beta))/math.sin(theta_1 - alpha)
	x = [BASE*math.cos(theta_1), l*math.cos(alpha), z]
	y = [BASE*math.sin(theta_1), l*math.sin(alpha), y]
	print('x:', x)
	print('y:', y)
	
	#x = str(x).strip("[]\"")
	#y = str(y).strip("[]\"")
	#data = [x, y]
	xy = x + y

	with open('data.csv', 'a') as csvfile:
		writer = csv.writer(csvfile, delimiter=',')
		writer.writerow(xy)	

	if DEBUG == 1:
		print("r_squared: ", r_squared)
		print("BASE: ", BASE)
		print("phi (degrees): ", int(math.degrees(phi)))
                print("alpha (degrees): ", int(math.degrees(alpha)))
                print("hand_direction.z: ", hand_direction.z)
                print("hand_direction.y: ", hand_direction.y)

	print("theta_1: ", theta_1)
	print("theta_2: ", theta_2)
	print("theta_3: ", theta_3)

	return [theta_1, theta_2, theta_3]


