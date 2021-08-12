import sys

MAX_ = 10 ** 5 + 1

N_, K_ = map(int, sys.stdin.readline().split())
if N_ >= K_:
    print(N_ - K_)
else:
    lst_depth = [-1 for _ in range(MAX_)]
    lst_depth[N_] = 0
    que_ = [N_]
    ptr_que = 0
    while ptr_que < len(que_):
        idx_curr = que_[ptr_que]
        depth_ = lst_depth[idx_curr]
        if idx_curr == K_:
            print(depth_)
            break
        else:
            depth_ += 1
            lst_temp = [idx_curr * 2, idx_curr - 1, idx_curr + 1]
            for idx_target in lst_temp:
                if 0 <= idx_target < MAX_ and lst_depth[idx_target] == -1:
                    lst_depth[idx_target] = depth_
                    que_.append(idx_target)
            ptr_que += 1
exit()