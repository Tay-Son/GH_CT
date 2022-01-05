import sys

N = int(sys.stdin.readline())
k = int(sys.stdin.readline())

idx_l = 0
idx_r = N ** 2 + 1
while idx_l + 1 < idx_r:
    idx_t = (idx_l + idx_r) // 2

    m_ = idx_t // N
    tot_ = N * m_

    for cnt_ in range(m_+1, N + 1):
        tot_ += idx_t // cnt_
    if tot_ > k - 1:
        idx_r = idx_t
    else:
        idx_l = idx_t
print(idx_l + 1)