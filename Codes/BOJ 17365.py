import sys

divider_ = 10 ** 9 + 7
tri_t = [0 for _ in range(27)]

tri_ = [tri_t.copy()]

for _ in range(int(sys.stdin.readline())):
    idx_tri = 0
    for each_ in sys.stdin.readline().rstrip():
        tri_[idx_tri][0] += 1
        idx_temp = ord(each_) - ord('a') + 1
        if not tri_[idx_tri][idx_temp]:
            tri_[idx_tri][idx_temp] = len(tri_)
            tri_.append(tri_t.copy())
        idx_tri = tri_[idx_tri][idx_temp]
    tri_[idx_tri][0] += 1

str_ = sys.stdin.readline().rstrip()
lst_dp = [0 for _ in range(len(str_) + 1)]
lst_dp[-1] = 1

for idx_ in range(len(str_) - 1, -1, -1):
    tot_ = 0
    idx_tri = 0
    for idx_sub in range(idx_, len(str_)):
        idx_temp = ord(str_[idx_sub]) - ord('a') + 1
        idx_temp2 = tri_[idx_tri][idx_temp]
        if idx_temp2:
            idx_tri = idx_temp2
            tot_ += tri_[idx_tri][0] * lst_dp[idx_sub + 1]
            tot_ %= divider_
        else:
            break
    lst_dp[idx_] = tot_

print(lst_dp[0])

exit()
