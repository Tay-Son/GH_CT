import sys


def cus_mult(cus_a, cus_b):
    return [cus_a[0] * cus_b[0] + 5  * cus_a[1] * cus_b[1], cus_a[0] * cus_b[1] + cus_a[1] * cus_b[0]]


def cus_pow(cus_, num_):
    cus_o = [1, 0]
    while num_:
        num_, is_ = divmod(num_, 2)
        if is_:
            cus_o = cus_mult(cus_o, cus_)
        cus_ = cus_mult(cus_, cus_)
    return cus_o


for case_ in range(1, int(sys.stdin.readline()) + 1):
    cus_ = cus_pow([3, 1], int(sys.stdin.readline()))
    print(cus_[0])

exit()
