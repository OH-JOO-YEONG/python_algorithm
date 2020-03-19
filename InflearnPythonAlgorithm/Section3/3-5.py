from operator import itemgetter

n = int(input())

a = []

for i in range(n):
    s = list(map(int, input().split()))
    a.append(s)

a.sort(key=itemgetter(0))
a.sort(key=itemgetter(1))

e = a[0][1]
cnt = 1
for i in range(1, n):
    if a[i][0] < e:
        pass
    else:
        e = a[i][1]
        cnt += 1
print(cnt)

"""
정답지
meeting = []
for i in range(n):
    s, e = map(int, input().split())
    meeting.append((s, e))
meeting.sort(key=lambda x : (x[1], x[0])) # x를 매개변수로 보고 x[1]이 우선순위 x[0]이 차순위
et = 0
cnt = 0
for s, e in meeting:
    if s >= et:
        et = e
        cnt += 1
print(cnt)
"""


