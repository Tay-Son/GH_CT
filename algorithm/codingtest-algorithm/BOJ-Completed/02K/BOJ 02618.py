import sys

INF_ = 1000000000
lst_ = [(0, 0)]


def dist_(idx_a, idx_b):
    r_a, c_a = (1, 1) if not idx_a else lst_[idx_a]
    r_b, c_b = (N_, N_) if not idx_b else lst_[idx_b]
    return abs(r_a - r_b) + abs(c_a - c_b)


N_ = int(sys.stdin.readline())
W_ = int(sys.stdin.readline())

for _ in range(W_):
    lst_.append(tuple(map(int, sys.stdin.readline().split())))

mat_dp = [[(0, 0) for _ in range(W_ + 1)] for _ in range(W_ + 1)]
mat_dp[0][1] = (dist_(0, 1), 0)
mat_dp[1][0] = (dist_(1, 0), 0)

for cnt_ in range(2, W_ + 1):
    min_c = INF_
    min_r = INF_
    min_c_idx = 0
    min_r_idx = 0
    for cnt_sub in range(cnt_ - 1):
        mat_dp[cnt_sub][cnt_] = (mat_dp[cnt_sub][cnt_ - 1][0] + dist_(cnt_ - 1, cnt_), -1)
        mat_dp[cnt_][cnt_sub] = (mat_dp[cnt_ - 1][cnt_sub][0] + dist_(cnt_, cnt_ - 1), -1)

        temp_ = mat_dp[cnt_ - 1][cnt_sub][0] + dist_(cnt_sub, cnt_)
        if min_r > temp_:
            min_r = temp_
            min_r_idx = cnt_sub

        temp_ = mat_dp[cnt_sub][cnt_ - 1][0] + dist_(cnt_, cnt_sub)
        if min_c > temp_:
            min_c = temp_
            min_c_idx = cnt_sub

    mat_dp[cnt_ - 1][cnt_] = (min_r, min_r_idx)
    mat_dp[cnt_][cnt_ - 1] = (min_c, min_c_idx)

min_ = INF_
idx_min = 0
is_1 = True
for cnt_ in range(W_):
    if mat_dp[cnt_][W_][0] < min_:
        min_ = mat_dp[cnt_][W_][0]
        idx_min = cnt_
        is_1 = True
    if mat_dp[W_][cnt_][0] < min_:
        min_ = mat_dp[W_][cnt_][0]
        idx_min = cnt_
        is_1 = False

print(min_)
lst_ = []
if is_1:
    lst_.append(1)
    idx_curr_r = idx_min
    idx_curr_c = W_
else:
    lst_.append(2)
    idx_curr_r = W_
    idx_curr_c = idx_min

for cnt_ in range(W_ - 1):
    if abs(idx_curr_r - idx_curr_c) != 1:
        if idx_curr_r > idx_curr_c:
            idx_curr_r -= 1
            lst_.append(2)
        else:
            idx_curr_c -= 1
            lst_.append(1)
    else:
        if lst_[-1] == 1:
            idx_curr_c = mat_dp[idx_curr_r][idx_curr_c][1]
            lst_.append(2)
        else:
            idx_curr_r = mat_dp[idx_curr_r][idx_curr_c][1]
            lst_.append(1)
for each_ in reversed(lst_):
    print(each_)

for each_ in mat_dp:
    print(each_)
print()
exit()
