def calc_with_answers(n):
    list = [0, 0]
    for i in range(2, n + 1):
        a = list[i - 1] + 1
        if i % 2 == 0:
            a = min(list[i // 2] + 1, a)
        if i % 3 == 0:
            a = min(list[i // 3] + 1, a)
        list.append(a)
    j = n
    answers = []
    while j > 1:
        if list[j] == list[j - 1] + 1:
            answers.insert(0, '1')
            j -= 1
            continue
        if (j % 2 == 0) & (list[j] == list[j // 2] + 1):
            answers.insert(0, '2')
            j //= 2
            continue
        answers.insert(0, '3')
        j //= 3
    return ''.join(answers)


param = int(input())
print(calc_with_answers(param))
