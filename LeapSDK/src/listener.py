from importLeap import pyLeap

class Listener(pyLeap.Listener):
	def on_connect(self, controller):
		print "Connected"
	
	def on_frame(self, controller):
		print "Frame available"
