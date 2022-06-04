import sys


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

        for p_ in [2, 3, 5, 7, 11, 13]:
            if m_ == p_:
                return True
            if is_composite(p_, m_, x_, s_):
                return False
        else:
            return True


cnt_ = 0
for _ in range(int(sys.stdin.readline())):
    val_ = int(sys.stdin.readline())
    if is_prime_MR(val_ * 2 + 1):
        print(val_)
        cnt_ += 1
print(cnt_)
exit()
