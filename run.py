#!/usr/bin/python
from lollercoaster.generator import LollerCoaster
from lollercoaster.earth import Earth
from colorama import *
import time

# Start colorama
init()

# Setup the column builder
block = LollerCoaster(79, 20)

# Setup the Earth (wow!)
earth = Earth(2, 79)

# Main loop
while True:
    print block.advance()
    print earth.advance()
    time.sleep(.33)
