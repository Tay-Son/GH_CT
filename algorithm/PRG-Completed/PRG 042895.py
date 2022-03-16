def solution(N_, T_):
    answer_ = -1
    lst_dp = []

    for idx_ in range(1, 9):
        set_ = set()
        set_.add(int(str(N_) * idx_))
        for idx_sub in range(idx_ - 1):
            for a_ in lst_dp[idx_sub]:
                for b_ in lst_dp[-idx_sub - 1]:
                    set_.add(a_ + b_)
                    set_.add(a_ - b_)
                    set_.add(a_ * b_)

                    if b_:
                        set_.add(a_ // b_)
        if T_ in set_:
            answer_ = idx_
            break
        lst_dp.append(set_)
    return answer_
