#
# Steering
#
# @author Jarrod Risley

# Imports
import os
import serial
from Subsystem import *

class Steering(Subsystem):

	calibrationConstant = 2.547 # ms/deg
	raw = 0.0

	#
	# Constructor
	#
	def __init__(self, motors, sensors, PIDController, isThisSetpoint, initialSensorReading):
		super().__init__(motors, sensors, PIDController, isThisSetpoint, initialSensorReading)

		if (isThisSetpoint):

			# If we are at the setpoint (i.e. middle of the track), we want to stay there.
			print("Getting setpoint for subsystem...")
			time.sleep(0.5)
			setpoint = initialSensorReading
			self._PIDController.setSetpoint(setpoint)
			self._PIDController.setCurrent(setpoint)

	#
	# Methods
	#
	def update(self):

		#self._Subsystem__pollPID()

		#print("PID output is " + str(self._output))

		self._output = self._Subsystem__pollSensors()

		if self._output >= 100 and self._output < 150:
			dutyCycle = 8 #7 - (1/self._output)
		elif self._output >= 50 and self._output < 100: 
			dutyCycle = 7
		elif self._output < 50: 
			dutyCycle = 6
		else:
			dutyCycle = 7

		print("Steering duty cycle has been set to: " + str(dutyCycle))
		self._motors.setTo(dutyCycle)


	def _Subsystem__pollSensors(self):
		# Sensor readings go here.

		lastRaw = self.raw
		self.raw = self._sensors.getSensorReadings(3)

		if self.raw != "":

			print("Max Sonar Sensor: " + self.raw)
			sonar = float(self.raw)

			return sonar * self.calibrationConstant

		elif self.raw == -1:
			return lastRaw * self.calibrationConstant

		else:

			print("Sensor reading undefined: Sensor reads " + self.raw)
			return 0

		# Do sensor math here

		


	def _Subsystem__pollPID(self):

		sensorReading = self._Subsystem__pollSensors()

		self._PIDController.setCurrent(sensorReading)

		self._output = self._PIDController.output()


	def haltMotors(self):
		print("eStop currently not supported")