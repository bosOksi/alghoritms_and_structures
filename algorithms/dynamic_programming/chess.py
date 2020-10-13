n, m = [int(i) for i in input().split()]
array = [[0]*(m + 1) for i in range(n + 1)]
array[1][1] = 1
for i in range(2, n + 1):
    for j in range(2, m + 1):
        array[i][j] = array[i - 1][j - 2] + array[i - 2][j - 1]
print(array[n][m])
