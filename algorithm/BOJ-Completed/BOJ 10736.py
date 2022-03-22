import sys
import math

for _ in range(int(sys.stdin.readline())):
    N_ = int(sys.stdin.readline())
    if N_ == 1:
        print(1)
        print(1)
    else:
        s_ = 2 ** (int(math.log2(N_)) - 1)
        e_ = min(3 * s_ - 1, N_) + 1
        lst_ = list(range(s_, e_))
        print(len(lst_))
        print(' '.join(map(str, lst_)))
exit()

import sys
from itertools import combinations as cb
from itertools import product as pd

for N_ in range(int(sys.stdin.readline())):
    # N_ = int(sys.stdin.readline())
    is_run = True
    for num_ in range(N_, 0, -1):
        if is_run:
            # for cb_ in cb(range(N_, 0, -1), num_, ):
            for cb_ in cb(range(1, N_ + 1), num_, ):
                is_ = True
                for pd_ in pd(cb_, repeat=3):
                    if not pd_[0] ^ pd_[1] ^ pd_[2]:
                        is_ = False
                        break
                if is_:
                    print(str(N_).zfill(3), str(len(cb_)).zfill(3))
                    for each_ in cb_:
                        print(bin(each_)[2:].zfill(6), str(each_).zfill(3))
                    print()

                    is_run = False
                    break
        else:
            break

exit()

from itertools import product as pd

import sys
import math


def next_(num_):
    lst_ = list(bin(num_)[2:])
    idx_ = len(lst_) - 1
    while lst_[idx_] != '1':
        lst_[idx_] = '1'
        idx_ -= 1
    lst_[idx_] = '0'
    return int(''.join(lst_), 2)


for _ in range(int(sys.stdin.readline())):
    N_ = int(sys.stdin.readline())
    b_ = int(math.log2(N_))

    lst_ = []
    for _ in range(min(2 ** b_, 2 ** (b_ - 1) + N_ - 2 ** b_ + 1)):
        print(bin(N_)[2:].zfill(8), str(N_).zfill(3))
        lst_.append(N_)
        N_ = next_(N_)

    for pd_ in pd(lst_, repeat=3):
        if not pd_[0] ^ pd_[1] ^ pd_[2]:
            print('F')
            break
    else:
        print('T')

    print(len(lst_))
    print(' '.join(map(str, lst_)))

exit()
