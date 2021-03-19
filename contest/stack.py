def calc(list):
    stack = []
    for i in range(len(list)):
        if list[i]=='*':
            stack[len(stack) - 1] = stack[len(stack) - 2] * stack[len(stack) - 1]
            del stack[len(stack) - 2]
            continue
        if list[i]=='+':
            stack[len(stack) - 1] = stack[len(stack) - 2] + stack[len(stack) - 1]
            del stack[len(stack) - 2]
            continue
        if list[i] == '-':
            stack[len(stack) - 1] = stack[len(stack) - 2] - stack[len(stack) - 1]
            del stack[len(stack) - 2]
            continue
        if list[i] == '/':
            stack[len(stack) - 1] = stack[len(stack) - 2] / stack[len(stack) - 1]
            del stack[len(stack) - 2]
            continue
        stack.append(int(list[i]))
    return stack[0]


list = input().split()
print(calc(list))

