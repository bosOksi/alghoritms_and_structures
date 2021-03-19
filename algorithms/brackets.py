def calc(num, count, stack, result):
    if count == num // 2 and len(stack) == 0:
        print(result)
        return
    if count < num // 2:
        calc(num, count + 1, stack + '(', result + '(')
        calc(num, count + 1, stack + '[', result + '[')
    if len(stack) > 0:
        if stack[-1] == '(':
            calc(num, count, stack[:-1], result + ')')
        if stack[-1] == '[':
            calc(num, count, stack[:-1], result + ']')


N = int(input())
calc(N, 0, "", "")
