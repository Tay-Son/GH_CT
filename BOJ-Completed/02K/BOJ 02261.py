import sys

sys.setrecursionlimit(10 ** 5)

N_ = int(sys.stdin.readline())
lst_ = []

for _ in range(N_):
    pos_x, pos_y = map(int, sys.stdin.readline().split())
    lst_.append((pos_x, pos_y))
lst_.sort()


def func(idx_s, idx_e):
    min_ = 20000 * 20000 * 2

    idx_c = (idx_s + idx_e) // 2
    if idx_s + 1 < idx_c:
        min_ = min(min_, func(idx_s, idx_c))
    if idx_c + 1 < idx_e:
        min_ = min(min_, func(idx_c, idx_e))

    x_c = lst_[idx_c][0]
    for idx_l in range(idx_c - 1, idx_s - 1, -1):
        x_l, y_l = lst_[idx_l]
        if (x_c - x_l) ** 2 >= min_:
            break
        for idx_r in range(idx_c, idx_e):
            x_r, y_r = lst_[idx_r]
            diff_x_sq = (x_r - x_l) ** 2
            if diff_x_sq >= min_:
                break
            diff_y_sq = (y_r - y_l) ** 2
            min_ = min(min_, diff_x_sq + diff_y_sq)

    return min_


print(func(0, N_))

exit()
