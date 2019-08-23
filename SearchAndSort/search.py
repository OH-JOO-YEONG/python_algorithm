def search_list(a, x):
    n = len(a)
    for i in range(n):
        if x == a[i]:
            return i

    return -1

v = [17, 92, 18, 33, 58, 7, 33, 42]
print(search_list(v, 18))
print(search_list(v, 33))
print(search_list(v, 900))

#practice
# 7-1
def search_all_list(a, y):
    n = len(a)
    x = []
    for i in range(n):
        if y == a[i]:
            x.append(i)
    return x

print(search_all_list(v, 18))
print(search_all_list(v, 33))
print(search_all_list(v, 900))

# 7-3
stu_no = [39, 14, 67, 105]
stu_name = ["Justin", "John", "Mike", "Summer"]

def searchStu(s_no, s_name, x):
    n = len(s_no)

    for i in range(0, n):
        if x == s_no[i]:
            return s_name[i]

    return "?"

print(searchStu(stu_no, stu_name, 105))
print(searchStu(stu_no, stu_name, 233))