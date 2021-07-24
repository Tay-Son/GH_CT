import sys
import heapq as hq

N_, K_ = map(int, sys.stdin.readline().split())
lst_gem = []
for _ in range(N_):
    lst_gem.append(tuple(map(int, sys.stdin.readline().split())))
lst_bag = []
for _ in range(K_):
    lst_bag.append(int(sys.stdin.readline()))

lst_gem.sort()
que_ = []
ptr_gem = 0
tot_ = 0
for bag_ in sorted(lst_bag):
    while ptr_gem < N_ and lst_gem[ptr_gem][0] <= bag_:
        hq.heappush(que_, -lst_gem[ptr_gem][1])
        ptr_gem += 1
    if que_:
        tot_ -= hq.heappop(que_)

print(tot_)
exit()