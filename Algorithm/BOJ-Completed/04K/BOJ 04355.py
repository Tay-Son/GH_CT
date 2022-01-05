import sys

N_ = int(sys.stdin.readline())
while N_:
    answer_ = N_
    for sn_ in range(2, int(N_ ** .5) + 1):
        if not N_ % sn_:
            answer_ -= answer_ // sn_
            while not N_ % sn_:
                N_ //= sn_
    if N_ > 1:
        answer_ -= answer_ // N_
    print(answer_)

    N_ = int(sys.stdin.readline())

exit()
