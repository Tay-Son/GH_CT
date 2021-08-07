import sys
import math

N_ = int(sys.stdin.readline())
M_ = int(sys.stdin.readline())
lst_b = list(map(int, sys.stdin.readline().split()))
min_ = abs(N_ - 100)
if N_ > 0:
    temp_ = math.floor(math.log(N_, 10)) + 1
else:
    temp_ = 1
for num_ in range(10 ** temp_ * 2):
    is_ = True
    for each_ in list(map(int, str(num_))):
        if each_ in lst_b:
            is_ = False
            break
    if is_:
        min_ = min(min_, abs(N_ - num_) + len(str(num_)))

print(min_)