import sys

sys.setrecursionlimit(100009)


def dfs_(idx_s, grp_, lst_iv, lst_):
    lst_iv[idx_s] = True
    for idx_e in grp_[idx_s]:
        if not lst_iv[idx_e]:
            dfs_(idx_e, grp_, lst_iv, lst_)
    lst_.append(idx_s)


def dfs2_(idx_s, grp_, lst_iv):
    lst_iv[idx_s] = True
    for idx_e in grp_[idx_s]:
        if not lst_iv[idx_e]:
            dfs2_(idx_e, grp_, lst_iv)


for _ in range(int(sys.stdin.readline())):
    N_, M_ = map(int, sys.stdin.readline().split())
    grp_ = [[] for _ in range(N_ + 1)]

    for _ in range(M_):
        idx_s, idx_e = map(int, sys.stdin.readline().split())
        grp_[idx_s].append(idx_e)
    for idx_s in range(1, N_ + 1):
        grp_[idx_s].sort()

    stk_ = []
    lst_iv = [False for _ in range(N_ + 1)]
    for idx_s in range(1, N_ + 1):
        if not lst_iv[idx_s]:
            dfs_(idx_s, grp_, lst_iv, stk_)

    lst_iv = [False for _ in range(N_ + 1)]
    tot_ = 0
    while stk_:
        idx_s = stk_.pop()
        if not lst_iv[idx_s]:
            tot_ += 1
            dfs2_(idx_s, grp_, lst_iv)
    print(tot_)
exit()

for _ in range(int(sys.stdin.readline())):
    N_, M_ = map(int, sys.stdin.readline().split())
    grp_f = [[] for _ in range(N_ + 1)]
    grp_r = [[] for _ in range(N_ + 1)]

    for _ in range(M_):
        idx_s, idx_e = map(int, sys.stdin.readline().split())
        grp_f[idx_s].append(idx_e)
        grp_r[idx_e].append(idx_s)
    for idx_s in range(1, N_ + 1):
        grp_f[idx_s].sort()

    stk_ = []
    lst_iv = [False for _ in range(N_ + 1)]
    for idx_s in range(1, N_ + 1):
        if not lst_iv[idx_s]:
            dfs_(idx_s, grp_f, lst_iv, stk_)

    lst_iv = [False for _ in range(N_ + 1)]
    grd_ = []
    lst_p = [-1 for _ in range(N_ + 1)]
    while stk_:
        idx_s = stk_.pop()
        if not lst_iv[idx_s]:
            lst_temp = []
            dfs_(idx_s, grp_r, lst_iv, lst_temp)
            grd_.append(lst_temp)
            for idx_ in lst_temp:
                lst_p[idx_] = len(grd_) - 1

    grp_gf = []
    for idx_grd in range(len(grd_)):
        set_f = set()
        set_r = set()
        for idx_ in grd_[idx_grd]:
            for idx_e in grp_f[idx_]:
                if lst_p[idx_e] != idx_grd:
                    set_f.add(lst_p[idx_e])
        grp_gf.append(sorted(list(set_f)))

    stk_ = []
    lst_iv = [False for _ in range(len(grd_))]
    for idx_s in range(len(grd_)):
        if lst_iv[idx_s] == False:
            dfs_(idx_s, grp_gf, lst_iv, stk_)

    lst_trs = []
    lst_iv = [False for _ in range(len(grd_))]
    tot_ = 0
    while stk_:
        idx_s = stk_.pop()
        if lst_iv[idx_s] == False:
            tot_ += 1
            dfs_(idx_s, grp_gf, lst_iv, lst_trs)
    print(tot_)

exit()
