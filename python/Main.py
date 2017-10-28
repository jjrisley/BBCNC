#
# Main
#
# @author Jarrod Risley
#
# The main loop for the entire program.
#

#
# Imports
#
import Adafruit_BBIO.GPIO as io
import time

pin = "P8_26"

io.setup(pin, io.OUT)

while True:
    io.output(pin, io.HIGH)
    time.sleep(0.5)
    io.output(pin, io.LOW)
    time.sleep(0.5)