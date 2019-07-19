#최댓값 구하기

def find_max(a):
    n = len(a)
    max_v = a[0]

    for i in range(1, n): # 자료 n개 중에서 최댓값 비교하는 구문 시간 복잡도 따지는 곳
        if a[i] > max_v:
            max_v = a[i]

    return max_v

b = [17, 92, 18, 33, 58, 7, 33, 42]

print(find_max(b))

# 시간복잡도 O(n)

#최댓값 위치를 구하는 알고리즘

def find_max_idx(a):
    n = len(a)
    max_idx = 0

    for i in range(1, n):
        if a[i] > a[max_idx]:
            max_idx = i

    return max_idx

b = [17, 92, 18, 33, 58, 7, 33, 42]
print(find_max_idx(b))
