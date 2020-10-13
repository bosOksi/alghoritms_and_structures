def calc(n):
    list = [0, 0]
    for i in range(2, n + 1):
        a = list[i - 1] + 1
        if i % 2 == 0:
            a = min(list[i // 2] + 1, a)
        if i % 3 == 0:
            a = min(list[i // 3] + 1, a)
        list.append(a)
    return list[n]


param = int(input())
print(calc(param))
