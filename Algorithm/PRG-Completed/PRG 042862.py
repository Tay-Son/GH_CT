def solution(N_, lst_lost, lst_reserve):
    set_reserve = set(lst_reserve)
    set_lost = set(lst_lost)

    lst_lost = list(set_lost.difference(set_reserve))
    set_reserve = set_reserve.difference(set_lost)

    answer_ = N_ - len(lst_lost)
    for each_lost in lst_lost:
        if (each_lost + 1) <= N_ and (each_lost + 1) in set_reserve:
            set_reserve.remove(each_lost + 1)
            answer_ += 1
        elif (each_lost - 1) >= 1 and (each_lost - 1) in set_reserve:
            set_reserve.remove(each_lost - 1)
            answer_ += 1

    return answer_