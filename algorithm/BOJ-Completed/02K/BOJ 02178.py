import sys

N_, M_ = map(int, sys.stdin.readline().split())
grd_ = []
for _ in range(N_):
    grd_.append(list(map(lambda x: int(x) ^ 1, list(sys.stdin.readline().strip()))))

lst_aux = [(0, 1), (0, -1), (1, 0), (-1, 0)]

grd_[0][0] = 1
que_ = [(0, 0)]
ptr_que = 0

while ptr_que < len(que_):
    idx_curr_y, idx_curr_x = que_[ptr_que]
    depth_ = grd_[idx_curr_y][idx_curr_x] + 1

    for aux_y, aux_x in lst_aux:
        idx_target_y, idx_target_x = idx_curr_y + aux_y, idx_curr_x + aux_x
        if 0 <= idx_target_y < N_ and 0 <= idx_target_x < M_ and not grd_[idx_target_y][idx_target_x]:
            grd_[idx_target_y][idx_target_x] = depth_
            que_.append((idx_target_y, idx_target_x))
    ptr_que += 1

print(grd_[N_ - 1][M_ - 1])

exit()
