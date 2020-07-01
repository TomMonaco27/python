class Matrix:
    def __init__(self, list_of_lists):
        self.list_of_lists = list_of_lists
        self.final = [[0 for i in range(len(self.list_of_lists[0]))] for j in range(len(self.list_of_lists))]

    def __str__(self):
        return '\n'.join('\t'.join(map(str, row)) for row in self.list_of_lists)

    def __add__(self, other):
#        other = Matrix(other)
#        sum_el = 0
        sum_matrix = []
        final = []
        for i in range(len(self.list_of_lists)):
            for j in range(len(self.list_of_lists[i])):
                self.final[i][j] = self.list_of_lists[i][j] + other.list_of_lists[i][j]
                print(f'self.final = {self.final}')
        return self.final
#        return Matrix(self.sum_matrix[i][j] + other.sum_matrix[i][j])


my_matrix_1 = Matrix([[1, 2], [1, 2], [1, 2]])
my_matrix_2 = Matrix([[1, 2], [1, 2], [1, 2]])
print(my_matrix_1)
print()
print(my_matrix_2)
print()
mat = my_matrix_1 + my_matrix_2
print(mat)
