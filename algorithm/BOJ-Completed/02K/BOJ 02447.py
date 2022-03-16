import sys

N = int(sys.stdin.readline())

grd_ = [['*' for _ in range(N)] for _ in range(N)]


def func(x, y, n):
    temp_ = n // 3
    if n >= 3:
        for b_y in range(3):
            for b_x in range(3):
                if b_x == 1 and b_y == 1:
                    for idx_y in range(temp_ + y, 2 * temp_ + y):
                        for idx_x in range(temp_ + x, 2 * temp_ + x):
                            grd_[idx_y][idx_x] = ' '
                else:
                    func(x + b_x * temp_, y + b_y * temp_, temp_)


func(0, 0, N)

for each_ in grd_:
    print(''.join(each_))