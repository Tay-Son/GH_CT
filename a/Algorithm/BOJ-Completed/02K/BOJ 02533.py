import sys

sys.setrecursionlimit(10 ** 6)

N_ = int(sys.stdin.readline())
grp_ = [[] for _ in range(N_ + 1)]
for _ in range(N_ - 1):
    idx_a, idx_b = map(int, sys.stdin.readline().split())
    grp_[idx_a].append(idx_b)
    grp_[idx_b].append(idx_a)

lst_is_visited = [False for _ in range(N_ + 1)]
lst_dp = [[-1, -1] for _ in range(N_ + 1)]


def rec_(idx_):
    lst_is_visited[idx_] = True
    tot_a, tot_b = 1, 0
    for each_ in grp_[idx_]:
        if lst_is_visited[each_] == False:
            a_, b_ = rec_(each_)
            tot_a += min(a_, b_)
            tot_b += a_
    return tot_a, tot_b


print(min(rec_(1)))

exit()