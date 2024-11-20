matrix = [[1, 2, 3], [4, 5, 6]]
dict_matrix = {i: {j: value for j, value in enumerate(row)} for i, row in enumerate(matrix)}
print(dict_matrix)
