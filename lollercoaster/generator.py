from lollercoaster.columns import Column, pattern_types

def generate_block(cols, max_height):
    columns = [Column(10, "flat", max_height) for c in xrange(cols)]
    rows = [""] * max_height

    # Fill as alternating types
    for i, col in enumerate(columns):
        col.fill(pattern_types[i % 3])

    # Fill the rows, starting at the top working down
    for c in range(max_height):
        for col in columns:
            rows[c] += col.retrieve_row(max_height - c - 1)

    # Print the rows
    for row in rows:
        print row
