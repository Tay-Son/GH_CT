def solution(R_, C_, lst_query):
    grd_ = [[cnt_ + cnt_r * C_ + 1 for cnt_ in range(C_)] for cnt_r in range(R_)]
    for each_ in grd_:
        print(each_)
    print()

    lst_answer = []
    for idx_y1, idx_x1, idx_y2, idx_x2, in lst_query:
        idx_x1 -= 1
        idx_x2 -= 1
        idx_y1 -= 1
        idx_y2 -= 1

        min_ = R_ * C_
        val_temp = grd_[idx_y1][idx_x1]
        min_ = min(min_, val_temp)
        for idx_r in range(idx_y1, idx_y2):
            val_ = grd_[idx_r + 1][idx_x1]
            min_ = min(min_, val_)
            grd_[idx_r][idx_x1] = val_
        for idx_c in range(idx_x1, idx_x2):
            val_ = grd_[idx_y2][idx_c + 1]
            min_ = min(min_, val_)
            grd_[idx_y2][idx_c] = val_
        for idx_r in range(idx_y2, idx_y1, -1):
            val_ = grd_[idx_r - 1][idx_x2]
            min_ = min(min_, val_)
            grd_[idx_r][idx_x2] = val_
        for idx_c in range(idx_x2, idx_x1 + 1, -1):
            val_ = grd_[idx_y1][idx_c - 1]
            min_ = min(min_, val_)
            grd_[idx_y1][idx_c] = val_
        grd_[idx_y1][idx_x1 + 1] = val_temp
        lst_answer.append(min_)

        for each_ in grd_:
            print(each_)
        print()

    return lst_answer


print(solution(6, 6, [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]]))
