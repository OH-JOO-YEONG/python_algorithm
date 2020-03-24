s = input()

stack = []
b = ""
"""
틀렸음 오답
for i in s:
    if i == "+" or i == "-" or i == "*" or i == "/" or i == "(":
        if stack:
            if i == "*" or i == "/":
                if stack[-1] == "*" or stack[-1] == "/":
                    tmp = stack.pop()
                    b += tmp
        stack.append(i)
    elif i == ")":
        while stack:
            c = stack.pop()
            if c == "(":
                break
            b += c
        if stack:
            if stack[-1] == "*" or stack[-1] == "/":
                c = stack.pop()
                b += c
    else:
        b += i
stack = stack[::-1]
for i in stack:
    b += i
print(b)
"""

"""
정답지
"""
a = input()
stack = []
res = ''

for x in a:
    if x.isdecimal():
        res += x
    else:
        if x == '(':
            stack.append(x)
        elif x == '*' or x == '/':
            while stack and (stack[-1] == '*' or stack[-1] == '/'):
                res += stack.pop()
            stack.append(x)
        elif x == '+' or x == '-': # x가 '+'나 '-'인 피연산자면 stack이 있거나 stack[-1]이 '(' 아닐 때까지 res에 pop해서 넣어준다.
            while stack and stack[-1] != '(':
                res += stack.pop()
            stack.append(x)
        elif x == ')':# x가 ')' 이면 '(' 때까지
            while stack and stack[-1] != '(':
                res += stack.pop()
            stack.pop()

while stack:
    res += stack.pop()

print(res)