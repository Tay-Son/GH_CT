import sys

N_, K_ = map(int, sys.stdin.readline().split())
lst_input = list(map(int, sys.stdin.readline().split()))

mat_dp = [[-1 for _ in range(N_)] for _ in range(N_)]


def func(ptr_s, ptr_e):
    if mat_dp[ptr_s][ptr_e] == -1:
        if ptr_s == ptr_e:
            mat_dp[ptr_s][ptr_e] = 0
        else:
            min_ = 201
            for ptr_ in range(ptr_s, ptr_e):
                temp_ = 0
                if lst_input[ptr_s] != lst_input[ptr_ + 1]:
                    temp_ += 1
                min_ = min(min_, func(ptr_s, ptr_) + func(ptr_ + 1, ptr_e) + temp_)
            mat_dp[ptr_s][ptr_e] = min_
    return mat_dp[ptr_s][ptr_e]


print(func(0, N_ - 1))

exit()
