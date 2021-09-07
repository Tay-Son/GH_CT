import sys
import heapq as hq

que_ = []
num_com = int(sys.stdin.readline())
for _ in range(num_com):
    com_ = int(sys.stdin.readline())
    if not com_:
        if len(que_):
            print(hq.heappop(que_)[1])
        else:
            print(0)
    else:
        hq.heappush(que_, (abs(com_ * 2 + (com_ > 0)), com_))