def solution(N_, S_, E_, grp_, lst_trap):
    import heapq as hq

    INF_ = 1000000009

    dct_ = {trap_: idx_ for trap_, idx_ in zip(lst_trap, range(len(lst_trap)))}



    is_p = [True for _ in range(N_ + 1)]
    mat_p = [[INF_ for _ in range(N_ + 1)] for _ in range(N_ + 1)]
    mat_r = [[INF_ for _ in range(N_ + 1)] for _ in range(N_ + 1)]
    for idx_s, idx_e, weight_ in grp_:
        mat_p[idx_s][idx_e] = min(mat_p[idx_s][idx_e], weight_)
        mat_r[idx_e][idx_s] = min(mat_r[idx_e][idx_s], weight_)

    grd_d = [[INF_ for _ in range(4)] for _ in range(N_ + 1)]
    grd_d[S_][0] = 0
    grd_iv = [[False for _ in range(4)] for _ in range(N_ + 1)]

    hqu_ = [(0, S_, 0)]
    while hqu_:
        dist_, idx_s, dim_ = hq.heappop(hqu_)
        grd_iv[idx_][dim_] = True
        for idx_e in m

    return min(grd_d[E_])
