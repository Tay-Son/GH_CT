import sys
import heapq as hq

sys.setrecursionlimit(10 ** 5)

N_, M_ = map(int, sys.stdin.readline().split())

grp_ = [[] for _ in range(N_ + 1)]
lst_nc = [0 for _ in range(N_ + 1)]
for _ in range(M_):
    idx_c, idx_s = map(int, sys.stdin.readline().split())
    grp_[idx_c].append(idx_s)
    lst_nc[idx_s] += 1

hqu_ = []

for idx_s in range(1, N_ + 1):
    if not lst_nc[idx_s]:
        hq.heappush(hqu_, idx_s)

lst_answer = []
while hqu_:
    idx_s = hq.heappop(hqu_)
    for idx_c in sorted(grp_[idx_s]):
        lst_nc[idx_c] -= 1
        if not lst_nc[idx_c]:
            hq.heappush(hqu_, idx_c)
    lst_answer.append(idx_s)

print(' '.join(map(str, lst_answer)))

exit()
