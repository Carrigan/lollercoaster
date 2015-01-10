from lollercoaster.columns import Column, pattern_types
import random


def generate_block(cols, max_height):
    # Create the columns
    height = 10
    columns = []
    for i in range(cols):
        current_type = random.randint(-1, 1)

        if current_type == -1:
            if height == 0:
                current_type = 0
            height += current_type

        if current_type == 1 and height == max_height - 1:
            current_type = 0

        columns.append(Column(height, current_type, max_height))

        if current_type == 1:
            height += current_type

    # Fill as alternating types
    for i, col in enumerate(columns):
        col.fill(pattern_types[i % 3])

    # Fill the rows, starting at the top working down
    rows = [""] * max_height
    for c in range(max_height):
        for col in columns:
            rows[c] += col.retrieve_row(max_height - c - 1)

    # Print the rows
    for row in rows:
        print row
