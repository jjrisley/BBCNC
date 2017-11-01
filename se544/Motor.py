# Imports
import RPi.GPIO as io
import time

class Motor:

	#
	# Global Class Variables
	#
	__freq = 50 # Hz
	ESC_NEUTRAL = 7.5
	SERVO_NEUTRAL = 7

	#
	# Constructor
	#
	def __init__(self, pin, hasESC):

		self.__pin = pin
		
		io.setup(self.__pin, io.OUT)
		self.__pwm = io.PWM(self.__pin, self.__freq)
		self.__pwm.start(self.__freq)
		self.__pwm.ChangeFrequency(self.__freq)

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

		self.__pwm.ChangeDutyCycle(dutyCycle)

	# end set

	def eStop(self):
		
		"""Immediately shuts off the motor."""

		self.__pwm.stop()
