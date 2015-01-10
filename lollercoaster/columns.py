column_dict = {
    1: "/",
    0: "_",
    -1: "\\"
}

pattern_types = [
    "col",
    "in",
    "out",
]

class Column(object):
    def __init__(self, height, column_type, max_height):
        if column_type not in column_dict:
            raise ValueError()

        self.rows = [" "] * max_height
        self.type = type
        self.height = height
        self.rows[height] = column_dict[column_type]

    def retrieve_row(self, row):
        return self.rows[row]

    def fill(self, pattern):
        if pattern not in pattern_types:
            raise ValueError()

        for i in range(len(self.rows[:self.height])):
            if pattern == "col":
                self.rows[i] = "|"
            elif pattern == "in":
                if i & 1:
                    self.rows[i] = "/"
                else:
                    self.rows[i] = "\\"
            elif pattern == "out":
                if i & 1:
                    self.rows[i] = "\\"
                else:
                    self.rows[i] = "/"
