plants_mapping = {'V': 'Violets',
                  'C': 'Clover',
                  'R': 'Radishes',
                  'G': 'Grass'}
class Garden(object):
    default_students = ['Alice', 'Bob', 'Charlie', 'David',
                        'Eve', 'Fred', 'Ginny', 'Harriet',
                        'Ileana', 'Joseph', 'Kincaid', 'Larry']

    def __init__(self, diagram, students=None):
        self.row1, self.row2 = diagram.split('\n')
        if students:
            self.default_students = sorted(students)

    def plants(self, student):
        index = self.default_students.index(student)
        l = []
        l.append(plants_mapping[self.row1[index * 2]])
        l.append(plants_mapping[self.row1[index * 2 + 1]])
        l.append(plants_mapping[self.row2[index * 2]])
        l.append(plants_mapping[self.row2[index * 2 + 1]])
        return l
