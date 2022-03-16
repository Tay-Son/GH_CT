def solution(grd_land, P_, Q_):
    N_ = len(grd_land) ** 2
    lst_ = []
    for each_lst in grd_land:
        lst_.extend(each_lst)
    lst_.sort()

    lst_sum = sum(lst_)
    min_ = lst_sum * Q_
    temp_ = (lst_sum - lst_[0] * N_) * Q_
    min_ = min(min_, temp_)

    for idx_ in range(1, N_):
        if lst_[idx_] != lst_[idx_ - 1]:
            temp_ += (P_ * idx_ * (lst_[idx_] - lst_[idx_ - 1])) - (Q_ * (N_ - idx_) * (lst_[idx_] - lst_[idx_ - 1]))
            min_ = min(min_, temp_)

    return min_


print(solution([[4, 4, 3], [3, 2, 2], [2, 1, 0]], 5, 3))
