import sys

A_, B_ = map(int, sys.stdin.readline().split())

set_A = set(map(int, sys.stdin.readline().split()))
set_B = set(map(int, sys.stdin.readline().split()))
set_U = set_A.union(set_B)

print(len(set_U) * 2 - A_ - B_)

exit()
