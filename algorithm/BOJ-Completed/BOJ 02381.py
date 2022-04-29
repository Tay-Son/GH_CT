import sys

max_s = -2000000
max_d = -2000000
min_s = 2000000
min_d = 2000000

for _ in range(int(sys.stdin.readline())):
    x_, y_ = map(int, sys.stdin.readline().split())
    s_ = x_ + y_
    d_ = x_ - y_
    max_s = max(max_s, s_)
    max_d = max(max_d, d_)
    min_s = min(min_s, s_)
    min_d = min(min_d, d_)
print(max(max_s - min_s, max_d - min_d))
exit()
