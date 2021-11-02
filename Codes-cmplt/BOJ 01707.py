import sys

sys.setrecursionlimit(10 ** 6)


def dfs_(g_, idx_):
    lst_iv[idx_] = g_
    for idx_t in grp_[idx_]:
        if not lst_iv[idx_t]:
            if not dfs_(-g_, idx_t):
                return False
        elif lst_iv[idx_t] == g_:
            return False
    return True


for _ in range(int(sys.stdin.readline())):
    V_, E_ = map(int, sys.stdin.readline().split())
    grp_ = [[] for _ in range(V_ + 1)]
    for _ in range(E_):
        idx_a, idx_b = map(int, sys.stdin.readline().split())
        grp_[idx_a].append(idx_b)
        grp_[idx_b].append(idx_a)

    lst_iv = [0 for _ in range(V_ + 1)]

    is_ = True
    for idx_ in range(1, V_ + 1):
        if not lst_iv[idx_]:
            if not dfs_(idx_, idx_):
                is_ = False
                break

    print('YES' if is_ else 'NO')

exit()
