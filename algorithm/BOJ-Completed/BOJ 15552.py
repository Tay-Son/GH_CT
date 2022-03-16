import sys

num_input = int(sys.stdin.readline())
for _ in range(num_input):
    a, b = map(int,sys.stdin.readline().split())
    print(a+b)