# 알파코드
alpha = (
    'A', 'B', 'C', 'D', 'E',
    'F', 'G', 'H', 'I', 'J',
    'K', 'L', 'M', 'N', 'O',
    'P', 'Q', 'R', 'S', 'T',
    'U', 'V', 'W', 'X', 'Y',
    'Z'
)

def dfs(l, p):
    global cnt
    if l > n:
        return
    if l == n:
        for j in range(p):
            print(alpha[res[j] - 1], end='')
        print()
        cnt += 1
    else:
        for i in range(1, 27):
            if code[l] == i:
                res[p] = i
                dfs(l + 1, p + 1)
            if i >= 10 and l + 1 < n:
                if int(str(code[l]) + str(code[l + 1])) == i:
                    res[p] = i
                    dfs(l + 2, p + 1)

if __name__=="__main__":
    code = list(map(int, input()))
    n = len(code)
    code.insert(n, -1)
    res = [0] * (n + 1)
    cnt = 0
    dfs(0, 0)
    print(cnt)

def DFS(L, P):
    global cnt
    if L == n:
        for j in range(P):
            print(chr(res[j] + 64), end='')
        print()
        cnt += 1
    else:
        for i in range(1, 27):
            if code[L] == i:
                res[P] = i
                DFS(L + 1, P + 1)
            elif i >= 10 and code[L] == i // 10 and code[L + 1] == i % 10:
                res[P] = i
                DFS(L + 2, P + 1)