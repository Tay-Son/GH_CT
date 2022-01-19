import sys
sys.setrecursionlimit(2501)

str_ = sys.stdin.readline().rstrip()
N_ = len(str_)
lst_n = [1 for _ in range(N_)]

lst_dp = [-1 for _ in range(N_ + 1)]
lst_dp[N_] = 0
lst_pal = [-1 for _ in range(2 * N_ - 1)]


def is_pal(idx_s, idx_e):
    sum_ = idx_s + idx_e - 1
    if lst_pal[sum_] == -1:
        if not sum_ % 2:
            cnt_ = 1
            ptr_l = sum_ // 2
            ptr_r = sum_ // 2
            while 0 <= ptr_l - cnt_ and ptr_r + cnt_ < N_ and str_[ptr_l - cnt_] == str_[ptr_r + cnt_]:
                cnt_ += 1
            lst_pal[sum_] = cnt_ * 2 - 1
        else:
            cnt_ = 0
            ptr_l = sum_ // 2
            ptr_r = sum_ // 2 + 1
            while 0 <= ptr_l - cnt_ and ptr_r + cnt_ < N_ and str_[ptr_l - cnt_] == str_[ptr_r + cnt_]:
                cnt_ += 1
            lst_pal[sum_] = cnt_ * 2

    # print(idx_s, idx_e, sum_, lst_pal[sum_])

    if lst_pal[sum_] >= idx_e - idx_s:
        return True
    else:
        return False

for idx_s in range(N_-1,-1,-1):
    lst_dp

def rec_(idx_s):
    if lst_dp[idx_s] == -1:
        min_ = 2500
        for idx_e in range(idx_s + 1, N_ + 1):
            if is_pal(idx_s, idx_e):
                min_ = min(min_, rec_(idx_e))
        lst_dp[idx_s] = min_ + 1

    return lst_dp[idx_s]


print(rec_(0))
print(lst_pal)
print(lst_dp)
print(len(str_))

exit()
