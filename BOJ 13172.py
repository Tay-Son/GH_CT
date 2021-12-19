import sys
from math import gcd

DIV_ = 1000000007
M_ = int(sys.stdin.readline())
deno_, nume_ = map(int, sys.stdin.readline().split())
for _ in range(M_ - 1):
    n_, s_ = map(int, sys.stdin.readline().split())
    gcd_ = gcd(n_, s_)
    n_, s_ = n_ // gcd_, s_ // gcd_

    s_ = (s_ * deno_) % DIV_
    deno_ = (deno_ * n_) % DIV_
    nume_ = (nume_ * n_ + s_ * deno_) % DIV_

print((nume_ * pow(deno_, DIV_ - 2, DIV_)) % DIV_)

exit()

import sys
from math import gcd

DIV_ = 1000000007

tot_ = 0
for _ in range(int(sys.stdin.readline())):
    n_, s_ = map(int, sys.stdin.readline().split())
    gcd_ = gcd(n_, s_)
    n_ //= gcd_
    s_ //= gcd_
    tot_ += (s_ * pow(n_, DIV_ - 2, DIV_)) % DIV_
    tot_ %= DIV_

print(tot_)

exit()
