import sys

for _ in range(int(sys.stdin.readline())):
    str_ = sys.stdin.readline().rstrip()
    cnt_ = 0
    ptr_l = 0
    ptr_r = len(str_) - 1

    while ptr_l < ptr_r:
        if str_[ptr_l] == str_[ptr_r]:
            ptr_l += 1
            ptr_r -= 1
        else:
            cnt_ += 1
            cnt_sub = 0
            ptr_l_sub = ptr_l
            ptr_r_sub = ptr_r - 1
            while ptr_l_sub < ptr_r_sub:
                if str_[ptr_l_sub] == str_[ptr_r_sub]:
                    ptr_l_sub += 1
                    ptr_r_sub -= 1
                else:
                    cnt_sub += 1
                    break

            ptr_l_sub = ptr_l + 1
            ptr_r_sub = ptr_r
            while ptr_l_sub < ptr_r_sub:
                if str_[ptr_l_sub] == str_[ptr_r_sub]:
                    ptr_l_sub += 1
                    ptr_r_sub -= 1
                else:
                    cnt_sub += 1
                    break

            if cnt_sub > 1:
                cnt_ += 1
            break
    print(cnt_)

exit()
