import sys

LIM_ = 400000

W_, N_ = map(int, sys.stdin.readline().split())
lst_ = list(map(int, sys.stdin.readline().split()))
lst_dp = [0 for _ in range(LIM_ + 1)]
is_ = False
for idx_a in range(N_):
    for idx_b in range(idx_a + 1, N_):
        idx_target = lst_[idx_a] + lst_[idx_b]
        idx_counter = W_ - idx_target
        if 0 < idx_counter <= LIM_:
            if lst_dp[idx_counter] and lst_dp[idx_counter] < idx_a:
                is_ = True
                break

            if lst_dp[idx_target]:
                lst_dp[idx_target] = min(lst_dp[idx_target], idx_b)
            else:
                lst_dp[idx_target] = idx_b
if is_:
    print("YES")
else:
    print("NO")

exit()
