n = int(input())
arr1 = [int(i) for i in input().split()]
m = int(input())
arr2 = [int(i) for i in input().split()]
F = [[0] * (m + 1) for i in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if arr1[i - 1] == arr2[j - 1]:
            F[i][j] = F[i - 1][j - 1] + 1
        else:
            F[i][j] = max(F[i - 1][j], F[i][j - 1])
print(F[n][m])
