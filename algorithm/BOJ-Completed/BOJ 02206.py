import sys
from collections import deque

INF_ = 100000007

R_, C_ = map(int, sys.stdin.readline().split())

grd_ = []
for _ in range(R_):
    grd_.append(list(map(int, sys.stdin.readline().strip())))

grd_depth = [[[INF_, INF_] for _ in range(C_)] for _ in range(R_)]
deq_ = deque([(0, 0, 0, 0)])

while deq_:

    depth_, is_b, c_r, c_c = deq_.popleft()
    depth_ += 1
    if depth_ < grd_depth[c_r][c_c][is_b]:
        grd_depth[c_r][c_c][is_b] = depth_
        for o_r, o_c in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            t_r, t_c = c_r + o_r, c_c + o_c
            if 0 <= t_r < R_ and 0 <= t_c < C_:
                if grd_[t_r][t_c]:
                    if not is_b:
                        deq_.append((depth_, is_b + 1, t_r, t_c))
                else:
                    deq_.append((depth_, is_b, t_r, t_c))

temp_ = min(grd_depth[R_ - 1][C_ - 1])
if temp_ == INF_:
    print(-1)
else:
    print(temp_)

exit()
