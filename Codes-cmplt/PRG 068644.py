def solution(lst_number):
    from itertools import combinations as cb
    set_ = set()
    for cb_ in cb(lst_number, 2):
        set_.add(sum(cb_))
    return sorted(list(set_))
