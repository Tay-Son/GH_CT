def solution(mat_land, threshold_):
    import heapq as hq
    import sys
    sys.setrecursionlimit(90009)

    N_ = len(mat_land)
    mat_iv = [[-1 for _ in range(N_)] for _ in range(N_)]

    def dfs_a(idx_c_r, idx_c_c, cnt_):
        mat_iv[idx_c_r][idx_c_c] = cnt_
        curr_height = mat_land[idx_c_r][idx_c_c]
        for o_r, o_c in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            t_r, t_c = idx_c_r + o_r, idx_c_c + o_c
            if 0 <= t_r < N_ \
                    and 0 <= t_c < N_ \
                    and mat_iv[t_r][t_c] == -1 \
                    and abs(curr_height - mat_land[t_r][t_c]) <= threshold_:
                dfs_a(t_r, t_c, cnt_)

    cnt_ = 0
    for idx_c_r in range(N_):
        for idx_c_c in range(N_):
            if mat_iv[idx_c_r][idx_c_c] == -1:
                dfs_a(idx_c_r, idx_c_c, cnt_)
                cnt_ += 1

    grp_ = [dict() for _ in range(cnt_)]
    for idx_c_r in range(N_):
        for idx_c_c in range(N_):
            for o_r, o_c in [(0, 1), (1, 0)]:
                t_r, t_c = idx_c_r + o_r, idx_c_c + o_c
                if 0 <= t_r < N_ and 0 <= t_c < N_:
                    g_a = mat_iv[idx_c_r][idx_c_c]
                    g_b = mat_iv[t_r][t_c]
                    diff_ = abs(mat_land[idx_c_r][idx_c_c] - mat_land[t_r][t_c])
                    if g_a != g_b:
                        if g_b not in grp_[g_a]:
                            grp_[g_a][g_b] = diff_
                        else:
                            grp_[g_a][g_b] = min(grp_[g_a][g_b], diff_)
                        if g_a not in grp_[g_b]:
                            grp_[g_b][g_a] = diff_
                        else:
                            grp_[g_b][g_a] = min(grp_[g_b][g_a], diff_)

    tot_ = 0
    lst_iv = [False for _ in range(cnt_)]
    hqu_ = [(0, 0)]
    while hqu_:
        dist_, idx_s = hq.heappop(hqu_)
        if not lst_iv[idx_s]:
            lst_iv[idx_s] = True
            tot_ += dist_
            for idx_e, dist_ in grp_[idx_s].items():
                if not lst_iv[idx_e]:
                    hq.heappush(hqu_, (dist_, idx_e))

    return tot_


print(solution(
    [[10, 11, 10, 11],
     [2, 21, 20, 10],
     [1, 20, 21, 11],
     [2, 1, 2, 1]],
    1))
