def solution(lst_):
    min_ = lst_[0]
    lst_temp = [False for _ in range(len(lst_))]
    for idx_ in range(1, len(lst_)):
        if lst_[idx_] < min_:
            min_ = lst_[idx_]
            lst_temp[idx_] = True
    cnt_ = len(lst_)
    min_ = lst_[-1]
    for idx_ in range(len(lst_) - 2, 0, -1):
        if lst_[idx_] < min_:
            min_ = lst_[idx_]
        elif not lst_temp[idx_]:
            cnt_ -= 1

    return cnt_


print(solution([-16, 27, 65, -2, 58, -92, -71, -68, -61, -33]))

-16, -92, -71, -68, -61, -33
