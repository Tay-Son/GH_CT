import sys
import heapq as hq

N_ = int(sys.stdin.readline())

val_input = int(sys.stdin.readline())
que_l = [-val_input]
que_r = []

print(-que_l[0])
if N_ > 0:
    for cnt_ in range(1, N_):
        val_input = int(sys.stdin.readline())
        if val_input <= -que_l[0]:
            hq.heappush(que_l, -val_input)
            if len(que_l) > len(que_r) + 1:
                hq.heappush(que_r, -hq.heappop(que_l))
        else:
            hq.heappush(que_r, val_input)
            if len(que_r) > len(que_l):
                temp_ = hq.heappop(que_r)
                hq.heappush(que_l, -temp_)
        print(-que_l[0])
