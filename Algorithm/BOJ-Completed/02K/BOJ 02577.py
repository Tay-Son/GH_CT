import sys
from collections import Counter

A = int(sys.stdin.readline())
B = int(sys.stdin.readline())
C = int(sys.stdin.readline())

val_ = A * B * C
dct_ = Counter(str(A * B * C))
for cnt_ in range(0,10):
    print(dct_[str(cnt_)])