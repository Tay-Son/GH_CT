import sys

lst_time = []
lst_time_tot = []
grp_ = []
tot_ = 0


def func_(idx_s):
    if lst_time_tot[idx_s] == -1:
        max_ = 0
        for idx_c in grp_[idx_s]:
            max_ = max(max_, func_(idx_c))
        lst_time_tot[idx_s] = max_ + lst_time[idx_s]
    return lst_time_tot[idx_s]


for _ in range(int(sys.stdin.readline())):
    N_, K_ = map(int, sys.stdin.readline().split())
    lst_time = [0] + list(map(int, sys.stdin.readline().split()))
    print(lst_time)
    lst_time_tot = [-1 for _ in range(N_ + 1)]
    grp_ = [[] for _ in range(N_ + 1)]
    tot_ = 0
    for _ in range(K_):
        idx_c, idx_s = map(int, sys.stdin.readline().split())
        grp_[idx_s].append(idx_c)
    print(func_(int(sys.stdin.readline())))
exit()
