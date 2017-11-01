#
# Steering
#
# @author Jarrod Risley

# Imports
import os
import serial
from Subsystem import *
from MaxSerial import *

class Steering(Subsystem):

	calibrationConstant = 2.547 # ms/deg
	raw = 0.0
	

	#
	# Constructor
	#
	def __init__(self, motors, sensorNames, PIDController, isThisSetpoint):
		super().__init__(motors, sensorNames, PIDController, isThisSetpoint)

		sonar1 = MaxSerial("AIN0")
		
		if (isThisSetpoint):

			# If we are at the setpoint (i.e. middle of the track), we want to stay there.
			print("Getting setpoint for subsystem...")
			time.sleep(0.5)
			setpoint = sonar1.getReading()
			self._PIDController.setSetpoint(setpoint)
			self._PIDController.setCurrent(setpoint)

	#
	# Methods
	#
	def update(self):

		self._Subsystem__pollPID()

		print("PID output is " + str(self._output))

		print("Steering duty cycle has been set to: " + str(dutyCycle))
		self._motors.setTo(100 - ((self._output / 180) * self._motors.getDutySpan() + self._motors.getDutyMin()))


	def _Subsystem__pollSensors(self):
		# Sensor readings go here.

		lastRaw = self.raw
		self.raw = self.sonar1.getReading()

		print("Max Sonar Sensor: " + self.raw)
		reading = float(self.raw)

		return reading #* self.calibrationConstant


		


	def _Subsystem__pollPID(self):

		sensorReading = self._Subsystem__pollSensors()

		self._PIDController.setCurrent(sensorReading)

		self._output = self._PIDController.output()


	def haltMotors(self):
		print("eStop currently not supported")