def solution(mat_):
    N_ = len(mat_)

    def rec_(idx_s_r, idx_s_c, N_):
        tot_ = 0
        for idx_r in range(idx_s_r, idx_s_r + N_):
            for idx_c in range(idx_s_c, idx_s_c + N_):
                tot_ += mat_[idx_r][idx_c]
        if not tot_:
            return [1, 0]
        elif tot_ == N_ * N_:
            return [0, 1]
        else:
            lst_answer = [0, 0]
            N_ //= 2
            for mag_r in range(2):
                for mag_c in range(2):
                    lst_temp = rec_(idx_s_r + N_ * mag_r, idx_s_c + N_ * mag_c, N_)
                    lst_answer[0] += lst_temp[0]
                    lst_answer[1] += lst_temp[1]

            return lst_answer

    return rec_(0, 0, N_)


print(solution([[1, 1, 1, 1, 1, 1, 1, 1],
                [0, 1, 1, 1, 1, 1, 1, 1],
                [0, 0, 0, 0, 1, 1, 1, 1],
                [0, 1, 0, 0, 1, 1, 1, 1],
                [0, 0, 0, 0, 0, 0, 1, 1],
                [0, 0, 0, 0, 0, 0, 0, 1],
                [0, 0, 0, 0, 1, 0, 0, 1],
                [0, 0, 0, 0, 1, 1, 1, 1]]))
