# 버블정렬
def bubble_sort(a):
    n = len(a)

    for i in range(0, n):
        for j in range(0, n - 1 - i):
            if a[j] > a[j + 1]:
                print(a)
                a[j], a[j + 1] = a[j + 1], a[j]

d = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]
bubble_sort(d)
print(d)