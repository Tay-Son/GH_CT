import sys
from math import gcd

for _ in range(int(sys.stdin.readline())):
    a_, b_ = map(int, sys.stdin.readline().split())
    gcd_ = gcd(a_, b_)
    print(a_ * b_ // gcd_)

exit()
