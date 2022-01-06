def solution(lst_weight, lst_edge):
    import sys
    sys.setrecursionlimit(300009)

    N_ = len(lst_weight)
    grp_ = [[] for _ in range(N_)]
    set_temp = set()
    for idx_a, idx_b in lst_edge:
        if idx_a in set_temp:
            set_temp.remove(idx_a)
        else:
            set_temp.add(idx_a)
        if idx_b in set_temp:
            set_temp.remove(idx_b)
        else:
            set_temp.add(idx_b)

        grp_[idx_a].append(idx_b)
        grp_[idx_b].append(idx_a)

    def rec_(idx_, idx_p):
        print(idx_, idx_p)
        rem_ = 0
        tot_ = 0
        for idx_c in grp_[idx_]:
            if idx_c != idx_p:
                rem_temp, tot_temp = rec_(idx_c, idx_)
                rem_ += rem_temp
                tot_ += tot_temp

        return lst_weight[idx_] + rem_, abs(lst_weight[idx_] + rem_) + tot_

    rem_, tot_ = rec_(set_temp.pop(), -1)

    return tot_ if rem_ == 0 else -1


print(solution([-5, 0, 2, 1, 2], [[0, 1], [3, 4], [2, 3], [0, 3]]))
