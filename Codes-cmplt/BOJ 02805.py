import sys

N, M = map(int, sys.stdin.readline().split())
lst_wood = list(map(int, sys.stdin.readline().split()))
lst_wood.sort()


def func(H):
    answer_ = 0
    for wood in lst_wood:
        if wood > H:
            answer_ += (wood - H)
    return answer_


idx_l = 0
idx_r = max(lst_wood) + 1
while idx_l + 1 < idx_r:
    idx_t = (idx_l + idx_r) // 2
    val_ = func(idx_t)
    if val_ < M:
        idx_r = idx_t
    else:
        idx_l = idx_t

print(idx_l)