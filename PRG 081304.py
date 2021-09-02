def solution(N_, S_, E_, lst_grp, lst_trap):
    import heapq as hq
    INF_ = 100000009

    S_ -= 1
    E_ -= 1
    mat_weight = [[INF_ for _ in range(N_)] for _ in range(N_)]
    for idx_s, idx_e, weight_ in lst_grp:
        idx_s -= 1
        idx_e -= 1
        mat_weight[idx_s][idx_e] = weight_

    dct_trap = {each_ - 1: 2 ** idx_ for each_, idx_ in zip(lst_trap, range(len(lst_trap)))}
    lst_d = [[INF_ for _ in range(2 ** len(lst_trap))] for _ in range(N_)]
    lst_d[0][S_] = 0
    hqu_ = [(0, S_, 0)]

    while hqu_:
        curr_state, curr_idx, curr_dist = hq.heappop(hqu_)
        if curr_idx in dct_trap:
            curr_state ^= dct_trap[curr_idx]
            for idx_ in range(N_):


        for target_idx, weight_ in grp_[state_grp][curr_idx]:
            temp_dist = curr_dist + weight_
            if temp_dist < lst_d[target_idx][curr_state]:
                lst_d[idx_e][curr_state] = temp_dist
                hq.heappush(hqu_, (curr_state, target_idx, temp_dist))

    print(lst_d)
    return min(lst_d[E_])


print(solution(4, 1, 4, [[1, 2, 1], [3, 2, 1], [2, 4, 1]], [2, 3]))
