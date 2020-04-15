# 수들의 조합
def DFS(L, s):
    global cnt
    if L == k:
        if sum(res) % m == 0:
            cnt += 1
    else:
        for i in range(s, n):
            res[L] = a[i]
            DFS(L + 1, i + 1)



if __name__=="__main__":
    n, k = map(int, input().split())
    res = [0] * k
    a = list(map(int, input().split()))
    m = int(input())
    cnt = 0
    DFS(0, 0)
    print(cnt)


# 여긴 res 리스트를 안써도 되는 정답지라 메모리관리가 더 좋음 매개변수 3개 생각
"""
정답지
def DFS(L, s, sum):
    global cnt
    if L == k:
        if sum % m == 0:
            cnt += 1
    else:
        for i in range(s, n):
            DFS(L + 1, i + 1, sum + a[i])
"""
