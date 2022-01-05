import sys

sys.setrecursionlimit(100000)

val_N = int(sys.stdin.readline())

grd_nm = []
grd_cb = []
for _ in range(val_N):
    lst_input = list(sys.stdin.readline()[:-1])
    grd_nm.append(lst_input)
    lst_temp = []
    for idx_ in range(val_N):
        if lst_input[idx_] == 'B':
            lst_temp.append('B')
        else:
            lst_temp.append('T')
    grd_cb.append(lst_temp)


def func(grd_, idx_x, idx_y):
    curr_ = grd_[idx_y][idx_x]
    grd_[idx_y][idx_x] = 'V'
    if idx_x < val_N - 1 and grd_[idx_y][idx_x + 1] == curr_:
        func(grd_, idx_x + 1, idx_y)
    if idx_y < val_N - 1 and grd_[idx_y + 1][idx_x] == curr_:
        func(grd_, idx_x, idx_y + 1)
    if 0 < idx_x and grd_[idx_y][idx_x - 1] == curr_:
        func(grd_, idx_x - 1, idx_y)
    if 0 < idx_y and grd_[idx_y - 1][idx_x] == curr_:
        func(grd_, idx_x, idx_y - 1)


cnt_nm = 0
cnt_cb = 0

for idx_y in range(val_N):
    for idx_x in range(val_N):
        if not grd_nm[idx_y][idx_x] == 'V':
            cnt_nm += 1
            func(grd_nm, idx_x, idx_y)
        if not grd_cb[idx_y][idx_x] == 'V':
            cnt_cb += 1
            func(grd_cb, idx_x, idx_y)
print(' '.join([str(cnt_nm), str(cnt_cb)]))