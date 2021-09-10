def solution(lst_number):
    set_ = set(lst_number)
    tot_ = 0
    for num_ in range(1, 10):
        if num_ not in set_:
            tot_ += num_
    return tot_
