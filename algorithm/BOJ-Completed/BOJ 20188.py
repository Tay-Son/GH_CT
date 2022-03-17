import sys

sys.setrecursionlimit(999999)

N_ = int(sys.stdin.readline())
grp_ = [[] for _ in range(N_ + 1)]
for _ in range(N_ - 1):
    a_, b_ = map(int, sys.stdin.readline().split())
    grp_[a_].append(b_)
    grp_[b_].append(a_)

lst_c = [0 for _ in range(N_ + 1)]
ans_ = 0
cch_ = (N_ * (N_ - 1)) // 2


def nc2_(n_):
    return (n_ * (n_ - 1)) // 2


def func_(idx_):
    global ans_, cch_
    lst_c[idx_] = 1
    for idx_c in grp_[idx_]:
        if not lst_c[idx_c]:
            lst_c[idx_] += func_(idx_c)
    ans_ += cch_ - nc2_(N_ - lst_c[idx_])
    return lst_c[idx_]


func_(1)
print(ans_ - cch_)
exit()
