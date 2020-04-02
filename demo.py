# def solution(v):
#     a = []
#     b = []
#     answer = []
#     for i in range(3):
#         a.append(v[i][0])
#         b.append(v[i][1])
#     a1 = sum(a) - sum(set(a))
#     b1 = sum(b) - sum(set(b))
#     for j in range(2):
#         a.remove(a1)
#         b.remove(b1)
#     answer.append(a.pop())
#     answer.append(b.pop())
#     return answer


# A xor A = 0
# A xor A xor B = B를 이용하면 다른 값 1개를 쉽게 구할 수 있습니다.
# 0 xor B = B 이기 때문이다. xor은 0이 나오고 0이랑 xor하면 나머지 비교된 한 값이 나오게 된다.

def solution(v):
    answer = [0] * 2
    print(v[0][1] ^ v[1][1])
    answer[0] = v[0][0] ^ v[1][0] ^ v[2][0]
    answer[1] = v[0][1] ^ v[1][1] ^ v[2][1]
    return answer

print(solution([[1, 4], [3, 4], [3, 10]]))