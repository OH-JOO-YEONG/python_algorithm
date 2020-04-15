

def dfs(d, sum):
    global res
    if d > n: # 정답지로 추가해준대로하면 이 조건문이 필요없음
        return
    if d == n:
        if sum > res:
            res = sum
    else:
        if d + w[d][0] <= n: # 정답지에 추가해준 것(한번의 효율성을 올려줌)
            dfs(d + w[d][0], sum + w[d][1])
        dfs(d + 1, sum)


if __name__=="__main__":
    n = int(input())
    w = []
    for _ in range(n):
        ti, pi = map(int, input().split())
        w.append([ti, pi])
    res = 0
    dfs(0, 0)
    print(res)
