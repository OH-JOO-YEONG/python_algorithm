s = input()

stack = []
a = [0] * 2

for i in s:
    if i.isdecimal():
        stack.append(int(i))
    else:
        if i == '+':
            for j in range(2):
                if stack:
                    a[j] = stack.pop()
            stack.append(a[1] + a[0])
        if i == '-':
            for j in range(2):
                if stack:
                    a[j] = stack.pop()
            stack.append(a[1] - a[0])
        if i == '*':
            for j in range(2):
                if stack:
                    a[j] = stack.pop()
            stack.append(a[1] * a[0])
        if i == '/':
            for j in range(2):
                if stack:
                    a[j] = stack.pop()
            stack.append(a[1] / a[0])

print(stack[0])