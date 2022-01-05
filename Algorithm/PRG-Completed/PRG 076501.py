def solution(lst_absolute, lst_sign):
    tot_ = 0
    for absolute_, sign_ in zip(lst_absolute, lst_sign):
        tot_ += absolute_ * (1 if sign_ else -1)

    return tot_
