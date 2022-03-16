import sys
from collections import deque

for _ in range(int(sys.stdin.readline())):
    I_ = int(sys.stdin.readline())

    c_r, c_c = map(int, sys.stdin.readline().split())
    d_r, d_c = map(int, sys.stdin.readline().split())
    deq_ = deque()
    deq_.append((c_r, c_c, 0))
    grd_iv = [[False for _ in range(I_)] for _ in range(I_)]
    while deq_:
        c_r, c_c, dist_ = deq_.popleft()
        if not grd_iv[c_r][c_c]:
            grd_iv[c_r][c_c] = True
            if c_r == d_r and c_c == d_c:
                break
            else:
                dist_ += 1
                for o_r, o_c in [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]:
                    t_r, t_c = c_r + o_r, c_c + o_c
                    if 0 <= t_r < I_ and 0 <= t_c < I_:
                        deq_.append((t_r, t_c, dist_))
    print(dist_)
exit()
