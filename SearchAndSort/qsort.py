# 퀵 정렬
# def quick_sort(a):
#     n = len(a)
#     # 종료 조건 : 정렬할 리스트이 자료 개수가 한 개 이하이면 정렬할 필요가 없음
#     if n <= 1:
#         return a
#
#     # 기준 값을 정하고 기준에 맞춰 그룹을 나누는 과정
#     pivot = a[-1] # 편의상 리스트의 마지막 값을 기준 값으로 정함
#     g1 = [] # 기준값보다 작은 값을 담을 리스트
#     g2 = [] # 기준값보다 큰 값을 담을 리스트
#     for i in range(0, n - 1):
#         if a[i] < pivot: # 기준 값과 비교
#             g1.append(a[i]) # 작으면 g1에 추가
#         else:
#             g2.append(a[i]) # 크면 g2에 추가
#     print("g1:", g1)
#     print("g2:", g2)
#     # 각 그룹에 대해 재귀 호출로 퀵 정렬을 한 후
#     # 기준 값과 합쳐 하나의 리스트로 결괏값 반환
#     print("pivot:", pivot)
#     print("---")
#     return  quick_sort(g1) + [pivot] + quick_sort(g2)
#
# d = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]
# print(quick_sort(d))

def quick_sort_sub(a, start, end):
    # 종료 조건 : 정렬 대상이 한 개 이하이면 정렬할 필요가 없음
    if end - start <= 0: # 원소가 1개인 경우 그대로 두기
        return
    # 기준 값을 정하고 기준 값에 맞춰 리스트 안에서 각 자료의 위치를 맞춤
    # [기준 값보다 작은 값들, 기준 값, 기준 값보다 큰 값들]
    pivot = a[end] # 편의상 리스트의 마지막 값을 기준 값으로 정함
    i = start
    for j in range(start, end):
        if a[j] <= pivot:
            a[i], a[j] = a[j], a[i]
            i += 1
            print("a:", a)
    a[i], a[end] = a[end], a[i] # i가 반복한 만큼이 피벗의 자리니 체인지
    print("a1:", a)
    # 재귀호출 부분
    print("---")
    quick_sort_sub(a, start, i - 1) # 기준 값보다 작은 그룹을 재귀 호출로 다시 정렬
    quick_sort_sub(a, i + 1, end) # 기준 값보다 큰 그룹을 재귀 호출로 다시 정렬

def quick_sort(a):
    quick_sort_sub(a, 0, len(a) - 1)

d = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]
quick_sort(d)
print(d)