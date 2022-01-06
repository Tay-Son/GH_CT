import sys
import math

num_tc = int(sys.stdin.readline())
for _ in range(num_tc):
    x, y = map(int, sys.stdin.readline().split())
    t = math.ceil(math.sqrt(y - x)) - 1
    answer_ = 2 * t
    if y - x > (t ** 2 + (t + 1) ** 2) // 2:
        answer_ += 1
    print(answer_)

exit()