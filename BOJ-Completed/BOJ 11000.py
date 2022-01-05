import sys

N_ = int(sys.stdin.readline())
lst_ = []
for _ in range(N_):
    S_, T_ = map(int, sys.stdin.readline().split())
    lst_.append((S_, 1))
    lst_.append((T_, -1))
lst_.sort()

cur_ = 0
max_ = 0
for trs_, val_ in lst_:
    cur_ += val_
    max_ = max(max_, cur_)

print(max_)

exit()
