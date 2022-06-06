import sys
import random
from math import gcd

sys.setrecursionlimit(9999)


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
while N_ % 4 == 0:
    N_ //= 4
if N_ % 8 == 7:
    print(4)
else:
    temp_N = N_
    lst_ = []
    while 1 < temp_N:
        div_ = PR_(temp_N)
        temp_N //= div_
        lst_.append(div_)

    set_ = set()
    for each_ in lst_:
        if each_ in set_:
            set_.remove(each_)
        else:
            set_.add(each_)

    for each_ in set_:
        if each_ % 4 == 3:
            print(3)
            break
    else:
        if int(N_ ** .5) * int(N_ ** .5) != N_:
            print(2)
        else:
            print(1)

exit()
