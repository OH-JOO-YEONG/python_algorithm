n = int(input())

g = list(map(int, input().split()))

m = int(input())

for _ in range(m):
    large = max(g)
    mini = min(g)
    h = g.index(large)
    l = g.index(mini)
    g[h] -= 1
    g[l] += 1

"""
다른 답
이번에는 위 답이랑 아래 답이랑 둘다 생각함
g.sort()
for _ in range(m):
    g[0] += 1
    g[n - 1] -= 1
    g.sort()
"""

large = max(g)
mini = min(g)
res = large - mini
print(res)
