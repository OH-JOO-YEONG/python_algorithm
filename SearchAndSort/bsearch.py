# 이분 탐색의 원리
# 중간 위치를 찾습니다.
# 같다면 원하는 값을 찾은 것이므로 위치 번호르 결괏값으로 돌려줍니다.
# 찾는 값이 중간 위치값보다 크다면 중간 위치의 오른쪽을 대상으로 다시 탐색합니다
# 찾는 값이 중간 위치값보다 작다면 중간 위치의 왼쪽을 대상으로 다시 탐색합니다

# 이분 탐색

# def binary_search(a, x):
#     #탐색할 범위를 저장하는 변수 start, end
#     #리스트 전체를 범위로 탐색 시작(0 ~ len(a) - 1)
#     start = 0
#     end = len(a) - 1
#
#     while start <= end:
#         mid = (start + end) // 2
#         print("start : ", start)
#         print("mid : ", mid)
#         print("end : ", end)
#         if x == a[mid]:
#             return mid
#         elif x > a[mid]:
#             start = mid + 1
#         else:
#             end = mid - 1
#     return -1
#
# d = [1, 4, 9, 16, 25, 36, 49, 64, 81]
# print(binary_search(d, 36))
# print(binary_search(d, 74))

def jaekwi_binary_search_sub(a, x, start, end):

    if start > end:
        return -1

    mid = (start + end) // 2
    if x == a[mid]:
        return mid
    elif x > a[mid]:
        return jaekwi_binary_search_sub(a, x, mid + 1, end)
    else:
        return jaekwi_binary_search_sub(a, x, start, mid - 1)

    return -1

def jaekwi_binary_search(a, x):
    return jaekwi_binary_search_sub(a, x, 0, len(a) - 1)

d = [1, 4, 9, 16, 25, 36, 49, 64, 81]
print(jaekwi_binary_search(d, 36))
print(jaekwi_binary_search(d, 74))