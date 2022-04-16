import sys

for _ in range(int(sys.stdin.readline())):
    N_, M_ = map(int, sys.stdin.readline().split())
    print(1)
    if N_ % 2:
        idx_n = 0
        for idx_m in range(M_):
            print('(' + str(idx_n) + ',' + str(idx_m) + ')')
        for idx_n in range(1, N_):
            if idx_n % 2:
                for idx_m in range(M_ - 1, 0, -1):
                    print('(' + str(idx_n) + ',' + str(idx_m) + ')')
            else:
                for idx_m in range(1, M_):
                    print('(' + str(idx_n) + ',' + str(idx_m) + ')')
        idx_m = 0
        for idx_n in range(N_ - 1, 0, -1):
            print('(' + str(idx_n) + ',' + str(idx_m) + ')')
    else:
        for idx_n in range(N_):
            if idx_n % 2:
                for idx_m in range(M_ - 1, -1, -1):
                    print('(' + str(idx_n) + ',' + str(idx_m) + ')')
            else:
                for idx_m in range(M_):
                    print('(' + str(idx_n) + ',' + str(idx_m) + ')')

exit()
