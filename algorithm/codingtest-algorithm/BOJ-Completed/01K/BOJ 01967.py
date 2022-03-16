import sys
sys.setrecursionlimit(10**4)

n = int(sys.stdin.readline())
tre_ = [[] for _ in range(n+1)]

for _ in range(n-1):
    s_, e_, w_ = map(int, sys.stdin.readline().split())
    tre_[s_].append([e_, w_])
    tre_[e_].append([s_, w_])

weights_tot = [-1 for _ in range(n + 1)]


def func(idx_s, weight):
    weights_tot[idx_s] = weight
    for idx_t, w_a in tre_[idx_s]:
        if weights_tot[idx_t] == -1:
            func(idx_t, weight + w_a)


func(1, 0)

max_ = -1
idx_m = 0
for idx_ in range(1, n + 1):
    temp_ = weights_tot[idx_]
    if temp_ > max_:
        max_ = temp_
        idx_m = idx_

weights_tot = [-1 for _ in range(n + 1)]
func(idx_m, 0)

print(max(weights_tot))

exit()