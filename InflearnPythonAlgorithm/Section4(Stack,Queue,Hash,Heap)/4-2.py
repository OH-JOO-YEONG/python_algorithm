# 쇠막대기(스택)
s = input()

stack = []
res = 0
tmp = ''

for i in s:
    if tmp == '(' and i == '(':
        stack.append(tmp)
    if (tmp == '(' and i == ')') and stack:
        res += len(stack)
    if (tmp == ')' and i == ')') and stack:
        stack.pop()
        res += 1
    tmp = i

print(res)

"""
정답지
s = input()
stack = []
cnt = 0
for i in range(len(s)):
    if s[i] == '(':
        stack.append(s[i])
    else:
        stack.pop()
        if s[i - 1] == '(':
            cnt += len(stack)
        else:
            cnt += 1
print(cnt)
"""
