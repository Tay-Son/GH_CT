import sys

R_, C_ = map(int, sys.stdin.readline().split())
c_r, c_c = map(int, sys.stdin.readline().split())
t_ = int(sys.stdin.readline())

c_r = (c_r + t_) % (2 * R_)
c_c = (c_c + t_) % (2 * C_)

c_r = c_r if c_r <= R_ else (2 * R_ - c_r)
c_c = c_c if c_c <= C_ else (2 * C_ - c_c)

print(c_r, c_c)

exit()

import sys

R_, C_ = map(int, sys.stdin.readline().split())
c_r, c_c = map(int, sys.stdin.readline().split())
t_ = int(sys.stdin.readline())

s_r = True
s_c = True

while t_:
    print(c_r, c_c, s_r, s_c)
    t_r = abs((R_ if s_r else 0) - c_r)
    t_c = abs((C_ if s_c else 0) - c_c)

    m_ = min(t_, t_r, t_c)

    c_r += (m_ if s_r else -m_)
    c_c += (m_ if s_c else -m_)
    t_ -= m_

    if t_r == m_:
        s_r = not s_r

    if t_c == m_:
        s_c = not s_c

print(c_r, c_c)

exit()
