import sys

sys.setrecursionlimit(10 ** 5)

N_ = int(sys.stdin.readline())

lst_ = []
grp_u = [[] for _ in range(N_ + 1)]
grp_d = [[] for _ in range(N_ + 1)]
for _ in range(int(sys.stdin.readline())):
    S_, E_, W_ = map(int, sys.stdin.readline().split())
    lst_.append((S_, E_, W_))
    grp_d[E_].append((S_, W_))
    grp_u[S_].append((E_, W_))

lst_dp_d = [-1 for _ in range(N_ + 1)]
lst_dp_u = [-1 for _ in range(N_ + 1)]

idx_s, idx_e = map(int, sys.stdin.readline().split())


def func_d(idx_):
    if lst_dp_d[idx_] == -1:
        max_ = 0
        for idx_t, weight_ in grp_d[idx_]:
            if idx_t != idx_s:
                weight_t = func_d(idx_t)
                if weight_t:
                    weight_ += weight_t
                else:
                    weight_ = 0
            max_ = max(max_, weight_)
        lst_dp_d[idx_] = max_
    return lst_dp_d[idx_]


def func_u(idx_):
    if lst_dp_u[idx_] == -1:
        max_ = 0
        for idx_t, weight_ in grp_u[idx_]:
            if idx_t != idx_e:
                weight_t = func_u(idx_t)
                if weight_t:
                    weight_ += weight_t
                else:
                    weight_ = 0
            max_ = max(max_, weight_)
        lst_dp_u[idx_] = max_
    return lst_dp_u[idx_]


dct_ = {}
weight_max = 0
for S_, E_, W_ in lst_:
    weight_ = func_u(E_) + func_d(S_) + W_
    weight_max = max(weight_max, weight_)
    if weight_ not in dct_:
        dct_[weight_] = 1
    else:
        dct_[weight_] += 1

print(weight_max)
print(dct_[weight_max])
exit()
