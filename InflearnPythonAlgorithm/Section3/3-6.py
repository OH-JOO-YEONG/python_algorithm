n = int(input())

player = []

for i in range(n):
    h, k = map(int, input().split())
    player.append((h, k))

player.sort(reverse=True)
k = 0
cnt = 0
for p in player:
    if p[1] > k:
        cnt += 1
        k = p[1]
print(cnt)