import sys
from collections import deque

INF_ = 10000000

for _ in range(int(sys.stdin.readline())):
    C_, R_ = map(int, sys.stdin.readline().split())

    grd_ = []
    que_ = deque()
    for idx_r in range(R_):
        lst_temp = []
        for idx_c, value_ in enumerate(sys.stdin.readline().rstrip()):
            if value_ == '.':
                lst_temp.append(0)
            elif value_ == '*':
                lst_temp.append(0)
                que_.append((1, idx_r, idx_c))
            elif value_ == '#':
                lst_temp.append(-1)
            else:
                c_r, c_c = idx_r, idx_c
                lst_temp.append(0)
        grd_.append(lst_temp)

    ptr_que = 0
    while que_:
        depth_, idx_r, idx_c = que_.popleft()
        if not grd_[idx_r][idx_c]:
            grd_[idx_r][idx_c] = depth_
            depth_ += 1
            for o_r, o_c in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                t_r, t_c = idx_r + o_r, idx_c + o_c
                if 0 <= t_r < R_ and 0 <= t_c < C_ and not grd_[t_r][t_c]:
                    que_.append((depth_, t_r, t_c))

    for each_ in grd_:
        print(each_)

    grd_iv = [[False for _ in range(C_)] for _ in range(R_)]
    que_ = deque()
    que_.append((1, c_r, c_c))
    ptr_que = 0
    min_ = INF_
    while que_:
        depth_, idx_r, idx_c = que_.popleft()
        if not grd_iv[idx_r][idx_c]:
            if idx_r in [0, R_ - 1] or idx_c in [0, C_ - 1]:
                min_ = depth_
                break
            else:
                grd_iv[idx_r][idx_c] = True
                depth_ += 1
                for o_r, o_c in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    t_r, t_c = idx_r + o_r, idx_c + o_c
                    if (not grd_[t_r][t_c] or grd_[t_r][t_c] > depth_) and not grd_iv[t_r][t_c]:
                        que_.append((depth_, t_r, t_c))

    if min_ == INF_:
        print('IMPOSSIBLE')
    else:
        print(min_)
    print()
exit()
