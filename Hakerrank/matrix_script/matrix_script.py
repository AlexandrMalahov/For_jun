import re


first_multiple_input = input('Введите количество и строк и столбцов матрицы: ').split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []
matrix_list = []
new_matrix = []
for _ in range(n):
    matrix_item = input('Введите текст для расшифровки: ')
    matrix.append(matrix_item)

for x in zip(*matrix):
    matrix_list.append(x)

for tup in matrix_list:
    new_matrix.append(''.join(tup))

text = ''.join(new_matrix)
# Hakerrank не принимает решение с таким regex, хотя он убирает все ненужные символы из строки.
# Правильный regex: (?<=\w)([^\w]+)(?=\w)
text = re.sub(r'[#$&%*]', ' ', text)
print(text)
