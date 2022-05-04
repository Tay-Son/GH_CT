def solution(N_, lst_wire):
    grp_ = [[] for _ in range(N_)]

    for wire_ in lst_wire:
        a_, b_ = wire_
        a_, b_ = a_ - 1, b_ - 1
        grp_[a_].append(b_)
        grp_[b_].append(a_)

    lst_iv = [False for _ in range(N_)]

    def rec_(idx_):
        min_ = N_
        lst_iv[idx_] = True
        tot_ = 1
        for idx_t in grp_[idx_]:
            if not lst_iv[idx_t]:
                tot_c, min_c = rec_(idx_t)
                tot_ += tot_c
                min_ = min(min_, min_c)
        min_ = min(min_, abs(N_ - 2 * tot_))
        print(idx_, tot_, min_)
        return tot_, min_

    return rec_(0)[1]
