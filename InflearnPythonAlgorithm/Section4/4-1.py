num, m = map(int, input().split())
num = list(map(int, str(num))) # string 상태에서 숫자화시켜 리스트에 넣는 방식
stack = []
for x in num:
    while stack and m > 0 and stack[-1] < x:
        stack.pop()
        m -= 1
    stack.append(x)

if m != 0:
    stack = stack[:-m]

res = ''.join(map(str, stack))
print(res)

