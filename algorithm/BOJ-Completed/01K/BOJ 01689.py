import sys

N_ = int(sys.stdin.readline())

lst_ = []

for _ in range(N_):
    s_, e_ = map(int, sys.stdin.readline().split())
    lst_.append((s_, 1))
    lst_.append((e_, -1))

lst_.sort()

curr_ = 0
max_ = 0

for each_ in lst_:
    curr_ += each_[1]
    max_ = max(max_, curr_)
print(max_)

exit()