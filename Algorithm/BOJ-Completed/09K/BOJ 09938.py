import sys

sys.setrecursionlimit(100000)

N_, L_ = map(int, sys.stdin.readline().split())

lst_p = [idx_ for idx_ in range(L_ + 1)]
lst_c = [False for _ in range(L_ + 1)]


def find(idx_):
    temp_ = lst_p[idx_]
    if temp_ != idx_:
        temp_ = find(temp_)
        lst_p[idx_] = temp_
    return temp_


def union(idx_a, idx_b):
    p_a = find(idx_a)
    p_b = find(idx_b)
    lst_p[p_a] = p_b
    print('LADICA')


for idx_ in range(1, N_ + 1):
    A_, B_ = map(int, sys.stdin.readline().split())
    if not lst_c[A_]:
        lst_c[A_] = True
        union(A_, B_)
    elif not lst_c[B_]:
        lst_c[B_] = True
        union(B_, A_)
    elif not lst_c[find(A_)]:
        lst_c[find(A_)] = True
        union(A_, B_)
    elif not lst_c[find(B_)]:
        lst_c[find(B_)] = True
        union(B_, A_)
    else:
        print('SMECE')

exit()
