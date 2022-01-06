def solution(N_):
    grd_ = [[0 for _ in range(cnt_)] for cnt_ in range(1, N_ + 1)]

    cnt_ = 1
    temp_ = (N_ * (N_ + 1)) // 2
    target_ = N_ - 1
    idx_r = 0
    offset_ = 0
    while cnt_ < temp_:
        for _ in range(target_):
            grd_[idx_r][offset_] = cnt_
            idx_r += 1
            cnt_ += 1
        for idx_c in range(offset_, offset_ + target_):
            grd_[idx_r][idx_c] = cnt_
            cnt_ += 1
        for _ in range(target_):
            grd_[idx_r][-offset_ - 1] = cnt_
            idx_r -= 1
            cnt_ += 1
        target_ -= 3
        offset_ += 1
        idx_r += 2
    if cnt_ <= temp_:
        grd_[idx_r][offset_] = cnt_

    lst_answer = []
    for each_lst in grd_:
        print(each_lst)
        lst_answer += each_lst
    print()
    return lst_answer


print(solution(7))
