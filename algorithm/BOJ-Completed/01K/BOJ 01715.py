import sys
import heapq as hq

que_ = []
for _ in range(int(sys.stdin.readline())):
    hq.heappush(que_, int(sys.stdin.readline()))

cnt_ = 0
while len(que_) > 1:
    temp_ = hq.heappop(que_) + hq.heappop(que_)
    cnt_ += temp_
    hq.heappush(que_, temp_)

print(cnt_)

exit()