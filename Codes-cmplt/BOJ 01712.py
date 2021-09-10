import sys
import math

A, B, C = map(int, sys.stdin.readline().split())
answer_ = 0

if B < C:
    print(math.floor(A/(C-B))+1)
else:
    print(-1)