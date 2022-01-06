def solution(N_, lst_station, W_):
    import math
    ptr_ = 1
    tot_ = 0
    c_ = W_ * 2 + 1
    for station_ in lst_station:
        temp_ = station_ - W_
        if temp_ > ptr_:
            tot_ += math.ceil((temp_ - ptr_) / c_)
        ptr_ = station_ + W_ + 1
    tot_ += math.ceil((N_ - ptr_ + 1) / c_)

    return tot_


print(solution(11, [4, 11], 1))
