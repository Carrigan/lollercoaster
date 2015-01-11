from lollercoaster.columns import Column, pattern_types
import random


class ColumnBuilder(object):
    """
    This class holds the state machine for generating columns of the lollercoaster
    based on previous columns. Current implementation is a simple state based machine,
    but it could easily be migrated to a markov chain or other type. This machine
    keeps only the last column in memory along with a count of how many columns in a row
    have been in the same direction, meaning it is the task of another class to save
    the window being viewed.
    """

    def __init__(self, max_height):
        self.x = 0
        self.max_height = max_height
        self.last_column = None
        self.direction_count = 0

    def create_initial_column(self):
        """
        Randomly generates the first column so that the create_next_column
        function has an initial state to generate future columns.

        :return: The newly created column object.
        """
        self.x = 0
        initial_height = random.randint(0, self.max_height - 1)
        current_type = random.randint(-1, 1)
        self.last_column = Column(initial_height, current_type, self.max_height)
        self.last_column.fill(pattern_types[self.x % 3])
        self.direction_count += 1
        return self.last_column

    def create_next_column(self):
        """
        Generate a single column of the rollercoaster based on previous columns.
        This is a simple state based machine that is meant to mimic a real
        rollercoaster layout.

        :return: The newly created column object.
        """
        self.x += 1
        height = self.last_column.height
        last_type = self.last_column.column_type

        # If the last one was going up, this one's height will be increased
        if last_type == 1:
            height += 1

        # If we have been going up or down long enough, give it 50/50 to continue or flatten out
        current_type = None
        if self.direction_count < 2:
            current_type = last_type
        else:
            if last_type != 0:
                current_type = last_type if random.choice([True, False]) else 0
            else:
                current_type = current_type = random.randint(-1, 1)

        # Range check lower
        if current_type == -1:
            if height == 0:
                current_type = 0
            height += current_type

        # Range check upper
        if current_type == 1 and height == self.max_height - 2:
            current_type = 0

        # After all that, if the direction changed, reset the count
        if current_type != last_type:
            self.direction_count = 0
        else:
            self.direction_count += 1

        self.last_column = Column(height, current_type, self.max_height)
        self.last_column.fill(pattern_types[self.x % 3])
        return self.last_column


class LollerCoaster(object):
    """
    The LollerCoaster object holds the current window filled with columns
    and is responsible for drawing the coaster itself on top of these
    columns. Print this object will output the current window to stdout.
    """

    def __init__(self, column_count, max_height, coaster_text="ROFLOLOLOL"):
        self.column_count = column_count
        self.builder = ColumnBuilder(max_height)
        self.max_height = max_height
        self.coaster_text = coaster_text

        self.columns = [self.builder.create_initial_column()]
        for count in xrange(1, self.column_count):
            self.columns.append(self.builder.create_next_column())

        self._draw_cart()

    def __repr__(self):
        # Fill the rows, starting at the top working down
        output = ""
        for c in range(self.max_height):
            for col in self.columns:
                output += col.retrieve_row(self.max_height - c - 1)
            output += "\n"

        return output

    def advance(self):
        """
        Advance the lollercoaster one column.

        :return: Returns a copy of itself for printing to stdout.
        """
        self.columns = self.columns[1:]
        self.columns.append(self.builder.create_next_column())
        self._draw_cart()
        return self

    def _draw_cart(self):
        """
        Draw the lollercoaster on top of the columns. The representation of the
        coaster can be changed using the coaster_text argument of the init function.

        :return:
        """
        for col in self.columns:
            col.revert_top()

        for i, c in enumerate(self.coaster_text):
            self.columns[i + 30].change_top(c)
