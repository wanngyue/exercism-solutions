class Matrix(object):
    def __init__(self, matrix_string):
        self.rows = []
        for row in matrix_string.split('\n'):
            self.rows.append([int(num) for num in row.split()])

    def row(self, index):
        return self.rows[index]

    def column(self, index):
        return [row[index] for row in self.rows]
