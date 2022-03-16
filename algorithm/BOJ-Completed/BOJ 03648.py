import sys

sys.setrecursionlimit(1009)


def t_(in_):
    return in_ << 1


def f_(in_):
    return in_ << 1 | 1


def not_(in_):
    return in_ ^ 1


def dfs_(idx_s, grp_, lst_iv, stk_):
    lst_iv[idx_s] = True
    for idx_e in grp_[idx_s]:
        if not lst_iv[idx_e]:
            dfs_(idx_e, grp_, lst_iv, stk_)
    stk_.append(idx_s)


def dfs_r(idx_s, idx_c, grp_, lst_iv, lst_):
    lst_iv[idx_s] = True
    lst_[idx_s] = idx_c
    for idx_e in grp_[idx_s]:
        if not lst_iv[idx_e]:
            dfs_r(idx_e, idx_c, grp_, lst_iv, lst_)


while True:
    try:
        N_, M_ = map(int, sys.stdin.readline().split())
    except:
        break
    grp_f = [[] for _ in range(N_ << 1 + 2)]
    grp_r = [[] for _ in range(N_ << 1 + 2)]
    for _ in range(M_):
        a_, b_ = map(lambda x: t_(int(x)) if int(x) > 0 else f_(-int(x)), sys.stdin.readline().split())
        grp_f[not_(a_)].append(b_)
        grp_f[not_(b_)].append(a_)
        grp_r[b_].append(not_(a_))
        grp_r[a_].append(not_(b_))

    stk_ = []
    lst_iv = [False for _ in range(2 * (N_ + 1))]
    for idx_ in range(2, 2 * (N_ + 1)):
        if not lst_iv[idx_]:
            dfs_(idx_, grp_f, lst_iv, stk_)

    lst_scc = [0 for _ in range(2 * (N_ + 1))]
    lst_iv = [False for _ in range(2 * (N_ + 1))]
    idx_ = 1
    while stk_:
        idx_s = stk_.pop()
        if not lst_iv[idx_s]:
            dfs_r(idx_s, idx_, grp_r, lst_iv, lst_scc)
            idx_ += 1

    is_ = False
    for idx_ in range(1, N_ + 1):
        if lst_scc[t_(idx_)] == lst_scc[f_(idx_)]:
            is_ = True
            break
    if not is_ and lst_scc[t_(1)] > lst_scc[f_(1)]:
        print('yes')
    else:
        print('no')

exit()

import sys

sys.setrecursionlimit(100009)


def idx_(in_):
    return 2 * abs(in_) + int(in_ > 0) - 2


def dfs_(idx_s, grp_, lst_iv, stk_):
    lst_iv[idx_s] = True
    for idx_e in grp_[idx_s]:
        if not lst_iv[idx_e]:
            dfs_(idx_e, grp_, lst_iv, stk_)
    stk_.append(idx_s)


def dfs_r(idx_s, idx_c, grp_, lst_iv, lst_):
    lst_iv[idx_s] = True
    lst_[idx_s] = idx_c
    for idx_e in grp_[idx_s]:
        if not lst_iv[idx_e]:
            dfs_r(idx_e, idx_c, grp_, lst_iv, lst_)


while True:
    try:
        N_, M_ = map(int, sys.stdin.readline().split())
    except:
        break

    grp_f = [[] for _ in range(N_ * 2)]
    grp_r = [[] for _ in range(N_ * 2)]
    for _ in range(M_):
        c_a, c_b = map(lambda x: int(x), sys.stdin.readline().split())
        t_a, t_b = -c_a, -c_b

        grp_f[idx_(t_a)].append(idx_(c_b))
        grp_f[idx_(t_b)].append(idx_(c_a))
        grp_r[idx_(c_b)].append(idx_(t_a))
        grp_r[idx_(c_a)].append(idx_(t_b))

    for idx_c in range(N_ * 2):
        grp_f[idx_c].sort()
        grp_r[idx_c].sort()

    lst_iv = [False for _ in range(N_ * 2)]
    stk_ = []
    for idx_s in range(N_ * 2):
        if not lst_iv[idx_s]:
            dfs_(idx_s, grp_f, lst_iv, stk_)

    is_ = True
    lst_iv = [False for _ in range(N_ * 2)]
    lst_scc = [0 for _ in range(N_ * 2)]
    while stk_:
        idx_s = stk_.pop()
        stk_sub = []
        if not lst_iv[idx_s]:
            dfs_(idx_s, grp_r, lst_iv, stk_sub)
        print(stk_sub)
        lst_scc = [0 for _ in range(N_ * 2)]
        idx_c = 1
        while stk_sub:
            temp_ = stk_sub.pop()
            if not lst_iv[temp_]:
                dfs_r(temp_, idx_c, grp_r, lst_iv, lst_scc)
                idx_c += 1

        print(lst_scc)
    for idx_s in range(1, N_ + 1):
        if lst_scc[idx_(idx_s)] == lst_scc[idx_(-idx_s)]:
            is_ = False
            break

    if is_ and lst_scc[idx_(1)] > lst_scc[idx_(-1)]:
        print('yes')
    else:
        print('no')

exit()
