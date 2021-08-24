def solution(N_):
    str_3 = ''
    while N_ > 2:
        N_, rem_ = divmod(N_, 3)
        str_3 = str(rem_) + str_3
    str_3 = str(N_) + str_3

    mag_ = 1
    tot_ = 0
    for each_ in str_3:
        tot_ += mag_ * int(each_)
        mag_ *= 3

    return tot_
