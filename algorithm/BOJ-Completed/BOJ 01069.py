import sys
import math

X_, Y_, D_, T_ = map(int, sys.stdin.readline().split())
distance_ = (X_ ** 2 + Y_ ** 2) ** .5

if D_ / T_ > 1:
    div_ = distance_ / D_
    ceil_ = math.ceil(div_)
    floor_ = math.floor(div_)

    if floor_ == 0:
        print(min(T_ + D_ - distance_, distance_, 2 * T_))
    else:
        print(min(ceil_ * T_, floor_ * T_ + distance_ - D_ * floor_))

else:
    print(distance_)

exit()
