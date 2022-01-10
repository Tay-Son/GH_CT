import sys
import heapq as hq

R_, C_ = map(int, sys.stdin.readline().split())
grd_ = []
for _ in range(R_):
    grd_.append(list(map(lambda x: int(x) * 2, sys.stdin.readline().split())))

hqu_ = [(0, 0, 0)]

while hqu_:
    depth_, c_r, c_c = hq.heappop(hqu_)
    for o_r, o_c in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
        t_r, t_c = c_r + o_r, c_c + o_c
        if 0 <= t_r < R_ and 0 <= t_c < C_:
            if grd_[t_r][t_c] == 0:
                grd_[t_r][t_c] -= 1
                hq.heappush(hqu_, (depth_, t_r, t_c))
            elif grd_[t_r][t_c] == 1:
                grd_[t_r][t_c] -= 2
                hq.heappush(hqu_, (depth_ + 1, t_r, t_c))
            elif grd_[t_r][t_c] == 2:
                grd_[t_r][t_c] -= 1

print(depth_)
exit()
