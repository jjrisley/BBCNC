# Imports
import os
import serial
from Subsystem import *
from Sensors import *

class Drive(Subsystem):

	bork = 7.5

	#
	# Constructor
	#
	def __init__(self, motors, sensors, PIDController, isThisSetpoint, initialSensorReading):
		super().__init__(motors, sensors, PIDController, isThisSetpoint, initialSensorReading)
		

	#
	# Methods
	#
	def update(self):

		self._Subsystem__pollPID()
		self._motors.setTo(self.bork)


	def _Subsystem__pollSensors(self):
		# Sensor readings go here.

		raw = self._sensors.getSensorReadings(0)

		if raw != "":

			print("IR Sensor: " + raw)
			ir = float(raw)

			if ir < 30: # if the IR sensor on the front is reading less than 30 cm...
				self.bork = 7.5
			else:
				self.bork = 6.5


			return ir

		else:

			print("Sensor reading undefined: Sensor reads " + raw)
			return 0

		# Do sensor math here

		


	def _Subsystem__pollPID(self):

		sensorReading = self._Subsystem__pollSensors()

		self._PIDController.setCurrent(sensorReading)

		self._output = self._PIDController.output()


	def haltMotors(self):
		print("--------- EMERGENCY STOP DETECTED ---------")
		self._motors.eStop()

