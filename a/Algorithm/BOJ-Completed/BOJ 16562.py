import sys

sys.setrecursionlimit(10 ** 4)

N_, M_, K_ = map(int, sys.stdin.readline().split())
lst_ = [0] + list(map(int, sys.stdin.readline().split()))

grp_ = [[] for _ in range(N_ + 1)]
for _ in range(M_):
    v_, w_ = map(int, sys.stdin.readline().split())
    grp_[v_].append(w_)
    grp_[w_].append(v_)

lst_is = [False for _ in range(N_ + 1)]


def func(idx_):
    lst_is[idx_] = True
    min_ = lst_[idx_]
    for each_ in grp_[idx_]:
        if lst_is[each_] == False:
            min_ = min(min_, func(each_))
    return min_


answer_ = 0
for idx_ in range(1, N_ + 1):
    if lst_is[idx_] == False:
        answer_ += func(idx_)

if answer_ <= K_:
    print(answer_)
else:
    print('Oh no')
