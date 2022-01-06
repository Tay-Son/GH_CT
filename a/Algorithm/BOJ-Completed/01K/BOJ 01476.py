import sys
val_E, val_S, val_M = map(int, sys.stdin.readline().split())

lst_ = [15, 28, 19]

curr_ = val_S - 1
while curr_ % lst_[2] != val_M - 1:
    curr_ += lst_[1]
temp_ = lst_[1] * lst_[2]
while curr_ % lst_[0] != val_E - 1:
    curr_ += temp_
print(curr_+1)