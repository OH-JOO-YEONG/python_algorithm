# 선택 정렬

def find_min_idx(a):
    n = len(a)
    min_idx = 0
    for i in range(1, n):
        if a[i] < a[min_idx]:
            min_idx = i
    return min_idx

def sel_sort(a):
    result = []
    while a: # 주어진 리스트에 값이 남아 있는 동안 계속
        min_idx = find_min_idx(a) # 리스트에 남아 있는 값 중 최솟값의 위치
        value = a.pop(min_idx) # 찾은 최솟값을 빼내어 value에 저장
        result.append(value) # value를 결과 리스트 끝에 추가
    return result

d = [2, 4, 5, 1, 3]
print(sel_sort(d))

def sel_sort1(a):
    n = len(a)
    for i in range(0, n-1): # 0부터  n - 2까지 반복
        # 1번 위치부터 끝까지 자료값 중 최솟값의 위치를 찾음
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j
                print(min_idx)
        a[i], a[min_idx] = a[min_idx], a[i]
        print(a)
        print("---")

b = [2, 4, 5, 1, 3]
sel_sort1(b)
print(b)

def sel_nsort(a):
    n = len(a)
    for i in range(0, n - 1):
        max_idx = i
        for j in range(i + 1, n):
            if a[j] > a[max_idx]:
                max_idx = j
        a[i], a[max_idx] = a[max_idx], a[i]
        print(a)
        print("---")

c = [2, 4, 5, 1, 3]
sel_nsort(c)
print(c)

