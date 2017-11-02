# Import statements go here.
import Adafruit_BBIO.ADC as adc
import Adafruit_BBIO.PWM as pwm
import time, traceback
from Motor import *
from Drive import *
from Steering import *
from PIDController import *

# This needs to be here.

#
# Global Script Variables
#
corgi = True
freq = 5
tb = "" # Traceback for any errors we encounter




# Main loopy thing

try:

	adc.setup()
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
	raw_input("Press 'Enter' to let Ein loose...")

	# Instantiate subsystems here.
	#mainDrive = Drive(Motor(12, True), sensors, PIDController(0, 0, 0, 1), False)
	steering = Steering(Motor("P8_13", 5, 10, False), ["AIN0", "AIN1"], PIDController(1, 0, 0, 0.05), True)

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
	pwm.cleanup()

# end while
