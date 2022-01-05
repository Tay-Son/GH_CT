import sys

N, C = map(int, sys.stdin.readline().split())

lst_ = []
for _ in range(N):
    lst_.append(int(sys.stdin.readline()))
lst_.sort()


def func(offset_):
    cnt_ = 1
    curr_ = lst_[0]
    for idx_ in range(1, N):
        temp_ = lst_[idx_]
        if temp_ - curr_ >= offset_:
            curr_ = temp_
            cnt_ += 1

    if cnt_ >= C:
        return True
    else:
        return False

idx_l = 0
idx_r = max(lst_)
while idx_l + 1 < idx_r:
    offset_ = (idx_l + idx_r) // 2
    if func(offset_):
        idx_l = offset_
    else:
        idx_r = offset_

print(idx_l)