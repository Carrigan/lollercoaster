#!/usr/bin/python
from lollercoaster.generator import LollerCoaster
from lollercoaster.earth import Earth
from colorama import *
import time
import signal
import sys
# Start colorama
init()

# Setup the column builder
block = LollerCoaster(79, 20)

# Setup the Earth (wow!)
earth = Earth(2, 79)
#Handle the Control-C signal gracefully
runAnimation = True
def signal_handler(signal, frame):
	runAnimation = False
	sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)
# Main loop
while runAnimation:
    print block.advance()
    print earth.advance()
    time.sleep(.33)
