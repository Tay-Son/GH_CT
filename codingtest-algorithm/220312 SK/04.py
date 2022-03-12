from itertools import combinations


def solution(N_, lst_edge):
    lst_c = [0 for _ in range(N_)]

    grp_ = [[] for _ in range(N_)]
    for idx_a, idx_b in lst_edge:
        grp_[idx_a].append(idx_b)
        grp_[idx_b].append(idx_a)

    def rec_(idx_p, idx_):
        lst_ = []
        for idx_c in grp_[idx_]:
            if idx_c != idx_p:
                lst_.append(rec_(idx_, idx_c))

        if idx_p != -1:
            lst_.append(N_ - sum(lst_) - 1)

        # print(idx_p, idx_, lst_)

        for val_a, val_b in combinations(lst_, 2):
            lst_c[idx_] += val_a * val_b * 2
        return sum(lst_[:-1]) + 1

    print(rec_(-1, 0))

    return sum(lst_c)


import time

N_c = 300000
lst_c = [[idx_//2, idx_] for idx_ in range(1, N_c)]

time_s = time.time()
for N_, lst_edge in [
    (5, [[0, 1], [0, 2], [1, 3], [1, 4]]),
    (4, [[2, 3], [0, 1], [1, 2]]),
    (5, [[0, 1], [0, 2], [0, 3], [0, 4]]),
    (5, [[0, 1], [1, 2], [2, 3], [3, 4]]),
    [N_c, lst_c]
]:
    print(solution(N_, lst_edge))
    print()
print(time.time() - time_s)
