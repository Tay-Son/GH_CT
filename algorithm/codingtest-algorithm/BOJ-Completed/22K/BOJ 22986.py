import sys

for _ in range(int(sys.stdin.readline())):
    N_, K_ = map(int, sys.stdin.readline().split())
    s_ = max(N_ - K_, 0)
    e_ = N_

    print((e_ - s_ + 1) * (s_ + e_) * 2)

exit()
