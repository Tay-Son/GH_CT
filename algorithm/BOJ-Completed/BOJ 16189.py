import sys

str_ = sys.stdin.readline().strip()

if len(str_) == 1:
    print('YES')

else:
    ptr_s = 0
    ptr_e = len(str_) - 1

    is_p = True
    while ptr_s <= ptr_e:
        if str_[ptr_s] != str_[ptr_e]:
            is_p = False
            break
        else:
            ptr_s += 1
            ptr_e -= 1
    if is_p:
        print('YES')
    else:
        print('NO')

exit()
