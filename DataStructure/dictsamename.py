# 딕셔너리를 이용해 동명이인을 찾는 알고리즘
# 1. 각 이름이 등장하는 횟수를 저장할 빈 딕셔너리를 만듭니다.
# 2. 입력으로 주어진 리스트에서 각 이름을 꺼내면서 반복합니다.
# 3. 주어진 이름이 name_dict에 있는지 확인합니다.
# 4. 이미 있다면 등장 횟수를 1 증가시킵니다.
# 5. 아직 없다면 그 이름을 키로 하는 항목을 새로 만들어 1을 저장합니다.
# 6. 1~5번 과정을 거치면 name_dict에는 리스트에 등장하는 모든 이름과 각각의 등장 횟수가 저장됩니다.
# 7. 만들어진 딕셔너리에서 등장 횟수가 2 이상인 이름을 찾아 결과 집합에 넣은 다음 출력으로 돌려줍니다.
def find_same_name(a):
    name_dict = {}
    for name in a:
        if name in name_dict:
            name_dict[name] += 1
        else:
            name_dict[name] = 1

    result = set()
    for name in name_dict:
        if name_dict[name] >= 2:
            result.add(name)

    return result

name1 = ["Tom", "Mike", 'Jerry', 'Tom']
print(find_same_name(name1))
name2 = ["Tom", "Mike", 'Jerry', 'Tom', "Mike"]
print(find_same_name(name2))

def numSearchStu(s_info, find_num):
    if find_num in s_info:
        return s_info[find_num]
    else:
        return "?"
sample_info = {
    39: "Justin",
    14: "John",
    67: "Mike",
    105: "Summer"
}

print(numSearchStu(sample_info, 105))
print(numSearchStu(sample_info, 777))