import sys
import math

str_input = sys.stdin.readline().rstrip()

P_ = 0
for idx_ in range(len(str_input) - 1):
    if str_input[idx_] != str_input[idx_ + 1]:
        P_ += 1
print(math.ceil(P_ / 2))

exit()