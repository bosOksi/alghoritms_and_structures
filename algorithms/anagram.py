def calc(list):
    result = []
    for i in range(len(list)):
        element = []
        isSwapped = False
        for l in range(len(list[i])):
            element.append(list[i][l])
        for j in range(len(list[i]) - 1, 0, -1):
            if list[i][j] > list[i][j - 1]:
                element[j] = list[i][j - 1]
                element[j - 1] = list[i][j]
                isSwapped = True
                #отсортировать оставшуюся подстроку. Пример abca -> acab
                element[j:len(element)] = sorted(element[(j):len(element)])
                break
        if isSwapped == False:
            element = sorted(list[i])
        result.append(''.join(element))
    for k in result:
        print(k)


list = []
while True:
    str = input()
    if str:
        list.append(str)
    else:
        break
calc(list)