import sys
import heapq as hq

sys.setrecursionlimit(10009)
INF_ = 3000001

N_, M_ = map(int, sys.stdin.readline().split())
s_n, s_m, e_n, e_m = map(lambda x_: int(x_) - 1, sys.stdin.readline().split())
print(s_n, s_m, e_n, e_m)

grd_ = []
for _ in range(N_):
    grd_.append(list(map(int, sys.stdin.readline().split())))

grd_dp = [[[INF_ for _ in range(3)] for _ in range(M_)] for _ in range(N_)]
hqu_ = [(grd_[s_n][s_m], s_n, s_m, 1)]

while hqu_:
    tot_, idx_s_n, idx_s_m, depth_ = hq.heappop(hqu_)
    print(idx_s_n, idx_s_m, depth_, tot_)

    depth_ %= 3
    if tot_ < grd_dp[idx_s_n][idx_s_m][depth_]:
        grd_dp[idx_s_n][idx_s_m][depth_] = tot_
        if idx_s_n == e_n and idx_s_m == e_m:
            print(idx_s_n, idx_s_m, depth_, tot_)
            break
        else:
            if depth_ == 0:
                lst_aux = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            elif depth_ == 1:
                lst_aux = [(1, 0), (-1, 0)]
            else:
                lst_aux = [(0, 1), (0, -1)]
            for o_n, o_m in lst_aux:
                t_n = idx_s_n + o_n
                t_m = idx_s_m + o_m
                if 0 <= t_n < N_ and 0 <= t_m < M_:
                    temp_ = grd_[t_n][t_m]
                    if temp_ != -1:
                        hq.heappush(hqu_, (tot_ + temp_, t_n, t_m, depth_ + 1))

print()
for idx_c in range(3):
    for idx_n in range(N_):
        for idx_m in range(M_):
            temp_ = grd_dp[idx_n][idx_m][idx_c]
            if temp_ != INF_:
                print(temp_, end=' ')
            else:
                print('I', end=' ')
        print()
    print()

temp_ = min(grd_dp[e_n][e_m])
if temp_ == INF_:
    print(-1)
else:
    print(temp_)

exit()

import sys
import heapq as hq

sys.setrecursionlimit(10009)
INF_ = 3000001

N_, M_ = map(int, sys.stdin.readline().split())
s_n, s_m, e_n, e_m = map(lambda x_: int(x_) - 1, sys.stdin.readline().split())

grd_ = []
for _ in range(N_):
    grd_.append(list(map(int, sys.stdin.readline().split())))

grd_dp = [[[INF_ for _ in range(3)] for _ in range(M_)] for _ in range(N_)]
hqu_ = [(grd_[s_n][s_m], s_n, s_m, 1)]

while hqu_:
    tot_, idx_s_n, idx_s_m, depth_ = hq.heappop(hqu_)
    print(idx_s_n, idx_s_m, depth_, tot_)
    depth_ %= 3
    if tot_ < grd_dp[idx_s_n][idx_s_m][depth_]:
        grd_dp[idx_s_n][idx_s_m][depth_] = tot_
        if idx_s_n != e_n or idx_s_m != e_n:
            if depth_ == 0:
                lst_aux = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            elif depth_ == 1:
                lst_aux = [(1, 0), (-1, 0)]
            else:
                lst_aux = [(0, 1), (0, -1)]
            for o_n, o_m in lst_aux:
                t_n = idx_s_n + o_n
                t_m = idx_s_m + o_m
                print(t_n, t_m)
                if 0 <= t_n < N_ and 0 <= t_m < M_:
                    temp_ = grd_[t_n][t_m]
                    if temp_ != -1:
                        hq.heappush(hqu_, (tot_ + temp_, t_n, t_m, depth_ + 1))
        else:
            break

print()
for idx_c in range(3):
    for idx_n in range(N_):
        for idx_m in range(M_):
            temp_ = grd_dp[idx_n][idx_m][idx_c]
            if temp_ != INF_:
                print(temp_, end=' ')
            else:
                print('I', end=' ')
        print()
    print()

temp_ = min(grd_dp[e_n][e_m])
if temp_ == INF_:
    print(-1)
else:
    print(temp_)

exit()


def rec_(idx_s_n, idx_s_m, depth_, tot_):
    print(idx_s_n, idx_s_m, depth_, tot_)
    depth_ %= 3
    if tot_ < grd_dp[idx_s_n][idx_s_m][depth_]:
        grd_dp[idx_s_n][idx_s_m][depth_] = tot_
        if depth_ == 0:
            lst_aux = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        elif depth_ == 1:
            lst_aux = [(1, 0), (-1, 0)]
        else:
            lst_aux = [(0, 1), (0, -1)]
        for o_n, o_m in lst_aux:
            t_n = idx_s_n + o_n
            t_m = idx_s_m + o_m
            print(t_n, t_m)
            if 0 <= t_n < N_ and 0 <= t_m < M_:
                temp_ = grd_[t_n][t_m]
                if temp_ != -1:
                    rec_(t_n, t_m, depth_ + 1, tot_ + temp_)


rec_(s_n, s_m, 1, grd_[s_n][s_m])

print(min(grd_dp[e_n][e_m]))

for idx_c in range(3):
    for idx_n in range(N_):
        for idx_m in range(M_):
            temp_ = grd_dp[idx_n][idx_m][idx_c]
            if temp_ != INF_:
                print(temp_, end=' ')
            else:
                print('I', end=' ')
        print()
    print()

exit()
