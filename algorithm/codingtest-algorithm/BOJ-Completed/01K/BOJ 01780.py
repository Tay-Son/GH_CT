import sys

N = int(sys.stdin.readline())
grd_ = []
for _ in range(N):
    grd_.append(list(map(int, sys.stdin.readline().split())))


def func(x, y, n):
    if n == 1:
        if grd_[y][x] == -1:
            return [1, 0, 0]
        elif grd_[y][x] == 0:
            return [0, 1, 0]
        else:
            return [0, 0, 1]
    else:
        lst_cnt = [0, 0, 0]

        temp_n = n // 3
        for c_y in range(3):
            for c_x in range(3):
                lst_temp = func(x + c_x * temp_n, y + c_y * temp_n, temp_n)
                lst_cnt = [lst_cnt[i] + lst_temp[i] for i in range(3)]
        if sum(lst_cnt) == 9 and 9 in lst_cnt:
            return [lst_cnt[i] // 9 for i in range(3)]
        else:
            return lst_cnt


for each_ in func(0, 0, N):
    print(each_)