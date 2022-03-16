import sys

INF_ = 10 ** 18

N_, K_ = map(int, sys.stdin.readline().split())
N_s = '0' * (max(0, K_ - len(str(N_)))) + str(N_)
L_ = len(N_s)

grd_dp = [[-1 for _ in range(2 ** 10)] for _ in range(L_)]




def rec_(val_, depth_, bit_, cnt_, as_):
    print(val_, depth_, bin(bit_)[2:], cnt_)
    if depth_ == L_:
        if cnt_ == K_:
            return val_
        else:
            return ''
    else:
        if grd_dp[depth_][bit_] == -1:
            temp_ = ''

            if as_:
                if cnt_ == K_:
                    for num_ in range(int(N_s[depth_])):
                        if (1 << num_) & bit_:
                            temp_ = rec_(str(num_), depth_ + 1, bit_, cnt_, as_)

                        if len(temp_):
                            grd_dp[depth_][bit_] = temp_
                            break
                else:
                    for num_ in range(10):
                        if not (1 << num_) & bit_:
                            temp_ = rec_(str(num_), depth_ + 1, bit_, cnt_, as_)
            else:
                for num_ in range(int(N_s[depth_]), 10):
                    if (1 << num_) & bit_:
                        temp_ = rec_(str(num_), depth_ + 1, bit_, cnt_, as_)
                    elif cnt_ < K_:
                        temp_ = rec_(str(num_), depth_ + 1, bit_ | 1 << num_, cnt_ + 1, True)

                    if len(temp_):
                        grd_dp[depth_][bit_] = temp_
                        break

            grd_dp[depth_][bit_] = temp_
        return val_ + grd_dp[depth_][bit_]


for num_ in range(int(N_s[0]), 10):
    temp_ = rec_(str(num_), 1, 1 << num_, 1, False)
    if len(temp_):
        print(temp_)
        break

exit()
