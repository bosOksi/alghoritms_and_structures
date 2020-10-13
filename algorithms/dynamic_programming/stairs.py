def stairs(n):
    list = [0, 1, 2, 4]
    for i in range(4, n + 1):
        ai = list[i-3] + list[i-2] + list[i-1]
        list.append(ai)
    return list[n]


param = int(input())
print(stairs(param))
