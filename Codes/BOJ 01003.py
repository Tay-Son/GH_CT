import sys

lst_ = [[-1, -1] for _ in range(41)]
lst_[0] = [1, 0]
lst_[1] = [0, 1]


def func(N_):
    if lst_[N_][0] == -1:
        lst_[N_][0] = func(N_ - 1)[0] + func(N_ - 2)[0]
        lst_[N_][1] = func(N_ - 1)[1] + func(N_ - 2)[1]
    return lst_[N_]


for _ in range(int(sys.stdin.readline())):
    N_ = int(sys.stdin.readline())
    print(' '.join(map(str, func(N_))))
exit()
