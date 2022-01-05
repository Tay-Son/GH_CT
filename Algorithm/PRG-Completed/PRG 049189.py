def solution(N_, lst_edge):
    grp_ = [[] for _ in range(N_ + 1)]
    for each_edge in lst_edge:
        idx_a, idx_b = each_edge
        grp_[idx_a].append(idx_b)
        grp_[idx_b].append(idx_a)

    lst_is_visited = [False for _ in range(N_ + 1)]
    dct_ = dict()

    que_ = [(1, 0)]
    lst_is_visited[1] = True
    ptr_que = 0
    while que_ and ptr_que < len(que_):
        idx_s, depth_ = que_[ptr_que]
        if depth_ not in dct_:
            dct_[depth_] = 1
        else:
            dct_[depth_] += 1
        depth_ += 1
        for idx_e in grp_[idx_s]:
            if not lst_is_visited[idx_e]:
                que_.append((idx_e, depth_))
                lst_is_visited[idx_e] = True
        ptr_que += 1

    return sorted(dct_.items(), reverse=True)[0][1]