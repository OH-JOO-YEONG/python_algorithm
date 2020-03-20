from collections import deque

n, m = map(int, input().split())

p = list(map(int, input().split()))

p.sort()
p = deque(p)
cnt = 0

while p:
    if len(p) > 1 and p[0] + p[-1] <= m:
        p.popleft() # list 자료형은 pop(0)을 하면 뒤에 있는 자료들을 뒤에서 앞으로 땡긴다. 그래서 deque로 자료형을 바꿔주고 popleft() 메서드를 이용한다.
        p.pop()
        cnt += 1
    else:
        p.pop()
        cnt += 1

print(cnt)