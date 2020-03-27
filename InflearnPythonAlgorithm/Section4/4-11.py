# 최대힙
import heapq as hq

a = []
# heapq 모듈은 최소힙을 기반이기 때문에 마이너스 부호를 넣어서 힙을 구성하면 최대힙 구성하는 것 같이 된다.
while True:
    n = int(input())
    if n == 1:
        break
    if n == 0:
        if len(a) == 0:
            print(-1)
        else:
            print(-hq.heappop(a))
    else:
        hq.heappush(-n)

