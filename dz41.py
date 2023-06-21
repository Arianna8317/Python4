# Напишите функцию для транспонирования матрицы

matrix = [[1, 2, 23, 5], [14, 5, 16, 9], [7, 8, 9, 16], [2, 3, 5, 6]]


def transpose(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    if rows == cols:
        result_matrix = []
        for j in range(cols):
            row_j = []
            for i in range(rows):
                row_j.append(matrix[i][j])
            result_matrix.append(row_j)
        return result_matrix
    else:
        return None


def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(f"{matrix[i][j]:>3}", end="")
        print()    


print("Исходная матрица :")
print_matrix(matrix)
transp = transpose(matrix)
if isinstance(transp, list):    
    print("Транспонированная матрица :")
    print_matrix(transp)
else:
    print("Матрицу нельзя транспонировать!")
