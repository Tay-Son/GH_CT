def solution(grd_):
    N_ = len(grd_)
    M_ = len(grd_[0])

    lst_offsets = [(1, 0), (0, -1), (-1, 0), (0, 1)]
    grd_vi = [[[False for _ in range(4)] for _ in range(M_)] for _ in range(N_)]

    lst_ = []
    for idx_n in range(N_):
        for idx_m in range(M_):
            for idx_d in range(4):
                set_ = set()
                if not grd_vi[idx_n][idx_m][idx_d]:
                    curr_n = idx_n
                    curr_m = idx_m
                    curr_d = idx_d
                    tot_ = 0
                    while True:
                        tot_ += 1
                        set_.add((curr_n, curr_m, curr_d))
                        offset_n, offset_m = lst_offsets[curr_d]
                        curr_n = (curr_n + offset_n) % N_
                        curr_m = (curr_m + offset_m) % M_
                        if grd_[curr_n][curr_m] == 'L':
                            curr_d = (curr_d + 1) % 4
                        elif grd_[curr_n][curr_m] == 'R':
                            curr_d = (curr_d - 1) % 4

                        if grd_vi[curr_n][curr_m][curr_d]:
                            break

                        if curr_n == idx_n and curr_m == idx_m and curr_d == idx_d:
                            lst_.append(tot_)
                            for n_, m_, d_ in set_:
                                grd_vi[n_][m_][d_] = True

    return sorted(lst_)


print(solution(["SL", "LR"]))
