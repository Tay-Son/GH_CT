def solution(mat_map):
    import heapq as hq
    INF_ = 100000009
    C_ = len(mat_map)
    R_ = len(mat_map[0])

    mat_d = [[INF_ for _ in range(R_)] for _ in range(C_)]
    mat_d[0][0] = 1

    hqu_ = [(1, 0, 0)]
    while hqu_:
        dist_, c_c, c_r = hq.heappop(hqu_)
        dist_ += 1
        for o_c, o_r in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            t_c, t_r = c_c + o_c, c_r + o_r
            if 0 <= t_c < C_ and 0 <= t_r < R_ and mat_map[t_c][t_r]:
                if mat_d[t_c][t_r] > dist_:
                    mat_d[t_c][t_r] = dist_
                    hq.heappush(hqu_, (dist_, t_c, t_r))

    return mat_d[C_ - 1][R_ - 1] if mat_d[C_ - 1][R_ - 1] != INF_ else -1


print(solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]))
