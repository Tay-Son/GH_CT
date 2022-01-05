import sys

sys.setrecursionlimit(500009)

lst_p = []


def find_(idx_):
    temp_ = lst_p[idx_]
    if temp_ != idx_:
        temp_ = find_(temp_)
        lst_p[idx_] = temp_
    return temp_


def union_(idx_a, idx_b):
    p_a, p_b = find_(idx_a), find_(idx_b)
    lst_p[p_b] = p_a


N_, M_ = map(int, sys.stdin.readline().split())
lst_p = [-1 for _ in range(N_)]

answer_ = 0
for cnt_ in range(1, M_ + 1):
    idx_a, idx_b = map(int, sys.stdin.readline().split())
    if find_(idx_a) != find_(idx_b):
        union_(idx_a, idx_b)
    else:
        answer_ = cnt_
        break
print(answer_)

exit()
