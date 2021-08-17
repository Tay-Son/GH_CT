import sys
sys.setrecursionlimit(10**4)

divider_ = 10007

N_, K_ = map(int, sys.stdin.readline().split())
dct_dct = dict()


def func_(N_, K_):
    if K_ != 0 and K_ != N_:
        if N_ not in dct_dct:
            dct_dct[N_] = dict()
            dct_dct[N_][K_] = (func_(N_ - 1, K_ - 1) + func_(N_ - 1, K_)) % divider_
        elif K_ not in dct_dct[N_]:
            dct_dct[N_][K_] = (func_(N_ - 1, K_ - 1) + func_(N_ - 1, K_)) % divider_
        return dct_dct[N_][K_]

    else:
        return 1


print(func_(N_, K_))

exit()
