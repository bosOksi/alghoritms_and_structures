def stairs(n):
    list = [0, 2, 3]
    for i in range(3, n + 1):
        ai = list[i-2] + list[i-1]
        list.append(ai)
    return list[n]


param = int(input())
print(stairs(param))
