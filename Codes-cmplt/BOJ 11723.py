import sys

set_ = [False for _ in range(21)]

for _ in range(int(sys.stdin.readline())):
    com_ = sys.stdin.readline().split()
    if len(com_) > 1:
        par_ =
    com_ = com_[0]

    if com_ == 'add':
        set_[int(com_[1])] = True
    elif com_ == 'remove':
        set_[int(com_[1])] = False
    elif com_ == 'check':
        sys.stdout.write('1\n' if set_[int(com_[1])] else '0\n')
    elif com_ == 'toggle':
        set_[int(com_[1])] = not set_[int(com_[1])]
    elif com_ == 'all':
        for num_ in range(20):
            set_[num_] = True
    elif com_ == 'empty':
        for num_ in range(20):
            set_[num_] = False
exit()

import sys

set_ = 0

for _ in range(int(sys.stdin.readline())):
    com_ = sys.stdin.readline().split()
    if len(com_) > 1:
        par_ = 2 ** (int(com_[1]) - 1)
    com_ = com_[0]

    if com_ == 'add':
        set_ |= par_
    elif com_ == 'remove':
        set_ &= ~par_
    elif com_ == 'check':
        sys.stdout.write('1\n' if (set_ & par_) else '0\n')
    elif com_ == 'toggle':
        set_ ^= par_
    elif com_ == 'all':
        set_ = 2 ** 20 - 1
    elif com_ == 'empty':
        set_ = 0
exit()
