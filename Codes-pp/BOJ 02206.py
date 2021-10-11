import sys
import heapq as hq

INF_ = 1000000007

N_, M_ = map(int, sys.stdin.readline().split())
grd_ = []
for _ in range(N_):
    grd_.append(list(map(int, sys.stdin.readline().rstrip())))

grd_iv = [[0 for _ in range(M_)] for _ in range(N_)]
hqu_ = [(0, 0, 0)]
dct_ = dict()

while hqu_:
    depth_, c_r, c_c = hq.heappop(hqu_)
    depth_ += 1
    grd_iv[c_r][c_c] = depth_

    for o_r, o_c in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        t_r, t_c = c_r + o_r, c_c + o_c
        if 0 <= t_r < N_ and 0 <= t_c < M_ and not grd_iv[t_r][t_c]:
            if grd_[t_r][t_c]:
                dct_[(t_r, t_c)] = depth_
            else:
                hq.heappush(hqu_, (depth_, t_r, t_c))

if not grd_iv[N_-1][M_-1]:
    hqu_ = [(N_-1, M_-1, 0)]

    while hqu_:
        depth_, c_r, c_c = hq.heappop(hqu_)
        depth_ += 1
        grd_iv[c_r][c_c] = depth_

        for o_r, o_c in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            t_r, t_c = c_r + o_r, c_c + o_c
            if 0 <= t_r < N_ and 0 <= t_c < M_ and not grd_iv[t_r][t_c]:
                if grd_[t_r][t_c] and (t_r, t_c) in dct_:
                    dct_[(t_r, t_c)] += depth_
                else:
                    hq.heappush(hqu_, (depth_, t_r, t_c))

else:



if grd_iv[N_ - 1][M_ - 1] == INF_:
    print(-1)
else:
    print(grd_iv[N_ - 1][M_ - 1])

for each_ in grd_:
    print(each_)
print()

for each_ in grd_iv:
    print(each_)
print()

exit()
