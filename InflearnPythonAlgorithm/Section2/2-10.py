# 스도쿠 검사
a = [list(map(int, input().split())) for _ in range(9)]

def my_solution(a):
    # 나의 코드 의도
    # 한번에 하려했음 모든 것을 구하려다가 메모리낭비와 시간낭비가 심했음
    dx = [-1, -1, 0, 1, 1, 1, 0, -1]
    dy = [0, 1, 1, 1, 0, -1, -1, -1]
    for i in range(9):
        # lt와 rt는 3 * 3 부분의 중복을 찾으려는 변수
        lt = 0
        rt = 0
        if i >= 3:
            lt += 3
        if i >= 6:
            lt += 3
        for j in range(9):
            if j == 3 + rt:
                rt += 3
            # 여길 매번 81번동안 매번 요 if문을 실행하는 게 너무 안좋음. 시간낭비심함
            if all(a[1 + lt][1 + rt] == a[1 + lt + dx[k]][1 + rt + dy[k]] for k in range(8)):
                print("1여기")
                return False

            for c in range(9):
                if c != j:
                    if a[i][c] == a[i][j]:
                        print("2여기")
                        return False
                if c != i:
                    if a[c][j] == a[i][j]:
                        print("3여기")
                        return False
    return True

if my_solution(a):
    print("YES")
else:
    print("NO")

"""
체크리스트를 만들어서 하나씩 체크하고 체크리스트의 합이 9가 안되면 False를 리턴해주는 것
def check(a):
    for i in range(9):
        ch1 = [0] * 10
        ch2 = [0] * 10
        for j in range(9):
            ch1[a[i][j]] = 1
            ch2[a[j][i]] = 1
        if sum(ch1) != 9 or sum(ch2) != 9:
            return False
    for i in range(3):
        for j in range(3):
            ch3 = [0] * 10
            for k in range(3):
                for s in range(3):
                    ch3[a[i * 3 + k][j * 3 + s]] = 1
            if sum(ch3) != 9:
                return False
    return True
"""

