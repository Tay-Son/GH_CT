import sys
import heapq as hq

que_x = []
for _ in range(int(sys.stdin.readline())):
    x_origin, y_origin, x_offset, y_offset = map(float, sys.stdin.readline().split())
    x_end = x_origin + x_offset
    y_end = y_origin + y_offset
    hq.heappush(que_x, (x_origin, 1, y_origin, y_end))
    hq.heappush(que_x, (x_end, -1, y_origin, y_end))

sum_ = 0
pos_past_x = 0.0
que_y = []
while que_x:
    pos_curr_x, com_, y_origin, y_end = hq.heappop(que_x)

    que_temp = []
    tot_y = 0
    pos_past_y = 0
    state_ = 0
    while que_y:
        pos_curr_y, state_mod = hq.heappop(que_y)
        if state_:
            tot_y += pos_curr_y - pos_past_y
        hq.heappush(que_temp, (pos_curr_y, state_mod))
        pos_past_y = pos_curr_y
        state_ += state_mod

    hq.heappush(que_temp, (y_origin, com_))
    hq.heappush(que_temp, (y_end, -com_))
    que_y = que_temp
    sum_ += tot_y * (pos_curr_x - pos_past_x)
    pos_past_x = pos_curr_x

int_sum = int(sum_)
if sum_ == int_sum:
    print(int_sum)
else:
    print(round(sum_, 2))
exit()
