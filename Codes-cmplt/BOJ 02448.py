import sys
import math

N_ = int(sys.stdin.readline())
C_ = int(math.log2(N_ // 3))
grd_ = [[' ' for _ in range(2 * N_ - 1)] for _ in range(N_)]


def rec_(idx_r, idx_c, level_):
    if level_ == 0:
        grd_[idx_r][idx_c + 2] = '*'
        grd_[idx_r + 1][idx_c + 1] = '*'
        grd_[idx_r + 1][idx_c + 3] = '*'
        grd_[idx_r + 2][idx_c] = '*'
        grd_[idx_r + 2][idx_c + 1] = '*'
        grd_[idx_r + 2][idx_c + 2] = '*'
        grd_[idx_r + 2][idx_c + 3] = '*'
        grd_[idx_r + 2][idx_c + 4] = '*'
    else:
        rec_(idx_r, idx_c + 3 * 2 ** (level_ - 1), level_ - 1)
        rec_(idx_r + 3 * 2 ** (level_ - 1), idx_c, level_ - 1)
        rec_(idx_r + 3 * 2 ** (level_ - 1), idx_c + 6 * 2 ** (level_ - 1), level_ - 1)


rec_(0, 0, C_)
print(C_)
for each_ in grd_:
    print(''.join(each_))

exit()
