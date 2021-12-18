import sys
from copy import deepcopy
from collections import deque

R_, C_ = map(int, sys.stdin.readline().split())
grd_ = []
for _ in range(R_):
    grd_.append(list(map(int, sys.stdin.readline().split())))

ans_ = 0
for y_ in range(6000):
    grd_iv = deepcopy(grd_)
    cnt_ = 0
    for idx_r in range(R_):
        for idx_c in range(C_):
            if grd_iv[idx_r][idx_c]:
                cnt_ += 1
                if cnt_ > 1:
                    ans_ = y_
                    break
                else:
                    que_ = deque()
                    que_.append((idx_r, idx_c))
                    while que_:
                        i_r, i_c = que_.popleft()
                        if grd_iv[i_r][i_c]:
                            grd_iv[i_r][i_c] = 0
                            for o_r, o_c in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                                t_r = i_r + o_r
                                t_c = i_c + o_c
                                if 0 <= t_r < R_ and 0 <= t_c < C_ and grd_iv[t_r][t_c]:
                                    que_.append((t_r, t_c))
        if cnt_ > 1:
            break
    print(y_, cnt_)
    for each_ in grd_:
        print(each_)
    print()

    if cnt_ > 1:
        break
    else:
        grd_d = [[0 for _ in range(C_)] for _ in range(R_)]
        for idx_r in range(R_):
            for idx_c in range(C_):
                if grd_[idx_r][idx_c]:
                    for o_r, o_c in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                        t_r = idx_r + o_r
                        t_c = idx_c + o_c
                        if 0 <= t_r < R_ and 0 <= t_c < C_ and not grd_[t_r][t_c]:
                            grd_d[idx_r][idx_c] += 1
        for idx_r in range(R_):
            for idx_c in range(C_):
                grd_[idx_r][idx_c] = max(0, grd_[idx_r][idx_c] - grd_d[idx_r][idx_c])

    if not sum([sum(each_) for each_ in grd_]):
        break

        for each_ in grd_d:
            print(each_)
        print()

print(ans_)

exit()
