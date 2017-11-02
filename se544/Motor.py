# Imports
import Adafruit_BBIO.PWM as pwm
import time

class Motor:

	#
	# Global Class Variables
	#
	__freq = 50 # Hz
	_minDuty = 0.0
	_maxDuty = 0.0
	_dutySpan = 0.0
	ESC_NEUTRAL = 7.5
	SERVO_NEUTRAL = 7

	#
	# Constructor
	#
	def __init__(self, pin, minDuty, maxDuty, hasESC):

		self._pin = pin
		self._minDuty = minDuty
		self._maxDuty = maxDuty
		self._dutySpan = maxDuty - minDuty
		
		pwm.start(self._pin, (100 - minDuty), 50)
		

		if (hasESC):

			self.setTo(self.ESC_NEUTRAL) # ESC expects a neutral throttle signal at 1.5 milliseconds - for 50 Hz, that's a duty cycle of 7.5%.
			time.sleep(0.1) # Need this so the ESC can read the signal.

		else:
			self.setTo(self.SERVO_NEUTRAL)




	# end __init__


	#
	# Methods
	#

	def setTo(self, dutyCycle):

		"""Sets the motor to the specified duty cycle."""

		pwm.set_duty_cycle(self._pin, dutyCycle)

	# end set

	def getDutySpan(self):
		return self._dutySpan

	def getDutyMin(self):
		return self._minDuty

	def eStop(self):
		
		"""Immediately shuts off the motor."""

		print("Not defined lol")
