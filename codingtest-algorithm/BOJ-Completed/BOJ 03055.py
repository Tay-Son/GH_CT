import sys
from collections import deque

INF_ = 2501
R_, C_ = map(int, sys.stdin.readline().split())

que_ = deque()
grd_ = []
for idx_r in range(R_):
    lst_temp = []
    for idx_c, chr_ in enumerate(sys.stdin.readline().rstrip()):
        if chr_ == 'S':
            s_r = idx_r
            s_c = idx_c
            lst_temp.append(INF_)
        elif chr_ == 'D':
            d_r = idx_r
            d_c = idx_c
            lst_temp.append(INF_ + 1)
        elif chr_ == 'X':
            lst_temp.append(-1)
        elif chr_ == '*':
            que_.append((idx_r, idx_c, 0))
            lst_temp.append(INF_)
        else:
            lst_temp.append(INF_)
    grd_.append(lst_temp)

while que_:
    idx_r, idx_c, depth_ = que_.popleft()
    if grd_[idx_r][idx_c] == INF_:
        grd_[idx_r][idx_c] = depth_
        depth_ += 1
        for o_r, o_c in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            t_r = o_r + idx_r
            t_c = o_c + idx_c
            if 0 <= t_r < R_ and 0 <= t_c < C_ and not grd_[t_r][t_c] == -1:
                que_.append((t_r, t_c, depth_))

que_ = deque()
que_.append((s_r, s_c, 0))
grd_iv = [[False for _ in range(C_)] for _ in range(R_)]
is_ = False
while que_:
    idx_r, idx_c, depth_ = que_.popleft()
    if not grd_iv[idx_r][idx_c]:
        if idx_r == d_r and idx_c == d_c:
            is_ = True
            break
        else:

            grd_iv[idx_r][idx_c] = True
            depth_ += 1
            for o_r, o_c in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                t_r = o_r + idx_r
                t_c = o_c + idx_c
                if 0 <= t_r < R_ and 0 <= t_c < C_ and depth_ < grd_[t_r][t_c]:
                    que_.append((t_r, t_c, depth_))

if is_:
    print(depth_)
else:
    print('KAKTUS')

exit()
