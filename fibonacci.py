def fibonacci(n):
    a = 0
    b = 1
    for _ in range(n):
        a, b = b, a + b
    return a


param = int(input())
print(fibonacci(param))
