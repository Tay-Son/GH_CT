import sys

R_, C_ = map(int, input().split())

grd_ = [list(sys.stdin.readline()) for _ in range(R_)]
grd_iv = [[set() for _ in range(C_)] for _ in range(R_)]

stk_ = [(0, 0, 1, grd_[0][0])]
max_ = 0
while stk_:
    curr_r, curr_c, depth_, route_ = stk_.pop()
    max_ = max(max_, depth_)
    if max_ < 26:
        depth_ += 1
        for offset_r, offset_c in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            target_r = curr_r + offset_r
            target_c = curr_c + offset_c

            if 0 <= target_r < R_ and 0 <= target_c < C_:
                if grd_[target_r][target_c] not in route_:
                    temp_ = route_ + grd_[target_r][target_c]
                    if grd_iv[target_r][target_c] != temp_:
                        grd_iv[target_r][target_c] = temp_
                        stk_.append((target_r, target_c, depth_, temp_))
print(max_)
exit()
