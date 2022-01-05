import sys

N_, M_ = map(int, sys.stdin.readline().split())
idx_r, idx_c, dir_ = map(int, sys.stdin.readline().split())

lst_d = [(-1, 0), (0, 1), (1, 0), (0, -1)]

grd_ = []
for idx_n in range(N_):
    lst_temp = list(map(int, sys.stdin.readline().split()))
    grd_.append(lst_temp)

cleaned_ = 0
is_run = True
while is_run:
    print(idx_r, idx_c, cleaned_)
    if grd_[idx_r][idx_c] == 0:
        grd_[idx_r][idx_c] = 2
        cleaned_ += 1

    is_c = False
    for o_ in range(1, 5):
        dir_c = (dir_ - o_) % 4

        o_r, o_c = lst_d[dir_c]
        t_r, t_c = idx_r + o_r, idx_c + o_c

        if 0 <= t_r < N_ and 0 <= t_c < M_ and not grd_[t_r][t_c]:
            idx_r, idx_c = t_r, t_c
            dir_ = dir_c
            is_c = True
            break

    if not is_c:
        o_r, o_c = lst_d[dir_]
        t_r, t_c = idx_r - o_r, idx_c - o_c

        if not (0 <= t_r < N_ and 0 <= t_c < M_):
            break
        else:
            if grd_[t_r][t_c] == 1:
                break
            else:
                idx_r = t_r
                idx_c = t_c

print(cleaned_)
for each_ in grd_:
    print(each_)
print()

exit()
