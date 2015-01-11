from lollercoaster.generator import ColumnBlock
from colorama import *
import time

# Start colorama
init()

# Setup the column builder
block = ColumnBlock(79, 20)

# Main loop
while True:
    print("\x1b2J")
    print block

    block.cycle()
    time.sleep(.1)
