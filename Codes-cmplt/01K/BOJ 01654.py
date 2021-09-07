import sys

K, N = map(int, sys.stdin.readline().split())
lst_K = []
for _ in range(K):
    lst_K.append(int(sys.stdin.readline()))

idx_l = 0
idx_r = max(lst_K)+1

while idx_l + 1 < idx_r:
    idx_ = (idx_l + idx_r) // 2
    if sum(map(lambda x: x // idx_, lst_K)) < N:
        idx_r = idx_
    else:
        idx_l = idx_

print(idx_l)