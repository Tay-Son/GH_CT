import sys
import heapq as hq

sys.setrecursionlimit(100009)

DIV_ = 1000000007

N_ = int(sys.stdin.readline())
grp_ = [[] for _ in range(N_ + 1)]
lst_n = [0] + list(map(int, sys.stdin.readline().split()))
for _ in range(N_ - 1):
    idx_a, idx_b = map(int, sys.stdin.readline().split())
    grp_[idx_a].append(idx_b)
    grp_[idx_b].append(idx_a)

lst_p = [0 for _ in range(N_ + 1)]
hqu_ = []


def dfs(idx_h, idx_s, depth_):
    hq.heappush(hqu_, (depth_, idx_s))
    lst_p[idx_s] = idx_h
    for idx_e in grp_[idx_s]:
        if idx_e != idx_h:
            dfs(idx_s, idx_e, depth_ - 1)


dfs(0, 1, 0)

lst_dp = [[0 for _ in range(10)] for _ in range(N_ + 1)]
while hqu_:
    trs_, curr_ = hq.heappop(hqu_)
    lst_dp[curr_][lst_n[curr_]] += 1
    h_ = lst_p[curr_]
    tot_ = 0
    for idx_ in range(9, -1, -1):
        lst_dp[h_][idx_] += lst_dp[curr_][idx_]
        if idx_ >= lst_n[h_]:
            tot_ += lst_dp[curr_][idx_]
        if idx_ == lst_n[h_]:
            lst_dp[h_][idx_] = (lst_dp[h_][idx_] + tot_) % DIV_

print(sum(lst_dp[1]) % DIV_)
exit()
