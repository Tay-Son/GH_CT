import sys

N_ = int(sys.stdin.readline())
lst_input = list(map(int, sys.stdin.readline().split()))
lst_input.sort()

ptr_l = 0
ptr_r = N_ - 1
min_ = abs(lst_input[ptr_l] + lst_input[ptr_r])
ptr_l_min = ptr_l
ptr_r_min = ptr_r

while ptr_l < ptr_r:
    temp_ = lst_input[ptr_l] + lst_input[ptr_r]
    temp_abs = abs(temp_)
    if temp_abs < min_:
        min_ = temp_abs
        ptr_l_min = ptr_l
        ptr_r_min = ptr_r

    if temp_ == 0:
        break
    elif temp_ < 0:
        ptr_l += 1
    else:
        ptr_r -= 1

print(lst_input[ptr_l_min], lst_input[ptr_r_min])

exit()