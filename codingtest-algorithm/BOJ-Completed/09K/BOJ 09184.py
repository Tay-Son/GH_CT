import sys

cub_dp = [[[-1 for _ in range(20)] for _ in range(20)] for _ in range(20)]


def func_(val_a, val_b, val_c):
    if val_a < 0 or val_b < 0 or val_c < 0:
        return 1
    elif 19 < val_a or 19 < val_b or 19 < val_c:
        return func_(19, 19, 19)
    else:
        if cub_dp[val_a][val_b][val_c] == -1:
            if val_a < val_b < val_c:
                cub_dp[val_a][val_b][val_c] = \
                    func_(val_a, val_b, val_c - 1) + \
                    func_(val_a, val_b - 1, val_c - 1) - \
                    func_(val_a, val_b - 1, val_c)
            else:
                cub_dp[val_a][val_b][val_c] = \
                    func_(val_a - 1, val_b, val_c) + \
                    func_(val_a - 1, val_b - 1, val_c) + \
                    func_(val_a - 1, val_b, val_c - 1) - \
                    func_(val_a - 1, val_b - 1, val_c - 1)
        return cub_dp[val_a][val_b][val_c]


val_a, val_b, val_c = map(int, sys.stdin.readline().split())
while not (val_a == -1 and val_b == -1 and val_c == -1):
    print('w(' + str(val_a) + ', ' + str(val_b) + ', ' + str(val_c) + ') = ' + \
          str(func_(val_a - 1, val_b - 1, val_c - 1)))
    val_a, val_b, val_c = map(int, sys.stdin.readline().split())
exit()