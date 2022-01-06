import sys
import math

for _ in range(int(sys.stdin.readline())):
    N_, K_ = map(int, sys.stdin.readline().split())
    depth_max = math.ceil(math.log2(N_))
    val_cache = 2 ** depth_max
    tre_ = [[0, 0] for _ in range(val_cache)] + \
           [[idx_, idx_] for idx_ in range(val_cache)]
    for idx_tre in range(val_cache - 1, 0, -1):
        tre_[idx_tre][0] = min(tre_[idx_tre * 2][0], tre_[idx_tre * 2 + 1][0])
        tre_[idx_tre][1] = max(tre_[idx_tre * 2][1], tre_[idx_tre * 2 + 1][1])

    for _ in range(K_):
        com_, val_a, val_b = map(int, sys.stdin.readline().split())
        if com_ == 0:
            idx_a = val_cache + val_a
            idx_b = val_cache + val_b
            temp_a = tre_[idx_a][0]
            temp_b = tre_[idx_b][0]
            tre_[idx_a][0], tre_[idx_a][1] = temp_b, temp_b
            tre_[idx_b][0], tre_[idx_b][1] = temp_a, temp_a
            idx_a //= 2
            idx_b //= 2
            while idx_a != idx_b:
                tre_[idx_a][0] = min(tre_[idx_a * 2][0], tre_[idx_a * 2 + 1][0])
                tre_[idx_a][1] = max(tre_[idx_a * 2][1], tre_[idx_a * 2 + 1][1])
                tre_[idx_b][0] = min(tre_[idx_b * 2][0], tre_[idx_b * 2 + 1][0])
                tre_[idx_b][1] = max(tre_[idx_b * 2][1], tre_[idx_b * 2 + 1][1])
                idx_a //= 2
                idx_b //= 2
            while idx_a > 0:
                tre_[idx_a][0] = min(tre_[idx_a * 2][0], tre_[idx_a * 2 + 1][0])
                tre_[idx_a][1] = max(tre_[idx_a * 2][1], tre_[idx_a * 2 + 1][1])
                idx_a //= 2

        elif com_ == 1:
            idx_a = val_cache + val_a
            idx_b = val_cache + val_b
            min_ = 10 ** 5
            max_ = 0
            while idx_a < idx_b:
                if idx_a % 2:
                    min_ = min(min_, tre_[idx_a][0])
                    max_ = max(max_, tre_[idx_a][1])
                    idx_a += 1
                if not idx_b % 2:
                    min_ = min(min_, tre_[idx_b][0])
                    max_ = max(max_, tre_[idx_b][1])
                    idx_b -= 1
                idx_a //= 2
                idx_b //= 2

            if idx_a == idx_b:
                min_ = min(min_, tre_[idx_a][0])
                max_ = max(max_, tre_[idx_a][1])

            if min_ == val_a and max_ == val_b:
                print('YES')
            else:
                print('NO')

exit()
