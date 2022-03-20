import sys

N_ = int(sys.stdin.readline())
A_, B_ = map(int, sys.stdin.readline().split())

min_, max_ = min(A_, B_), max(A_, B_)

if min_ > (N_ - 1) * N_ // 2:
    print(-1)
else:
    mag_ = 1
    while min_ > mag_:
        min_ -= mag_
        mag_ += 1
    if mag_ + A_ + B_ >= N_ * N_:
        print(-1)
    else:
        print(1)
        grd_ = [[0 for _ in range(N_)] for _ in range(N_)]

        cnt_a = A_
        for num_ in range(N_ + N_ - 1):
            is_run = True
            for idx_c in range(N_):
                idx_r = num_ - idx_c
                if 0 <= idx_r < N_:
                    grd_[idx_r][idx_c] = 1
                    cnt_a -= 1
                    if not cnt_a:
                        is_run = False
                        break
            if not is_run:
                break

        cnt_b = B_
        for num_ in range(N_ + N_ - 1, -1, -1):
            is_run = True
            for idx_c in range(N_ - 1, -1, -1):
                idx_r = num_ - idx_c
                if 0 <= idx_r < N_:
                    grd_[idx_r][idx_c] = 2
                    cnt_b -= 1
                    if not cnt_b:
                        is_run = False
                        break
            if not is_run:
                break

        for idx_r in range(N_):
            print(''.join(map(str, grd_[idx_r])))

exit()
#
# idx_r_s = 0
# idx_r = idx_r_s
# idx_c = 0
# for _ in range(A_):
#     grd_[idx_r][idx_c] = 1
#     idx_r -= 1
#     if idx_r < 0:
#         idx_r_s += 1
#         idx_r = idx_r_s
#         idx_c = 0
#     else:
#         idx_c += 1
#
# idx_r_s = N_ - 1
# idx_r = idx_r_s
# idx_c = N_ - 1
# for _ in range(B_):
#     grd_[idx_r][idx_c] = 1
#     idx_r += 1
#     if idx_r >= N_:
#         idx_r_s -= 1
#
# A_, B_ = min(A_, B_), max(A_, B_)
#


exit()
