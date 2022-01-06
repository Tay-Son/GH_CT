import sys

lst_ = [0 for _ in range(10001)]
for _ in range(int(sys.stdin.readline())):
    lst_[int(sys.stdin.readline().rstrip())] += 1

idx_ = 0
while idx_ < 10001:
    num_ = lst_[idx_]
    while num_:
        print(idx_)
        num_ -= 1
    idx_ += 1

exit()

import sys
import heapq as hq

hqu_ = []
for _ in range(int(sys.stdin.readline())):
    hq.heappush(hqu_, int(sys.stdin.readline()))
while hqu_:
    print(hq.heappop(hqu_))

exit()
