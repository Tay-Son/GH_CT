def solution(str_):
    from itertools import product as pd
    set_ = set()
    for pd_ in pd(list(' AEIOU'), repeat=5):
        target_ = ''.join(''.join(pd_).split())
        if target_:
            set_.add(target_)
    lst_ = sorted(list(set_))
    print(lst_)
    return lst_.index(str_) + 1


print(solution("AAAAE"))
