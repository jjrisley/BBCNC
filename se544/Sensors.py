#
# Sensors
#
# @author Jarrod Risely

# Imports
import serial

class Sensors:

	#
	# Class Variables
	#
	IR1 = ""
	IR2 = ""
	MS1 = ""
	MS2 = ""
	LI1 = ""
	LI2 = ""

	sensors = [IR1, IR2, MS1, MS2, LI1, LI2]

	def __init__(self):

		self.ser = serial.Serial("/dev/ttyACM0", 9600)

	def updateSensors(self):

		line = str(self.ser.readline().decode())
		line = line.split()

		if "US" in line: #Ultrasonic sensor 
			pass
		elif "MS" in line and "1" in line: #MaxSonar
			self.sensors[2] = line[2]
		elif "MS" in line and "2" in line: #MaxSonar
		 	self.sensors[3] = line[2]
		elif "IR" in line and "1" in line: #IR sensor
			self.sensors[0] = line[2]
		elif "IR" in line and "2" in line: #IR sensor
			self.sensors[1] = line[2]
		elif "LI" in line and "1" in line: #LI sensor
		 	self.sensors[4] = line[2]
		elif "LI" in line and "2" in line: #LI sensor
		 	self.sensors[5] = line[2]

		else:
			print("Error")

	def getSensorReadings(self, index):
		return self.sensors[index]

	def isSerialStillWorking(self):
		return self.ser.isOpen()
