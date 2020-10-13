# считываем размер матрицы и ее строки
n, m = [int(i) for i in input().split()]
array = []
for i in range(n):
    row = input().split()
    for j in range(m):
        row[j] = int(row[j])
    array.append(row)
result = [n][m]
for i in range(n):
    for j in range(m):
        if i > 0 & j > 0:
            array[i][j]
