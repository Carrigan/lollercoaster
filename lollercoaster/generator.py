from lollercoaster.columns import Column, pattern_types
import random


class ColumnBuilder(object):
    def __init__(self, max_height):
        self.x = 0
        self.max_height = max_height
        self.last_column = None

    def create_initial_column(self):
        self.x = 0
        initial_height = random.randint(0, self.max_height)
        current_type = random.randint(-1, 1)
        self.last_column = Column(initial_height, current_type, self.max_height)
        self.last_column.fill(pattern_types[self.x % 3])
        return self.last_column

    def create_next_column(self):
        self.x += 1
        height = self.last_column.height
        last_type = self.last_column.column_type

        if last_type == 1:
            height += 1

        current_type = random.randint(-1, 1)

        if current_type == -1:
            if height == 0:
                current_type = 0
            height += current_type

        if current_type == 1 and height == self.max_height - 1:
            current_type = 0

        self.last_column = Column(height, current_type, self.max_height)
        self.last_column.fill(pattern_types[self.x % 3])
        return self.last_column


def generate_block(cols, max_height):
    # Create the column builder object
    builder = ColumnBuilder(max_height)

    # Create a column array and fill it with the initial window
    columns = [builder.create_initial_column()]
    for count in xrange(1, cols):
        columns.append(builder.create_next_column())

    # Fill the rows, starting at the top working down
    rows = [""] * max_height
    for c in range(max_height):
        for col in columns:
            rows[c] += col.retrieve_row(max_height - c - 1)

    # Print the rows
    for row in rows:
        print row
