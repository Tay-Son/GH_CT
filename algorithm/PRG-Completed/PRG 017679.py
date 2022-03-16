def solution(M_, N_, lst_board):
    grd_ = [[] for _ in range(N_)]
    for idx_m in range(M_ - 1, -1, -1):
        for idx_n in range(N_):
            grd_[idx_n].append(lst_board[idx_m][idx_n])

    tot_ = 0
    is_run = True
    while is_run:
        for each_ in grd_:
            print(each_)
        print()

        is_run = False
        grd_is = [[False for _ in range(M_)] for _ in range(N_)]
        for idx_m in range(M_ - 1):
            for idx_n in range(N_ - 1):
                if grd_[idx_n][idx_m] != -2 and \
                        grd_[idx_n][idx_m] == \
                        grd_[idx_n + 1][idx_m] == \
                        grd_[idx_n][idx_m + 1] == \
                        grd_[idx_n + 1][idx_m + 1]:
                    is_run = True
                    grd_is[idx_n][idx_m] = True
                    grd_is[idx_n + 1][idx_m] = True
                    grd_is[idx_n][idx_m + 1] = True
                    grd_is[idx_n + 1][idx_m + 1] = True
        for idx_m in range(M_):
            for idx_n in range(N_):
                if grd_is[idx_n][idx_m]:
                    grd_[idx_n][idx_m] = -1
        for idx_n in range(N_):
            ptr_m = 0
            cnt_ = 0
            while ptr_m < len(grd_[idx_n]):
                if grd_[idx_n][ptr_m] == -1:
                    del (grd_[idx_n][ptr_m])
                    tot_ += 1
                    cnt_ += 1
                else:
                    ptr_m += 1
            grd_[idx_n].extend([-2] * cnt_)

    return tot_


print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))
