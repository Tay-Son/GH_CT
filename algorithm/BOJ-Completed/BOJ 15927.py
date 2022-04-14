import sys

str_ = sys.stdin.readline().rstrip()
len_ = len(str_)

is_p = True
is_a = True
ptr_s = 0
ptr_e = len_ - 1

while ptr_s < ptr_e:
    if str_[ptr_s] != str_[0]:
        is_a = False
    if str_[ptr_s] != str_[ptr_e]:
        is_p = False
        break
    ptr_s += 1
    ptr_e -= 1
if str_[ptr_s] != str_[0]:
    is_a = False

if not is_p:
    print(len_)
else:
    if not is_a:
        print(len_ - 1)
    else:
        print(-1)
exit()
