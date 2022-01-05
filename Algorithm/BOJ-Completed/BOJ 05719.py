import sys
import heapq as hq

INF_ = int(1e9)
N_, M_ = map(int, sys.stdin.readline().split())
while N_ != 0:
    S_, E_ = map(int, sys.stdin.readline().split())
    grp_ = [dict() for _ in range(N_)]
    for _ in range(M_):
        s_, e_, w_ = map(int, sys.stdin.readline().split())
        grp_[s_][e_] = w_

    lst_d = [INF_ for _ in range(N_)]
    lst_r = [set() for _ in range(N_)]
    lst_d[S_] = 0
    que_ = [(0, S_)]

    while que_:
        weight_curr, idx_curr = hq.heappop(que_)
        for idx_end, weight_end in grp_[idx_curr].items():
            temp_ = lst_d[idx_curr] + weight_end
            if temp_ < lst_d[idx_end]:
                lst_d[idx_end] = temp_
                lst_r[idx_end] = set([idx_curr])
                hq.heappush(que_, (temp_, idx_end))

            elif temp_ == lst_d[idx_end] and idx_curr not in lst_r[idx_end]:
                lst_d[idx_end] = temp_
                lst_r[idx_end].add(idx_curr)
                hq.heappush(que_, (temp_, idx_end))

    que_ = [E_]
    while que_:
        idx_e = hq.heappop(que_)
        for idx_r in lst_r[idx_e]:
            if idx_e in grp_[idx_r]:
                del (grp_[idx_r][idx_e])
                hq.heappush(que_, idx_r)

    lst_d = [INF_ for _ in range(N_)]
    lst_r = [[] for _ in range(N_)]
    lst_d[S_] = 0
    que_ = [(0, S_)]

    while que_:
        weight_curr, idx_curr = hq.heappop(que_)
        for idx_end, weight_end in grp_[idx_curr].items():
            temp_ = lst_d[idx_curr] + weight_end
            if temp_ < lst_d[idx_end]:
                lst_d[idx_end] = temp_
                lst_r[idx_end] = [idx_curr]
                hq.heappush(que_, (temp_, idx_end))

            elif temp_ == lst_d[idx_end]:
                lst_d[idx_end] = temp_
                lst_r[idx_end].append(idx_curr)
                hq.heappush(que_, (temp_, idx_end))

    temp_ = lst_d[E_]
    if temp_ != INF_:
        print(temp_)
    else:
        print(-1)

    N_, M_ = map(int, sys.stdin.readline().split())
exit()