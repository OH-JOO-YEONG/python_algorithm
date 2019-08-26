
def print_all_friends(g, start):
    qu = []
    done = set()

    qu.append((start, 0))
    done.add(start)
    print(qu)
    print(done)
    while qu:
        (p, d) = qu.pop(0)
        print("---")
        print("qu:", qu)
        print("done:", done)
        print("p : {} d : {}".format(p, d)) # 친구리스트 출력하는 곳
        print("1---")
        for x in g[p]:
            if x not in done:
                qu.append((x, d + 1))
                done.add(x)
                print("---")
                print("qu:", qu)
                print("done:", done)
                print("2---")

# 친구 관계 리스트
# A와 B가 친구이면
# A의 친구 리스트에도 B가 나오고, B의 친구 리스트에도 A가 나옴
fr_info = {
    'Summer' : ['John', 'Justin', 'Mike'],
    'John' : ['Summer', 'Justin'],
    'Justin' : ['John', 'Summer', 'Mike', 'May'],
    'Mike' : ['Summer', 'Justin'],
    'May' : ['Justin', 'Kim'],
    'Kim' : ['May'],
    'Tom' : ['Jerry'],
    'Jerry' : ['Tom']
}

print_all_friends(fr_info, 'Summer')
print()
print_all_friends(fr_info, 'Tom')

# 파이썬의 튜플
# 튜플은 여러 개의 정보를 묶어서 하나의 정보처럼 사용하기 위한 기능으로 수학에서 .x좌표와 y좌표를 묶어서 순서쌍(x, y)로 표현하는 것과 비슷한 개념

# t = (3, 7)
# t
# (3, 7)
# t[0]
# t[1]
# (x, y) = t
