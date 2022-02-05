import sys

def rec_(lst_, idx_):


for _ in range(int(sys.stdin.readline())):
    N_, L_, K_ = map(int, sys.stdin.readline().split())
    lst_ = []
    for _ in range(N_):
        pos_, idx_ = map(int, sys.stdin.readline().split())
        state_ = True if idx_ > 0 else False
        idx_ = abs(idx_)
        lst_.append((pos_, state_, idx_))

exit()
