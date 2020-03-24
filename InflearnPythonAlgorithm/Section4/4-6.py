from collections import deque
n, m = map(int, input().split())
dq = deque(map(int, input().split()))
dq[m] = -dq[m]

cnt = 0
while dq:
    cur = dq.popleft()
    for i in dq:
        if abs(cur) < abs(i):
            dq.append(cur)
            break
    else:
        cnt += 1
        if cur < 0:
            print(cnt)
            break

"""
정답지
n, m = map(int, input().split())
Q = [(pos, val) for pos, val in enumerate(list(map(int, input().split())))]
Q = deque(Q)
cnt = 0
while True:
    cur = Q.popleft()
    if any(cur[1] < x[1] for x in Q): # any 메소드는 단 하나라도 참이 되면 참이다.
        Q.append(cur)
    else:
        cnt += 1
        if cnt[0] == m:
            break
print(cnt)
"""