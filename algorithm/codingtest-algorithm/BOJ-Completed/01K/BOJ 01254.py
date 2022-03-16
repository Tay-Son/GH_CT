import sys

str_ = sys.stdin.readline().rstrip()

offset_ = 0
while offset_ < len(str_):
    ptr_l = offset_
    ptr_r = len(str_) - 1
    while ptr_l < ptr_r and str_[ptr_l] == str_[ptr_r]:
        ptr_l += 1
        ptr_r -= 1

    if ptr_l >= ptr_r:
        print(ptr_l, ptr_r)
        break
    else:
        offset_ += 1

print(offset_ + len(str_))

exit()
