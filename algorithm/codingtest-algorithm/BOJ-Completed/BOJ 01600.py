import sys
from collections import deque

INF_ = 40001

K_ = int(sys.stdin.readline())
C_, R_ = map(int, sys.stdin.readline().split())
grd_ = []
for _ in range(R_):
    grd_.append(list(map(int, sys.stdin.readline().split())))

grd_iv = [[[True for _ in range(K_ + 1)] if grd_[idx_r][idx_c] else [False for _ in range(K_ + 1)]
           for idx_c in range(C_)] for idx_r in range(R_)]
que_ = deque()
que_.append((0, 0, K_, 0))
grd_iv[0][0][K_] = True

min_ = INF_

while que_:
    i_r, i_c, K_, depth_ = que_.popleft()

    grd_iv[i_r][i_c][K_] = True
    if i_r == R_ - 1 and i_c == C_ - 1:
        min_ = depth_
        break
    else:
        depth_ += 1
        if K_:
            for o_r, o_c in [[1, 2], [1, -2], [-1, 2], [-1, -2], [2, 1], [-2, 1], [2, -1], [-2, -1]]:
                t_r, t_c = i_r + o_r, i_c + o_c
                if 0 <= t_r < R_ and 0 <= t_c < C_ and not grd_iv[t_r][t_c][K_ - 1]:
                    grd_iv[t_r][t_c][K_ - 1] = True
                    que_.append((t_r, t_c, K_ - 1, depth_))

        for o_r, o_c in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            t_r, t_c = i_r + o_r, i_c + o_c
            if 0 <= t_r < R_ and 0 <= t_c < C_ and not grd_iv[t_r][t_c][K_]:
                grd_iv[t_r][t_c][K_] = True
                que_.append((t_r, t_c, K_, depth_))

if min_ != INF_:
    print(min_)
else:
    print(-1)

exit()
