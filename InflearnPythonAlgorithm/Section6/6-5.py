

def dfs(l, sum1, sum2, sum3):
    global res
    if l == n:
        if sum1 != sum2 and sum2 != sum3 and sum1 != sum3:
            max1 = max(sum1, sum2, sum3)
            min1 = min(sum1, sum2, sum3)
            total = max1 - min1
            if total < res:
                res = total
    else:
        dfs(l + 1, sum1 + a[l], sum2, sum3)
        dfs(l + 1, sum1, sum2 + a[l], sum3)
        dfs(l + 1, sum1, sum2, sum3 + a[l])


if __name__=="__main__":
    n = int(input())
    a = []
    for _ in range(n):
        c = int(input())
        a.append(c)
    res = 2147000000
    dfs(0, 0, 0, 0)
    print(res)

"""
정답지
확장성이 더 크게 만드는 것. for i in range(n): 으로 하면 사람 수를 늘릴 수 있다.
def DFS(L):
    global res
    if L == n:
        cha = max(money) - min(money)
        if cha < res:
            tmp = set()
            for x in money:
                tmp.add(x)
            if len(tmp) == 3:
                res = cha
    else:
        for i in range(3):
            money[i] += coin[L]
            DFS(L + 1)
            money[i] -= coin[L]
"""

