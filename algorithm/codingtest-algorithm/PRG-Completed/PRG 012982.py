def solution(lst_d, budget_):
    lst_d.sort()
    for idx_ in range(len(lst_d)):
        budget_ -= lst_d[idx_]
        if budget_ < 0:
            idx_ -= 1
            break

    return idx_ + 1
