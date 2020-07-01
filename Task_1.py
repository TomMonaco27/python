class Matrix:
    def __init__(self, list_of_lists):
#        self.list_of_lists = [[]]
        self.list_of_lists = list_of_lists

    def __str__(self):
        return '\n'.join('\t'.join(map(str, row)) for row in self.list_of_lists)

    def __add__(self, other):
        other = Matrix(other)
#        sum_el = 0
        sum_matrix = []
        final = []
        for i in range(len(self.list_of_lists)):
            for j in range(len(self.list_of_lists[0])):
                sum_el = self.list_of_lists[i][j] + other[i][j]
                sum_matrix.append(sum_el)
                print(sum_el)
                if len(sum_matrix) == len(self.list_of_lists):
                    final.append(sum_matrix)
                    sum_matrix = []
        return Matrix(final)
#        return Matrix(self.sum_matrix[i][j] + other.sum_matrix[i][j])


my_matrix_1 = Matrix([[1, 2], [3, 4], [5, 6]])
my_matrix_2 = Matrix([[7, 8], [9, 10], [11, 12]])
print(my_matrix_1)
print()
print(my_matrix_2)

#print(my_matrix_1 + my_matrix_2)
