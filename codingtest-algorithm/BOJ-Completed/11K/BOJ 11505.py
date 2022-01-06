import sys
import math

DIV_ = 1000000007
N_, M_, K_ = map(int, sys.stdin.readline().split())
tre_depth = math.ceil(math.log2(N_ + 1))
cch_tpd = 2 ** tre_depth
tre_ = [1 for _ in range(2 ** (tre_depth + 1))]


def set_(idx_, val_new):
    idx_curr = cch_tpd + idx_
    tre_[idx_curr] = val_new

    while idx_curr > 1:
        idx_curr //= 2
        tre_[idx_curr] = tre_[idx_curr * 2] * tre_[idx_curr * 2 + 1]
        tre_[idx_curr] %= DIV_


def get_(idx_l, idx_r):
    ans_ = 1
    idx_l += cch_tpd
    idx_r += cch_tpd

    while idx_l < idx_r:
        if idx_l % 2:
            ans_ *= tre_[idx_l]
            ans_ %= DIV_
            idx_l += 1
        idx_l //= 2
        if not idx_r % 2:
            ans_ *= tre_[idx_r]
            ans_ %= DIV_
            idx_r -= 1
        idx_r //= 2

    if idx_l == idx_r:
        ans_ *= tre_[idx_r]
        ans_ %= DIV_

    return ans_


for idx_ in range(1, N_ + 1):
    set_(idx_, int(sys.stdin.readline()))
for _ in range(M_ + K_):
    com_, input_a, input_b = map(int, sys.stdin.readline().split())

    if com_ == 1:
        set_(input_a, input_b)
    elif com_ == 2:
        if input_a > input_b:
            input_a, input_b = input_b, input_a
        print(get_(input_a, input_b))
exit()
