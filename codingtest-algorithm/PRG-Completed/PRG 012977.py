def solution(lst_num):
    from itertools import combinations as cb

    lst_ = []
    for cb_ in cb(lst_num, 3):
        lst_.append(sum(cb_))

    set_prime = set()
    lst_is = [True for _ in range(max(lst_) + 1)]
    lst_is[0], lst_is[1] = False, False
    for idx_ in range(2, len(lst_is)):
        if lst_is[idx_]:
            set_prime.add(idx_)
            for idx_sub in range(idx_, len(lst_is), idx_):
                lst_is[idx_sub] = False
    tot_ = 0
    for cand_ in lst_:
        if cand_ in set_prime:
            tot_ += 1

    return tot_
