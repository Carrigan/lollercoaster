from lollercoaster.columns import Column


def generate_block(cols, max_height):
    columns = [Column(10, "flat", max_height) for c in xrange(cols)]
    rows = [""] * max_height
    for c in range(cols):
        for col in columns:
            rows[c] += col.retrieve_row(c)

    for row in rows:
        print row
