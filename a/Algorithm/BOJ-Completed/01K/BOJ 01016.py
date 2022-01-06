import sys
import math

O_, temp_ = map(int, sys.stdin.readline().split())

max_offset = temp_ - O_
lst_ofs = [True for _ in range(max_offset + 1)]

C_ = math.ceil(temp_ ** 0.5) + 1
cnt_ = 0
if C_ > 1:
    for num_ in range(2, C_):
        num_sq = num_ * num_
        for idx_ in range(math.ceil(O_ / num_sq) * num_sq - O_, max_offset + 1, num_sq):
            if lst_ofs[idx_]:
                lst_ofs[idx_] = False
                cnt_ += 1

print(max_offset - cnt_ + 1)
exit()
