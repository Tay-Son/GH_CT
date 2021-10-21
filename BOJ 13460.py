import sys
import heapq as hq

R_, C_ = map(int, sys.stdin.readline().split())
grd_ = []
for idx_r in range(R_):
    lst_temp = []
    for idx_c, value_ in enumerate(map(int, sys.stdin.readline().split())):
        if value_ == '#':
            lst_temp.append(1)
        elif value_ == '.':
            lst_temp.append(0)
        elif value_ == 'B':
            r_b, c_b = idx_r, idx_c
        elif value_ == 'R':
            r_r, c_r = idx_r, idx_c
        elif value_ == 'O':
            lst_temp.append(-1)

min_ = 11
hqu_ = [(0, r_b, c_b, r_r, c_r, 0), (0, r_b, c_b, r_r, c_r, 1), (0, r_b, c_b, r_r, c_r, 2), (0, r_b, c_b, r_r, c_r, 3)]
while hqu_:
    depth_, r_b, c_b, r_r, c_r, com_ = hq.heappop(hqu_)
    if depth_ < min_:
        is_ = True

        if com_ == 0:
            if r_b == r_r:
                pass
            else:
                while r_b + 1 < R_ and not grd_[r_b + 1][c_b]:
                    r_b += 1
                    if grd_[r_b][c_b] == -1:
                        is_ = False
                        break
                if is_:
                    while r_r + 1 < R_ and not grd_[r_r + 1][c_r]:
                        r_r += 1
                        if grd_[r_r][c_r] == -1:
                            min_ = min(min_, depth_)
                            is_ = False
                            break
                
exit()
