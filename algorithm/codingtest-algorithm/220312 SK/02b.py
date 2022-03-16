def solution(n_, is_c):
    grd_ = [[0 for _ in range(n_)] for _ in range(n_)]
    a_, b_, c_, d_ = 0, 0, 0, (0 if is_c else 2)

    lst_offset = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    for _ in range(n_ * n_ // 4):
        c_ += 1

        # print(a_, b_, c_)

        grd_[a_][b_] = c_
        grd_[n_ - b_ - 1][a_] = c_
        grd_[n_ - a_ - 1][n_ - b_ - 1] = c_
        grd_[b_][n_ - a_ - 1] = c_

        offset_a, offset_b = lst_offset[d_]
        temp_a = a_ + offset_a
        temp_b = b_ + offset_b

        if 0 <= temp_a < n_ and 0 <= temp_b < n_ and not grd_[temp_a][temp_b]:
            a_ = temp_a
            b_ = temp_b
        else:
            if is_c:
                d_ = (d_ + 1) % 4
            else:
                d_ = (d_ - 1) % 4
            offset_a, offset_b = lst_offset[d_]
            a_ += offset_a
            b_ += offset_b

    if n_ % 2:
        c_ += 1
        grd_[a_][b_] = c_

    return grd_


import time

time_s = time.time()

for n_, is_c in [
    (5, True),
    (6, False),
    (9, True),
    (1000, True)
]:
    for each_ in solution(n_, is_c):
        # print(each_)
        pass
    print()
print(time.time() - time_s)
