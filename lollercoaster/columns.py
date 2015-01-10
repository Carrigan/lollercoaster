column_types = {
    "up": "/",
    "flat": "_",
    "down": "\\"
}


class Column(object):
    def __init__(self, height, column_type, max_height):
        if column_type not in column_types:
            raise ValueError()

        self.rows = [" "] * max_height
        self.type = type
        self.height = height
        self.rows[height] = column_types[column_type]

    def retrieve_row(self, row):
        return self.rows[row]
