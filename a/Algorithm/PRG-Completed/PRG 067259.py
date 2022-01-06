def solution(grd_):
    import heapq as hq

    INF_ = 100000000
    N_ = len(grd_)
    grd_iv = [[[INF_ for _ in range(4)] for _ in range(N_)] for _ in range(N_)]

    grd_iv[0][0] = [0, 0, 0, 0]

    hqu_ = [(0, 0, 0, state_) for state_ in range(4)]

    while hqu_:
        cost_, c_r, c_c, state_ = hq.heappop(hqu_)

        for o_r, o_c, t_state in [(0, 1, 0), (0, -1, 1), (1, 0, 2), (-1, 0, 3)]:
            t_r = c_r + o_r
            t_c = c_c + o_c
            if 0 <= t_r < N_ and 0 <= t_c < N_ and not grd_[t_r][t_c]:
                cost_temp = cost_ + (100 if state_ == t_state else 600)
                if grd_iv[t_r][t_c][t_state] > cost_temp:
                    grd_iv[t_r][t_c][t_state] = cost_temp
                    hq.heappush(hqu_, (cost_temp, t_r, t_c, t_state))

    print(grd_iv[N_ - 1][N_ - 1])
    return min(grd_iv[N_ - 1][N_ - 1])


print(solution([
    [0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 0],
    [0, 0, 1, 0, 0, 0],
    [1, 0, 0, 1, 0, 1],
    [0, 1, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0]]))
