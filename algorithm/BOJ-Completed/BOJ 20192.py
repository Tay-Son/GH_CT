import sys

_ = int(sys.stdin.readline())
lst_ = list(map(int, sys.stdin.readline().split()))

is_asc = True
cnt_ = 0
for val_a, val_b in zip(lst_[:-1], lst_[1:]):
    if val_b < val_a and is_asc:
        cnt_ += 1
        is_asc = False
    elif val_a < val_b and not is_asc:
        is_asc = True
if is_asc and cnt_:
    cnt_ += 1
tot_ = 0
while cnt_:
    cnt_ = (cnt_ // 2) + int((cnt_ & 1) and (cnt_ != 1))
    tot_ += 1
print(tot_)

exit()
