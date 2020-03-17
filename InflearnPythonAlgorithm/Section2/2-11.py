a = [list(map(int, input().split())) for _ in range(7)]

res = 0

for i in range(7):
    for j in range(3):
        cnt = 0
        for k in range(2):
            if a[i][j + k] == a[i][-3 + j - k]:
                cnt += 1
            if cnt == 2:
                res += 1

for i in range(7):
    for j in range(3):
        cnt = 0
        for k in range(2):
            if a[j + k][i] == a[-3 + j - k][i]:
                cnt += 1
            if cnt == 2:
                res += 1

print(res)

"""
정답지
"""
board = [list(map(int, input().split())) for _ in range(7)]
cnt = 0
for i in range(3):
    for j in range(7):
        tmp = board[j][i:i+5]
        if tmp == tmp[::-1]:
            cnt += 1
        for k in range(2):
            if board[i + k][j] != board[i + 5 - k - 1][j]:
                break
        # for else 구동방식 - 정상적으로 for가 끝났으면 else문을 실행시킴
        else:
            cnt += 1