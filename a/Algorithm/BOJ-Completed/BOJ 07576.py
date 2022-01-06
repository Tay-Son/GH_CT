import sys

M_, N_ = map(int, sys.stdin.readline().split())
grd_ = []
que_ = []

cnt_ = N_ * M_
for idx_n in range(N_):
    lst_temp = list(map(int, sys.stdin.readline().split()))
    for idx_m in range(M_):
        temp_ = lst_temp[idx_m]
        if temp_ != 0:
            cnt_ -= 1
            if temp_ == 1:
                que_.append((idx_n, idx_m))
    grd_.append(lst_temp)

lst_aux = [(0, 1), (0, -1), (1, 0), (-1, 0)]
ptr_que = 0
max_ = 1
while ptr_que < len(que_):
    idx_curr_y, idx_curr_x = que_[ptr_que]
    depth_ = grd_[idx_curr_y][idx_curr_x] + 1
    for aux_y, aux_x in lst_aux:
        idx_target_y, idx_target_x = idx_curr_y + aux_y, idx_curr_x + aux_x
        if 0 <= idx_target_y < N_ and 0 <= idx_target_x < M_ and not grd_[idx_target_y][idx_target_x]:
            grd_[idx_target_y][idx_target_x] = depth_
            max_ = max(max_, depth_)
            cnt_ -= 1
            que_.append((idx_target_y, idx_target_x))
    ptr_que += 1

if not cnt_:
    print(max_ - 1)
else:
    print(-1)

exit()
