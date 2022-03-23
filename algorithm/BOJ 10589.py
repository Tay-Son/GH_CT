import sys

R_, C_ = map(int, sys.stdin.readline().split())
print(R_ // 2 + C_ // 2)
for idx_r in range(1, R_, 2):
    print(idx_r + 1, 1, idx_r + 1, C_)
for idx_c in range(1, C_, 2):
    print(1, idx_c + 1, R_, idx_c + 1)

exit()
