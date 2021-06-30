import sys
sys.setrecursionlimit(10**6)

N_, M_ = map(int, sys.stdin.readline().split())

lst_p = [idx_ for idx_ in range(N_ + 1)]


def find_(idx_):
    temp_ = lst_p[idx_]
    if temp_ != idx_:
        temp_ = find_(temp_)
        lst_p[idx_] = temp_
    return lst_p[idx_]


def union_(idx_a, idx_b):
    p_a = find_(idx_a)
    p_b = find_(idx_b)
    lst_p[p_a] = p_b


for _ in range(M_):
    com_, idx_a, idx_b = map(int, sys.stdin.readline().split())
    if com_:
        if find_(idx_a) == find_(idx_b):
            print('YES')
        else:
            print('NO')
    else:
        union_(idx_a, idx_b)

exit()
