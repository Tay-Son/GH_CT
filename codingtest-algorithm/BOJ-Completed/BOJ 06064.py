import sys
import math

T_ = int(sys.stdin.readline())

for _ in range(T_):
    M_, N_, x_, y_ = map(int, sys.stdin.readline().split())
    x_ -= 1
    y_ -= 1

    is_ = False
    for P_ in range(y_, abs(M_ * N_) // math.gcd(M_, N_), N_):
        if P_ % M_ == x_:
            is_ = True
            break
    if is_:
        print(P_ + 1)
    else:
        print(-1)
