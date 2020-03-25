# 교육과정설계(큐)
from collections import deque
s = input()

n = int(input())
res = []
for i in range(n):
    t = input()
    dq = deque(s)
    for j in t:
        for p, v in enumerate(list(dq)): # if x in dq: 이걸 인지하지 못했음 다음부터는 인지하기!
            if j == v:
                if p != 0:
                    dq.append(j)
        if dq:
            if dq[0] == j:
                dq.popleft()
    if dq:
        res.append(f'#{i + 1} NO')
    else:
        res.append(f'#{i + 1} YES')

for i in res:
    print(i)

"""
정답지
need = input()
n = int(input())
for i in range(n):
    plan = input()
    dq = deque(need)
    for x in plan:
        if x in dq:
            if dq.popleft() != j:
                print(f'#{i + 1} NO')
                break
    else:
        if dq:
            print(f'#{i + 1} NO')
        else:
            print(f'#{i + 1} YES')
"""
