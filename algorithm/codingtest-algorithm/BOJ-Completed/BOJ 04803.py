import sys


def rec_(idx_, idx_p, grp_, lst_iv):
    lst_iv[idx_] = True
    for idx_t in grp_[idx_]:
        if idx_t != idx_p:
            if not lst_iv[idx_t]:
                if not rec_(idx_t, idx_, grp_, lst_iv):
                    return False
            else:
                return False
    else:
        return True


idx_case = 0
N_, M_ = map(int, sys.stdin.readline().split())
while N_ + M_:
    idx_case += 1
    grp_ = [[] for _ in range(N_)]
    lst_iv = [False for _ in range(N_)]
    for _ in range(M_):
        a_, b_ = map(lambda x: int(x) - 1, sys.stdin.readline().split())
        grp_[a_].append(b_)
        grp_[b_].append(a_)
    tot_ = 0
    for idx_ in range(N_):
        if not lst_iv[idx_] and rec_(idx_, -1, grp_, lst_iv):
            tot_ += 1

    if not tot_:
        print('Case ' + str(idx_case) + ': No trees.')
    elif tot_ == 1:
        print('Case ' + str(idx_case) + ': There is one tree.')
    else:
        print('Case ' + str(idx_case) + ': A forest of ' + str(tot_) + ' trees.')

    N_, M_ = map(int, sys.stdin.readline().split())

exit()
