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
        self.column_type = column_type
        self.height = height
        self.rows[height] = column_dict[column_type]
        self.max_height = max_height

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

    def change_top(self, character):
        self.rows[self.height] = "\x1b[31;1m" + character + "\x1b[0m"

    def revert_top(self):
        self.rows[self.height] = column_dict[self.column_type]