# 삽입정렬

# def find_ins_idx(r, v):
#     #이미 정렬된 리스트 r의 자료를 앞에서부터 차례로 확인하여
#     for i in range(0, len(r)):
#         # v값 보다 i번 위치에 있는 자료 값이 크면
#         # v가 그 값 바로 앞에 놓여야 정렬 순서가 유지됨
#         if v < r[i]:
#             return i
#     # 적절한 위치를 못 찾았을 때는
#     # v가 r의 모든 자료보다 크다는 뜻이므로 맨 뒤에 삽입
#     return len(r)
#
# def ins_sort(a):
#     result = []
#     while a:
#         value = a.pop(0)
#         ins_idx = find_ins_idx(result, value)
#         print(result)
#         result.insert(ins_idx, value)
#         print(result)
#         print("--")
#     return result
#
# d = [2, 4, 5, 1, 3]
# print(ins_sort(d))

def ins_sort1(a):
    n = len(a)
    for i in range(1, n):
        key = a[i] # 1번위치에 있는 값을 key에 저장
        j = i - 1 # j를 i 바로 왼쪽 위치로 저장
        print("i : ", i)
        print("j : ", j)
        print("key :", key)
        # 리스트의 j번 위치에 있는 값과 key를 비교해 key가 삽입될 적절한 위치를 찾음
        while j >= 0 and a[j] > key:
            print("--전--")
            print("1 - a[j] :", a[j])
            print("1 - a[j+1] :", a[j+1])
            print(a)
            a[j + 1] = a[j] #삽입할 공간이 생기도록 값을 오른쪽으로 한 칸 이동
            print("--후--")
            print("2 - a[j] :", a[j])
            print("2 - a[j+1] :", a[j+1])
            print(a)
            j -= 1
        a[j + 1] = key #찾은 삽입 위치에 key를 저장
        print("3 - a[j] :", a[j])
        print("3 - a[j+1] :", a[j+1])
        print(a)
        print("-------")

d = [2, 4, 5, 1, 3]
ins_sort1(d)
print(d)
