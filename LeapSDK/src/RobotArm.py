
# this file uses tabs instead of spaces
class RobotArm():
	is_claw_open = True
	arm_angle = 45 # ranges from 0 to 90 degrees
	base_rotation_angle = 0 # range from -45 to 45?

	def reset(self):
		is_claw_open = True
		arm_angle = 45 # ranges from 0 to 90 degrees
		base_rotation_angle = 0

	def __init__(self):
		self.reset()

	def update(self, _is_claw_open, _arm_angle, _base_rotation_angle):
		
		is_claw_open = _is_claw_open

		if _arm_angle > 90:
			arm_angle = 90
		elif _arm_angle < 0:
			arm_angle = 0
		else:	
			arm_angle = _arm_angle 

		if _base_rotation_angle > 45:
			base_rotation_agle = 45
		elif _base_rotation_angle < -45:
			base_rotation_agle = -45
		else:
			base_rotation_angle = _base_rotation_angle

