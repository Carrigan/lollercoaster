import random

grass_tiles = [",", ";", "\"", "`", " "]


class Earth(object):
    def __init__(self, depth, length):
        self.rows = []
        for i in xrange(depth):
            self.rows.append("".join([random.choice(grass_tiles) for x in range(length)]))

    def __repr__(self):
        return "\x1b[32m" + "\n".join(self.rows) + "\x1b[0m"

    def cycle(self):
        for i, row in enumerate(self.rows):
            self.rows[i] = row[1:] + random.choice(grass_tiles)
        return self
