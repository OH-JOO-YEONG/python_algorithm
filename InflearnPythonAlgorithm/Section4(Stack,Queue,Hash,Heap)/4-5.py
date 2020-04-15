# 공주구하기(큐)
from collections import deque

n, k = map(int, input().split())

q = [i for i in range(1, n + 1)]

q = deque(q)

cnt = 0
while len(q) != 1:
    if cnt == k - 1:
        q.popleft()
        cnt = 0
    else:
        cnt += 1
        q.append(q.popleft())
print(q[0])

"""
정답지
"""
n, k = map(int, input().split())

dq = list(range(1, n + 1))

dq = deque(dq)

while dq:
    for _ in range(k-1):
        cur = dq.popleft()
        dq.append(cur)
    dq.popleft()
    if len(dq) == 1:
        print(dq[0])
        dq.popleft()