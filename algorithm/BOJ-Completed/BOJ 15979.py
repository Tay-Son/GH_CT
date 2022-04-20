import sys
from math import gcd

M_, N_ = map(int, sys.stdin.readline().split())

cnt_ = 0

if not (M_ == 0 and N_ == 0):
    cnt_ += 1
    if gcd(M_, N_) != 1:
        cnt_ += 1

print(cnt_)

exit()
