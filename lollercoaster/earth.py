import random

grass_tiles = [",", ";", "\"", "`", " "]


class Earth(object):
    """
    An object to hold the state data for the ground underneath the lollercoaster.
    This object can be drawn by printing it to stdout.
    """
    def __init__(self, depth, length):
        self.rows = []
        for i in xrange(depth):
            self.rows.append("".join([random.choice(grass_tiles) for x in range(length)]))

    def __repr__(self):
        return "\x1b[32m" + "\n".join(self.rows) + "\x1b[0m"

    def advance(self):
        """
        Advance the state of the earth by one column.

        :return: A reference to self for direct drawing.
        """
        for i, row in enumerate(self.rows):
            self.rows[i] = row[1:] + random.choice(grass_tiles)

        return self
