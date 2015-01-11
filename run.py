from lollercoaster.generator import ColumnBlock
from lollercoaster.ground import Earth
from colorama import *
import time

# Start colorama
init()

# Setup the column builder
block = ColumnBlock(79, 20)

# Setup the Earth (wow!)
earth = Earth(2, 79)

# Main loop
while True:
    print block.cycle()
    print earth.cycle()
    time.sleep(.33)
