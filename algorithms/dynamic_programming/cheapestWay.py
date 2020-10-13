# считываем размер матрицы и ее строки
n, m = [int(i) for i in input().split()]
array = []
for i in range(n):
    row = input().split()
    for j in range(m):
        row[j] = int(row[j])
    array.append(row)
for i in range(n):
    for j in range(m):
        if i > 0 and j > 0:
            array[i][j] += min(array[i-1][j], array[i][j-1])
        else:
            if i > 0:
                array[i][j] += array[i - 1][j]
            elif j > 0:
                array[i][j] += array[i][j - 1]
print(array[n - 1][m - 1])
