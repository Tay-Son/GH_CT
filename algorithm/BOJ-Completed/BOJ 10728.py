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