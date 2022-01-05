import sys

N_, M_ = map(int, sys.stdin.readline().split())
dct_ = dict()
for _ in range(N_):
    key_, value_ = sys.stdin.readline().split()
    dct_[key_] = value_
for _ in range(M_):
    print(dct_[sys.stdin.readline().strip()])
exit()