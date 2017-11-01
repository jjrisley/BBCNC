# Import statements go here.
import RPi.GPIO as io
import time, traceback
from Motor import *
from Drive import *
from Steering import *
from PIDController import *

# This needs to be here.
io.setmode(io.BOARD)

#
# Global Script Variables
#
corgi = True
freq = 5
tb = "" # Traceback for any errors we encounter




# Main loopy thing

try:


	#print("Initiallizing main drive motors...")
	#motor = Motor(18, corgi)

	#print("FORWARD!")
	#motor.setTo(5)
	#time.sleep(3)
	#print("Neutral")
	#motor.setTo(7.5)
	#time.sleep(3)
	#print("REVERSE!")
	#motor.setTo(10)
	#time.sleep(3)
	#print("Neutral")
	#motor.setTo(7.5)

	# Check for user in put to start running the program
	input("Press 'Enter' to let Ein loose...")

	# Instantiate subsystems here.
	#mainDrive = Drive(Motor(12, True), sensors, PIDController(0, 0, 0, 1), False)
	steering = Steering(Motor("P8_13", 5, 10, False), sensors, PIDController(0.075, 0, 0, 0.05), True)

	while (corgi):

		#mainDrive.update()
		steering.update()


except:
	tb = traceback.format_exc()

else:
	tb = "Program ran without error."

finally:

	print(tb)
	print("Ein is stopping...")
	io.cleanup()

# end while
