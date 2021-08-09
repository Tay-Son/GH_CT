import sys
from collections import deque

lst_dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]

N_ = int(sys.stdin.readline())
grd_ = [[1 for _ in range(N_ + 2)]] + \
       [[1] + [0 for _ in range(N_)] + [1] for _ in range(N_)] + \
       [[1 for _ in range(N_ + 2)]]

for _ in range(int(sys.stdin.readline())):
    idx_a, idx_b = map(int, sys.stdin.readline().split())
    grd_[idx_a][idx_b] = 2

deq_ = deque()
idx_curr_y = 1
idx_curr_x = 1
grd_[idx_curr_y][idx_curr_x] = 1
deq_.append((idx_curr_y, idx_curr_x))
cnt_mov = 0
cnt_dir = 0

is_ = True
for _ in range(int(sys.stdin.readline())):
    lst_input = sys.stdin.readline().split()
    t_ = int(lst_input[0])
    d_ = -1 if lst_input[1] == 'L' else 1
    if is_:
        while cnt_mov < t_:
            cnt_mov += 1
            idx_target_y = idx_curr_y + lst_dir[cnt_dir % 4][0]
            idx_target_x = idx_curr_x + lst_dir[cnt_dir % 4][1]
            temp_ = grd_[idx_target_y][idx_target_x]
            if temp_ != 1:
                idx_curr_y = idx_target_y
                idx_curr_x = idx_target_x
                grd_[idx_curr_y][idx_curr_x] = 1
                deq_.append((idx_curr_y, idx_curr_x))
                if temp_ != 2:
                    idx_temp_y, idx_temp_x = deq_.popleft()
                    grd_[idx_temp_y][idx_temp_x] = 0
            else:
                is_ = False
                break
        cnt_dir += d_

while is_:
    cnt_mov += 1
    idx_target_y = idx_curr_y + lst_dir[cnt_dir % 4][0]
    idx_target_x = idx_curr_x + lst_dir[cnt_dir % 4][1]
    temp_ = grd_[idx_target_y][idx_target_x]
    if temp_ != 1:
        idx_curr_y = idx_target_y
        idx_curr_x = idx_target_x
        grd_[idx_curr_y][idx_curr_x] = 1
        deq_.append((idx_curr_y, idx_curr_x))
        if temp_ != 2:
            idx_temp_y, idx_temp_x = deq_.popleft()
            grd_[idx_temp_y][idx_temp_x] = 0
    else:
        is_ = False
        break

print(cnt_mov)

exit()
