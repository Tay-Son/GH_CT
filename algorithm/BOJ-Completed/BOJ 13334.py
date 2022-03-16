import sys

lst_ = []
for _ in range(int(sys.stdin.readline())):
    val_a, val_b = map(int, sys.stdin.readline().split())
    if val_a > val_b:
        val_a, val_b = val_b, val_a
    lst_.append((val_a, val_b))

D_ = int(sys.stdin.readline())

lst_b = []
for s_, e_ in lst_:
    if e_ - s_ <= D_:
        lst_b.append((s_, 1))
        lst_b.append((e_ - D_, -1))
lst_b.sort()

curr_ = 0
max_ = 0
for _, each_ in lst_b:
    curr_ += -each_
    max_ = max(max_, curr_)
print(max_)

exit()