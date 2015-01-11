import random

grass_tiles = [",", ";", "\"", "`", " "]


def generate_earth(depth, length):
    for row in xrange(depth):
        print "".join([random.choice(grass_tiles) for x in range(length)])
