def solution(N_, lst_road, K_):
    import heapq as hq
    INF_ = 1000000007

    grp_ = [[] for _ in range(N_ + 1)]
    for idx_a, idx_b, weight_ in lst_road:
        grp_[idx_a].append((idx_b, weight_))
        grp_[idx_b].append((idx_a, weight_))

    lst_d = [INF_ for _ in range(N_ + 1)]
    lst_d[1] = 0

    hqu_ = [(0, 1)]
    while hqu_:
        dist_, idx_s = hq.heappop(hqu_)
        for idx_e, weight_ in grp_[idx_s]:
            temp_ = dist_ + weight_
            if temp_ < lst_d[idx_e]:
                lst_d[idx_e] = temp_
                hq.heappush(hqu_, (temp_, idx_e))
    cnt_ = 0
    for dist_ in lst_d:
        if dist_ <= K_:
            cnt_ += 1
    return cnt_

