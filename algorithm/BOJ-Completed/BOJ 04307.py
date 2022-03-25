import sys

for _ in range(int(sys.stdin.readline())):
    L_, N_ = map(int, sys.stdin.readline().split())
    min_ = 0
    max_ = 0
    for _ in range(N_):
        val_ = int(sys.stdin.readline())
        min_ = max(min_, min(val_, L_ - val_))
        max_ = max(max_, max(val_, L_ - val_))
    print(min_, max_)

exit()
