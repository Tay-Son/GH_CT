import sys

M_, N_, H_ = map(int, sys.stdin.readline().split())

lst_aux = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]

cub_ = []
que_ = []
cnt_ = N_ * M_ * H_
for idx_h in range(H_):
    grd_temp = []
    for idx_n in range(N_):
        lst_temp = list(map(int, sys.stdin.readline().split()))
        for idx_m in range(M_):
            temp_ = lst_temp[idx_m]
            if temp_ != 0:
                cnt_ -= 1
                if lst_temp[idx_m] == 1:
                    que_.append((idx_h, idx_n, idx_m))
        grd_temp.append(lst_temp)
    cub_.append(grd_temp)

ptr_que = 0
max_ = 1
while ptr_que < len(que_):
    idx_c_h, idx_c_n, idx_c_m = que_[ptr_que]
    depth_ = cub_[idx_c_h][idx_c_n][idx_c_m] + 1
    for idx_a_h, idx_a_n, idx_a_m in lst_aux:
        idx_t_h, idx_t_n, idx_t_m = idx_c_h + idx_a_h, idx_c_n + idx_a_n, idx_c_m + idx_a_m
        if 0 <= idx_t_h < H_ and 0 <= idx_t_n < N_ and 0 <= idx_t_m < M_ and cub_[idx_t_h][idx_t_n][idx_t_m] == 0:
            max_ = max(max_, depth_)
            cnt_ -= 1
            cub_[idx_t_h][idx_t_n][idx_t_m] = depth_
            que_.append((idx_t_h, idx_t_n, idx_t_m))
    ptr_que += 1

if not cnt_:
    print(max_ - 1)
else:
    print(-1)

exit()
