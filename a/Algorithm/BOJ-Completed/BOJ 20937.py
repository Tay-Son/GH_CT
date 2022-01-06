import sys
from collections import Counter

N_ = int(sys.stdin.readline())
print(max(Counter(map(int, sys.stdin.readline().split())).values()))

exit()