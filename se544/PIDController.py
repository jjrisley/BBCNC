#
# PID Controller
#
# @author Jarrod Risley

import time

class PIDController:

	"""PID controller that adjusts the output level of a system given a sensor reading."""

	#
	# Global Class Variables
	#
	_setpoint = 0.0
	_current = 0.0
	_previousError = 0.0
	_accumulator = 0.0
	_dt = 0.0

	# Constants
	_Kp = 0.0
	_Ki = 0.0
	_Kd = 0.0



	def __init__(self, P, I, D, dt):

		"""Initializes the PID Controller with the given P, I, and D values."""

		self._Kp = P
		self._Ki = I
		self._Kd = D
		self._dt = dt

	# end _init_

	def setSetpoint(self, point):

		"""Setter that sets the setpoint in terms of a raw analog value."""

		self._setpoint = point

	# end setSetpoint

	def setCurrent(self, value):

		"""Setter that sets the error in terms of a raw analog value."""

		self._current = self._setpoint - value

	# end setSetpoint

	def _getErrorFunction(self):
		
		"""This is e(t) in the PID control theory."""

		return (self._setpoint - self._current) 

	# end getErrorFunction

	def _proportionalTerm(self):

		"""The proportional 'P' term in PID."""

		return self._getErrorFunction() * self._Kp

	# end proportionalTerm

	def _integralTerm(self):
		"""The integral 'I' term in PID."""

		self._accumulator = self._accumulator + self._getErrorFunction()

		return self._Ki * self._accumulator * self._dt

	def _derivativeTerm(self):

		"""The derivative 'D' term in PID."""

		return self._Kd * (self._getErrorFunction() - self._previousError) / self._dt

	# end derivativeTerm

	def output(self):

		"""The output of the PIDController, which is the power level the system will output."""

		self._previousError = self._getErrorFunction()
	
		return self._proportionalTerm() + self._derivativeTerm() + self._integralTerm()