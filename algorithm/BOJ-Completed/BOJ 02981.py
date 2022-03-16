import sys
from math import gcd

lst_ = []
for _ in range(int(sys.stdin.readline())):
    lst_.append(int(sys.stdin.readline()))
lst_.sort()

gcd_ = lst_[1] - lst_[0]
for val_a, val_b in zip(lst_[2:], lst_[1:-1]):
    gcd_ = gcd(gcd_, val_a - val_b)

lst_d = []
lst_d_b = []

for num_ in range(1, int(gcd_ ** .5) + 1):
    if not gcd_ % num_:
        lst_d.append(num_)
        temp_ = gcd_ // num_
        if not num_ == temp_:
            lst_d_b.append(temp_)

print(' '.join(map(str, lst_d[1:] + lst_d_b[::-1])))

exit()
