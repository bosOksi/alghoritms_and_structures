def calc(list):
    return(int(len(list)/2))


list = input().split()
del list[len(list) - 1]
print(calc(list))