#
# Steering
#
# @author Jarrod Risley

# Imports
import os, time
from Subsystem import *
from MaxSonar import *

class Steering(Subsystem):

	calibrationConstant = 2.547 # ms/deg
	raw = 0.0

	#
	# Constructor
	#
	def __init__(self, motors, sensorNames, PIDController, isThisSetpoint):
		super(Steering, self).__init__(motors, sensorNames, PIDController, isThisSetpoint)

		self.sonar1 = MaxSonar(self._sensors[0])
		self.sonar2 = MaxSonar(self._sensors[1])
		
		if (isThisSetpoint):

			# If we are at the setpoint (i.e. middle of the track), we want to stay there.
			print("Getting setpoint for subsystem...")
			time.sleep(0.5)
			self.setpoint = 0.5 * (self.sonar1.getReading() + self.sonar2.getReading())
			self._PIDController.setSetpoint(self.setpoint)
			self._PIDController.setCurrent(self.setpoint)

	#
	# Methods
	#
	def update(self):

		self._Subsystem__pollPID()

		##### THIS IS WHERE YOU PUT THE PID S-CURVE STUFF ######

		print("														PID output is " + str(self._output))
		dutyCycle = ((self._output / self.setpoint) * self._motors.getDutySpan() + self._motors.getDutyMin())
		print("                                                 Steering duty cycle has been set to: " + str(dutyCycle))
		self._motors.setTo(dutyCycle) # If we didn't detect a hard-turn case, replace this line with the s-curve logic.

		# Otherwise execute the hard turn here.


	def _Subsystem__pollSensors(self):
		# Sensor readings go here.
		
		a = self.sonar1.getReading()
		b = self.sonar2.getReading()

		if a / b >= 0.9 or a/b <= 1.1:
			dHat = 0.5 * (self.sonar1.getReading() + self.sonar2.getReading())
		elif a / b > 1.1:
			print("Need to hard turn RIGHT")
			#
			#
			#
			# INCORPORATE FLAG LOGIC HERE 
			#
			#
			#
			return "Some flag thing needs to go here."
		elif a / b < 0.9:
			print("Need to hard turn LEFT")
			#
			#
			#
			# INCORPORATE FLAG LOGIC HERE
			#
			#
			#
			return "Some flag thing needs to go here."
		print("Average distance to wall: " + str(dHat))

		return dHat


		


	def _Subsystem__pollPID(self):

		sensorReading = self._Subsystem__pollSensors()


		#
		# Incorporate flag logic for hard turning here.
		#

		# Only go to the PID controller if we are in the case where a ~ b
		self._PIDController.setCurrent(sensorReading)

		self._output = self._PIDController.output()


	def haltMotors(self):
		print("eStop currently not supported")
