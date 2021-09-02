def solution(N_, lst_path, lst_order):
    set_path = set()
    set_order = set(range(N_))

    grp_path = [[] for _ in range(N_)]
    for idx_a, idx_b in lst_path:
        grp_path[idx_a].append(idx_b)
        grp_path[idx_b].append(idx_a)

    grp_order = [[] for _ in range(N_)]
    for cond_, target_ in lst_order:
        set_order.remove(target_)
        grp_order[cond_].append(target_)

    que_ = []
    if 0 in set_order:
        que_.append(0)
    ptr_que = 0
    lst_vi = [False for _ in range(N_)]
    while ptr_que < len(que_):
        idx_s = que_[ptr_que]
        lst_vi[idx_s] = True
        for idx_t in grp_order[idx_s]:
            set_order.add(idx_t)
            if idx_t in set_path:
                que_.append(idx_t)

        for idx_e in grp_path[idx_s]:
            if not lst_vi[idx_e]:
                set_path.add(idx_e)
                if idx_e in set_order:
                    que_.append(idx_e)

        ptr_que += 1

    return True if ptr_que == N_ else False

print(solution(9,
               [[0, 1], [0, 3], [0, 7], [8, 1], [3, 6], [1, 2], [4, 7], [7, 5]],
               [[4, 1], [8, 7], [6, 5]]))
