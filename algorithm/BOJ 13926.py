import sys
import random
from math import gcd
from itertools import combinations as cb

sys.setrecursionlimit(999999)


def mod_pow(x_, p_, m_):
    ans_ = 1
    x_ %= m_
    while p_:
        if p_ % 2:
            ans_ = (x_ * ans_) % m_
        x_ = (x_ * x_) % m_
        p_ //= 2
    return ans_


def is_composite(x_, p_, m_, s_):
    x_ = mod_pow(x_, p_, m_)
    if (x_ == 1) or (x_ == m_ - 1):
        return False
    else:
        for _ in range(s_ - 1):
            x_ = (x_ * x_) % m_
            if x_ == (m_ - 1):
                return False
        else:
            return True


def is_prime_MR(x_):
    if x_ < 2:
        return False
    else:
        s_ = 0
        m_ = x_ - 1
        while not m_ % 2:
            m_ //= 2
            s_ += 1

        for p_ in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]:
            if x_ == p_:
                return True
            if is_composite(p_, m_, x_, s_):
                return False
        else:
            return True


def PR_(x_):
    if is_prime_MR(x_) or x_ == 1:
        return x_
    elif not x_ % 2:
        return 2
    else:
        u_ = random.randrange(2, x_)
        v_ = u_
        w_ = random.randrange(1, x_)
        d_ = 1
        while d_ == 1:
            u_ = ((u_ * u_ % x_) + w_ + x_) % x_
            v_ = ((v_ * v_ % x_) + w_ + x_) % x_
            v_ = ((v_ * v_ % x_) + w_ + x_) % x_
            d_ = gcd(abs(u_ - v_), x_)
            if d_ == x_:
                return PR_(x_)
        if is_prime_MR(d_):
            return d_
        else:
            return PR_(d_)


N_ = int(sys.stdin.readline())

if N_ == 1:
    print(N_)
else:
    N_temp = N_
    tot_ = N_

    set_ = set()
    while 1 < N_temp:
        div_ = PR_(N_temp)
        N_temp //= div_
        set_.add(div_)

    for mag_ in range(1, len(set_) + 1):
        for cb_ in cb(set_, mag_):
            mag_sub = 1
            for each_ in cb_:
                mag_sub *= each_

            if mag_ % 2:
                tot_ -= N_ // mag_sub
            else:
                tot_ += N_ // mag_sub
    print(tot_)

exit()
