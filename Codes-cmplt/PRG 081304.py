def solution(N_, S_, E_, lst_grp, lst_trap):
    import heapq as hq
    INF_ = 100000009

    S_ -= 1
    E_ -= 1
    grp_c = [[] for _ in range(N_)]
    grp_r = [[] for _ in range(N_)]
    for idx_s, idx_e, weight_ in lst_grp:
        idx_s -= 1
        idx_e -= 1
        grp_c[idx_s].append((idx_e, weight_))
        grp_r[idx_e].append((idx_s, weight_))

    dct_trap = {each_ - 1: 2 ** idx_ for each_, idx_ in zip(lst_trap, range(len(lst_trap)))}
    lst_d = [[INF_ for _ in range(2 ** len(lst_trap))] for _ in range(N_)]
    lst_d[0][S_] = 0
    hqu_ = [(0, 0, S_)]

    while hqu_:
        curr_dist, curr_state, curr_idx = hq.heappop(hqu_)
        if curr_idx in dct_trap:
            curr_state ^= dct_trap[curr_idx]

        for target_idx, weight_ in grp_c[curr_idx]:

            if not ((curr_idx in dct_trap and bool(curr_state & dct_trap[curr_idx])) ^
                    (target_idx in dct_trap and bool(curr_state & dct_trap[target_idx]))):
                print(curr_idx, target_idx)
                temp_dist = curr_dist + weight_
                if temp_dist < lst_d[target_idx][curr_state]:
                    lst_d[target_idx][curr_state] = temp_dist
                    hq.heappush(hqu_, (temp_dist, curr_state, target_idx))

        for target_idx, weight_ in grp_r[curr_idx]:
            if ((curr_idx in dct_trap and bool(curr_state & dct_trap[curr_idx])) ^
                    (target_idx in dct_trap and bool(curr_state & dct_trap[target_idx]))):
                temp_dist = curr_dist + weight_
                if temp_dist < lst_d[target_idx][curr_state]:
                    lst_d[target_idx][curr_state] = temp_dist
                    hq.heappush(hqu_, (temp_dist, curr_state, target_idx))

    return min(lst_d[E_])


print(solution(4, 1, 4, [[1, 2, 1], [3, 2, 1], [2, 4, 1]], [2, 3]))
