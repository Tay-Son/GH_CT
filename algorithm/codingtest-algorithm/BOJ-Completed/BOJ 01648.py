import sys
grd_ = [[0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
        [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610],
        [0, 3, 0, 11, 0, 41, 0, 153, 0, 571, 0, 2131, 0, 7953],
        [1, 5, 11, 36, 95, 281, 781, 2245, 6336, 8160, 1700, 6987, 7410, 6182],
        [0, 8, 0, 95, 0, 1183, 0, 4923, 0, 7703, 0, 5362, 0, 5606],
        [1, 13, 41, 281, 1183, 6728, 1826, 8673, 6109, 5208, 1778, 1795, 7093, 6289],
        [0, 21, 0, 781, 0, 1826, 0, 5567, 0, 7147, 0, 5631, 0, 8010],
        [1, 34, 153, 2245, 4923, 8673, 5567, 8605, 9894, 1695, 8111, 2296, 7818, 7183],
        [0, 55, 0, 6336, 0, 6109, 0, 9894, 0, 2331, 0, 8412, 0, 1364],
        [1, 89, 571, 8160, 7703, 5208, 7147, 1695, 2331, 5606, 8159, 5570, 7982, 6167],
        [0, 144, 0, 1700, 0, 1778, 0, 8111, 0, 8159, 0, 4270, 0, 3727],
        [1, 233, 2131, 6987, 5362, 1795, 5631, 2296, 8412, 5570, 4270, 885, 1742, 3761],
        [0, 377, 0, 7410, 0, 7093, 0, 7818, 0, 7982, 0, 1742, 0, 3971],
        [1, 610, 7953, 6182, 5606, 6289, 8010, 7183, 1364, 6167, 3727, 3761, 3971, 990]]
N_, M_ = map(lambda x: int(x) - 1, sys.stdin.readline().split())
sys.stdout.write(str(grd_[N_][M_]))
exit()

import sys
from collections import deque

DIV_ = 9901

for idx_n in range(14):
    lst_temp = []
    for idx_m in range(14):
        # N_, M_ = map(int, sys.stdin.readline().split())
        # N_, M_ = max(N_, M_), min(N_, M_)
        N_, M_ = idx_n + 1, idx_m + 1
        grd_dp = [[0 for _ in range(2 ** M_ - 1)] + [1]] + [[-1 for _ in range(2 ** M_)] for _ in range(N_)]


        def rec_(bit_, idx_n):
            if grd_dp[idx_n][bit_] == -1:
                tot_ = 0
                que_ = deque([(2 ** M_ - 1, 0)])
                idx_t = idx_n - 1
                while que_:
                    bit_c, idx_m = que_.popleft()
                    if idx_m == M_:
                        tot_ += rec_(bit_c, idx_t)
                        tot_ %= DIV_
                    else:
                        if not bit_ & 1 << idx_m:
                            que_.append((bit_c, idx_m + 1))
                        else:
                            que_.append((bit_c ^ 1 << idx_m, idx_m + 1))

                            if idx_m + 1 < M_ and bit_ & 1 << (idx_m + 1):
                                que_.append((bit_c, idx_m + 2))

                grd_dp[idx_n][bit_] = tot_
            return grd_dp[idx_n][bit_]


        # print(rec_(2 ** M_ - 1, N_))
        lst_temp.append(rec_(2 ** M_ - 1, N_))
    print('[' + ','.join(map(str, lst_temp)) + '],')
exit()
