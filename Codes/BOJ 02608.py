import sys

lst_R = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
lst_R_offset = [[], [0], [0, 0], [0, 0, 0], [0, 1], [1],
                [1, 0], [1, 0, 0], [1, 0, 0, 0], [0, 2]]


def AtoR_(int_):
    str_out = ''
    ptr_ = 0
    for chr_ in reversed(str(int_)):
        str_temp = ''
        for offset_ in lst_R_offset[int(chr_)]:
            str_temp += lst_R[ptr_ + offset_]
        str_out = str_temp + str_out
        ptr_ += 2
    return str_out


dct_A = {'I': (1, 0), 'V': (5, 1), 'X': (10, 2), 'L': (50, 3), 'C': (100, 4), 'D': (500, 5), 'M': (1000, 6)}


def RtoA_(str_):
    tot_ = 0
    ptr_ = 0
    for chr_ in reversed(str_):
        if dct_A[chr_][1] >= ptr_:
            ptr_ = dct_A[chr_][1]
            tot_ += dct_A[chr_][0]
        else:
            tot_ -= dct_A[chr_][0]
    return tot_


str_ra = sys.stdin.readline().rstrip()
str_rb = sys.stdin.readline().rstrip()
answer_a = RtoA_(str_ra) + RtoA_(str_rb)
answer_r = AtoR_(answer_a)

print(answer_a)
print(answer_r)
