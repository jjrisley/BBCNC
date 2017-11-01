#
# Sensors
#
# @author Jarrod Risely

# Imports
import Adafruit_BBIO.ADC as adc

class MaxSonar:

	#
	# Class Variables
	#
	__pin = ""
	
	def __init__(self, pin):
		self.__pin = pin
		
	#
	# Methods
	#
	
	def getReading(self):
		
		val = 0.0
		average = 0.0
		
		for z in range(10):
			val = adc.read(self.__pin) * 1.26238
			average = average + val
		
		average = average / 10
		
		return average