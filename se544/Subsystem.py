#
# Subsystem
#
# @author Jarrod Risley

# Imports
from abc import ABCMeta

class Subsystem:
	
	__metaclass__ = ABCMeta
	#
	# Global Class Variables
	#
	_kp = 0.0
	_ki = 0.0
	_kd = 0.0
	_output = 0.0
	_setpoint = 0.0
	_sensors = []

	#
	# Constructor
	#
	def __init__(self, motors, sensorNames, PIDController, isThisSetpoint):

		self._motors = motors
		self._sensors = sensorNames
		self._PIDController = PIDController
		
		# Grab an initial reading for the sensors.

		"""if (isThisSetpoint):

			# If we are at the setpoint (i.e. middle of the track), we want to stay there.
			print("Getting setpoint for subsystem...")
			time.sleep(0.5)
			setpoint = self.__pollSensors()
			self._PIDController.setSetpoint(setpoint)
			self._PIDController.setCurrent(setpoint)

		else:

			# Otherwise, we are not at our setpoint - we have a predetermined error in the beginning.
			reading = self.__pollSensors()
			self._PIDController.setCurrent(reading)
			self._PIDController.setSetpoint(endCondition)
			"""
		



	# end __init__

	#
	# Methods
	#

	def update(self):
		"""Updates the subsystem to the current conditions following a call from an ISR"""

	def __pollSensors(self):
		"""Polls all available sensors on this subsystem."""

	def __pollPID(self):
		"""Polls the PID subsystem."""

	def haltMotors(self):
		"""Sends an emergency stop command to the sybsystem's motors."""
