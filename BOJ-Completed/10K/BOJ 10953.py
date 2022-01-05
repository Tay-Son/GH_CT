import sys

num_tc = int(sys.stdin.readline())
for _ in range(num_tc):
    a, b = map(int, sys.stdin.readline().split(','))
    print(a + b)