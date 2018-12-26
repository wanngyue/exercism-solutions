import bisect

plants_mapping = {'V': 'Violets',
                  'C': 'Clover',
                  'R': 'Radishes',
                  'G': 'Grass'}


class Garden(object):
    students = ['Alice', 'Bob', 'Charlie', 'David',
                'Eve', 'Fred', 'Ginny', 'Harriet',
                'Ileana', 'Joseph', 'Kincaid', 'Larry']

    def __init__(self, diagram, students=None):
        self.rows = diagram.split('\n')
        if students:
            self.students = sorted(students)

    def plants(self, student):
        index = bisect.bisect_left(self.students, student) * 2
        initials = ''.join(row[index:index + 2] for row in self.rows)
        return [plants_mapping[initial] for initial in initials]
