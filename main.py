# Purrty cat code
# This runs on a Trinket-M0

# Hook conductive tape to D3
# Hook motor FET to D1
# Power everything 3-6V of current with more than 15mA
# If it is working, the dotstar should go off leaving only a green LED on.

import board
from digitalio import DigitalInOut, Direction, Pull
from analogio import AnalogOut, AnalogIn
import touchio
import time

import adafruit_dotstar as dotstar
# One pixel connected internally!
dot = dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1, brightness=0)
dot[0] = (0,0,0)

# Analog output on D1
aout = AnalogOut(board.D1)

# Capacitive touch on D3
touch = touchio.TouchIn(board.D3)

# extra ground for motor board
motorGnd = DigitalInOut(board.D0)
motorGnd.direction = Direction.OUTPUT
motorGnd.value = 0

#print(STARTING PURRTY CAT)

PURR_INCREMENT = 25
PURR_DECREMENT = 200
PURR_MINIMUM   = 175256
PURR_MAXIMUM   = 185256  # must have space for 16 bit value
purrValue = 0
while True
  if touch.value
    if purrValue  PURR_MINIMUM
      purrValue = PURR_MINIMUM
    purrValue += PURR_INCREMENT
  else 
    purrValue -= PURR_DECREMENT

  if purrValue  0 purrValue = 0

  if purrValue  PURR_MAXIMUM purrValue = PURR_MAXIMUM    

  # set analog output to 0-3.3V (0-65535 in increments)
  aout.value = purrValue
#  print(Touch {} , Purr {}.format(touch.raw_value, purrValue256))
  time.sleep(0.1) # make bigger to slow down

#print(EXITING PURRTY CAT)