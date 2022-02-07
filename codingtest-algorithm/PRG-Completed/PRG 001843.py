def lin_(lst_, grd_, idx_s, idx_e):
    if grd_[idx_s][idx_e] == -1:
        min_ = 100000
        max_ = -100000
        for idx_c in range(idx_s, idx_e):
            min_a, max_a = lin_(lst_, grd_, idx_s, idx_c)
            min_b, max_b = lin_(lst_, grd_, idx_c + 1, idx_e)
            if lst_[idx_c + 1] >= 0:
                max_ = max(max_, max_a + max_b)
                min_ = min(min_, min_a + min_b)
            else:
                max_ = max(max_, max_a - min_b)
                min_ = min(min_, min_a - max_b)
        grd_[idx_s][idx_e] = [min_, max_]
    return grd_[idx_s][idx_e]


def solution(lst_):
    lst_num = [int(lst_[0])]
    for o_, v_ in zip(lst_[1::2], lst_[2::2]):
        lst_num.append(int(v_) * (1 if o_ == '+' else -1))
    lst_ = lst_num
    grd_d = [[-1 for _ in range(len(lst_))] for _ in range(len(lst_))]
    for idx_, val_ in enumerate(lst_):
        grd_d[idx_][idx_] = [abs(val_), abs(val_)]
    return lin_(lst_, grd_d, 0, len(lst_num) - 1)[1]